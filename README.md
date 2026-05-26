# 📊 Sales Analytics ETL Pipeline (Pandas + PySpark + Airflow Concepts)

## 📌 Overview
This project is a modular ETL (Extract, Transform, Load) pipeline built using Python and Pandas.  
It simulates a real-world data engineering workflow including data validation, cleaning, transformation, aggregation, and storage.

The pipeline is designed to handle both good and bad data using a quarantine system and produces analytics-ready outputs.

## ⚙️ Features

- Extract data from CSV files
- Data quality validation (null checks, duplicates, schema validation)
- Data quarantine system for bad records
- Data cleaning and transformation
- Aggregation of business metrics
- Output storage in Parquet and SQLite
- Automated daily run simulation using scheduler script
- Modular and production-style Python structure
- PySpark transformations
- Spark SQL aggregations
- Airflow DAG orchestration concepts
- Distributed data processing workflow


## 🏗️ Pipeline Architecture

```text
CSV Input
   ↓
Extract Data
   ↓
Data Quality Check
   ↓
Split Data (Good / Bad)
   ↓
Bad Data → Quarantine Folder
   ↓
Clean & Transform Good Data
   ↓
Aggregation (Metrics)
   ↓
Load to:
   ├── Parquet Files
   └── SQLite Database