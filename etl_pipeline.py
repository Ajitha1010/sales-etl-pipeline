import pandas as pd
import os
from glob import glob
import sqlite3
import logging
import config
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def data_quality_check(df):

    logging.info("Starting advanced data quality checks")

    issues = []
    score = 100
    if df.empty:
        issues.append("Dataset is empty")
        logging.error("Dataset is empty")
        return 0, issues
    required_columns = ["customer_id", "customer_city"]

    missing_cols = [
        col for col in required_columns
        if col not in df.columns
    ]

    if missing_cols:
        issues.append(f"Missing columns: {missing_cols}")
        score -= 30
        logging.warning(f"Missing columns: {missing_cols}")
    null_ratio = df.isnull().mean().mean()

    logging.info(f"Null ratio: {null_ratio:.2f}")

    if null_ratio > 0.1:
        issues.append(f"High null ratio: {null_ratio:.2f}")
        score -= 20
        logging.warning("High null ratio detected")

    dup_ratio = df.duplicated().mean()

    logging.info(f"Duplicate ratio: {dup_ratio:.2f}")

    if dup_ratio > 0.05:
        issues.append(f"High duplicate ratio: {dup_ratio:.2f}")
        score -= 20
        logging.warning("High duplicate ratio detected")

    if "customer_city" in df.columns:

        invalid_city_count = df["customer_city"].isna().sum()

        if invalid_city_count > 0:
            issues.append(f"Invalid city values: {invalid_city_count}")
            score -= 10
            logging.warning("Invalid city values found")
    logging.info(f"Data Quality Score: {score}/100")

    if issues:
        for issue in issues:
            logging.warning(issue)
    else:
        logging.info("No data quality issues found")
    return score, issues

def split_good_bad_data(df):

    logging.info("Splitting data into good and bad records")

    # -----------------------------
    # BAD DATA RULES
    # -----------------------------
    bad_condition = (
        df["customer_id"].isnull() |
        df["customer_city"].isnull()
    )

    bad_data = df[bad_condition]
    good_data = df[~bad_condition]

    logging.info(f"Good records: {len(good_data)}")
    logging.info(f"Bad records: {len(bad_data)}")

    return good_data, bad_data

def save_quarantine_data(bad_df, timestamp):

    if bad_df.empty:
        logging.info("No bad data to quarantine")
        return

    path = f"output/quarantine/bad_data_{timestamp}.parquet"

    bad_df.to_parquet(path, index=False)

    logging.warning(f"Bad data saved to quarantine: {path}")

def extract_data():
    logging.info("Starting data extraction")
    df = pd.read_csv(config.INPUT_CSV)
    logging.info(f"Loaded {len(df)} rows")
    return df

def transform_data(df):
    logging.info("Starting transformations")
    df = df.dropna()
    df = df.drop_duplicates()
    df = df.rename(columns={
        "customer_city": "city"
    })
    logging.info("Transformations completed")
    return df

def create_metrics(df):
    city_summary = (
        df.groupby("city")
        .size()
        .reset_index(name="customer_count")
    )
    return city_summary

def load_data(df, parquet_path):
    df.to_parquet(
    parquet_path,
    index=False)
    conn = sqlite3.connect(config.SQLITE_DB_PATH)
    df.to_sql(
        "city_summary",
        conn,
        if_exists="replace",
        index=False
    )
    conn.close()
    logging.info("Saving outputs")

def cleanup_old_files():

    files = sorted(
        glob(f"{config.PARQUET_OUTPUT_DIR}/city_summary_*.parquet")
    )

    if len(files) > config.RETENTION_LIMIT:

        files_to_delete = files[:-config.RETENTION_LIMIT]

        for file in files_to_delete:
            try:
                os.remove(file)
                logging.info(f"Deleted: {file}")
            except Exception as e:
                logging.error(f"Failed to delete {file}: {e}")

def run_pipeline():
    try:
        df = extract_data()
        score, issues = data_quality_check(df)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        good_df, bad_df = split_good_bad_data(df)
        save_quarantine_data(bad_df, timestamp)
        if score < 50:
            raise ValueError("Data quality too low. Pipeline stopped.")
        df = good_df
        df = transform_data(df)
        city_summary = create_metrics(df)
        parquet_path = (f"config.PARQUET_OUTPUT_DIR"
            f"city_summary_{timestamp}.parquet")
        load_data(
                city_summary,
                parquet_path)
        cleanup_old_files()
        logging.info(
        "ETL Pipeline completed successfully")
    except Exception as e:
        logging.error(
            f"Pipeline failed: {e}")
        
run_pipeline()