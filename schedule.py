import time
import etl_pipeline

def run_daily():

    while True:
        print("Running daily ETL job...")

        etl_pipeline.run_pipeline()

        print("Job completed. Sleeping for 24 hours.")

        time.sleep(10)  # (use 86400 in real life)