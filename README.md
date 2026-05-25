# 📊 Sales ETL Pipeline (Pandas Data Engineering Project)

## 📌 Overview

This project is a complete end-to-end **ETL (Extract, Transform, Load) pipeline** built using Python and Pandas.

It simulates a real-world data engineering workflow where raw e-commerce customer data is:
- Extracted from CSV files
- Validated using data quality checks
- Cleaned and transformed
- Aggregated into business metrics
- Stored in multiple formats for analytics and reporting

The pipeline also includes a **quarantine system for bad data**, ensuring invalid records are isolated instead of breaking the workflow.

---

## ⚙️ Tech Stack

- Python
- Pandas
- SQLite (built-in database)
- PyArrow (for Parquet file format)
- Logging (pipeline monitoring)
- OS / File Handling
- Cron-like scheduling simulation (Python script)

---

## 💼 Business Use Case

This pipeline simulates a real-world **e-commerce data processing system** used in analytics teams.

### In a real company scenario:

- Customer order data is collected from multiple sources
- Raw data is often incomplete or messy
- Data must be validated before analysis
- Bad data is isolated for auditing
- Clean data is transformed into business insights
- Final data is used for dashboards and reporting

### This pipeline helps:

- Improve data reliability
- Ensure analytics accuracy
- Automate daily data processing
- Enable reporting systems (BI tools)

---

## 🏗️ Pipeline Architecture

```text
CSV Input (Raw Data)
        ↓
Data Extraction (Pandas read_csv)
        ↓
Data Quality Check (nulls, duplicates, schema validation)
        ↓
Split Data
   ├── Good Data
   └── Bad Data → Quarantine Folder
        ↓
Clean & Transform Good Data
        ↓
Aggregation (Business Metrics)
        ↓
Load Layer
   ├── Parquet Files (Analytics Storage)
   └── SQLite Database (Query Storage)
