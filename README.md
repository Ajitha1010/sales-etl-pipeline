# 📊 Sales Analytics ETL Pipeline  
### Pandas + PySpark + Airflow Concepts

---

# 📌 Overview

This project is an end-to-end **Sales Analytics ETL Pipeline** designed using modern data engineering concepts.

The pipeline processes raw e-commerce customer and order data through multiple stages including:

- Data ingestion
- Data quality validation
- Data cleaning and transformation
- Business metric aggregation
- Analytics-ready storage

The project combines:
- **Pandas** for local ETL processing
- **PySpark** for distributed data transformations
- **SQLite** for lightweight analytical storage
- **Airflow DAG concepts** for workflow orchestration simulation

This project simulates how real-world data engineering pipelines are built in analytics and cloud data platforms.

---

# ⚙️ Features

- Extract data from CSV files
- Data quality validation
  - Null checks
  - Duplicate checks
  - Schema validation
- Data quarantine system for invalid records
- Data cleaning and preprocessing
- Business KPI aggregations
- PySpark DataFrame transformations
- Spark SQL aggregations
- Output storage in:
  - Parquet format
  - SQLite database
- Airflow-style DAG orchestration simulation
- Modular and scalable project structure
- Logging and pipeline monitoring
- Daily pipeline scheduling simulation

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Local ETL processing |
| PySpark | Distributed data processing |
| Spark SQL | Data aggregation and analytics |
| SQLite | Lightweight analytical database |
| Parquet | Columnar analytics storage |
| Apache Airflow Concepts | Workflow orchestration |
| Databricks | Spark execution environment |
| Git & GitHub | Version control |
| Logging | Pipeline monitoring |

---

# 💼 Business Use Case

This project simulates a real-world **e-commerce sales analytics pipeline** used by data engineering and analytics teams.

## Real-World Scenario

E-commerce companies generate large amounts of raw transactional data daily.

Before this data can be used for:
- dashboards
- reporting
- forecasting
- customer analytics

it must go through a reliable ETL pipeline.

---

# 📈 Pipeline Objectives

The pipeline helps organizations:

- Improve data quality
- Automate daily data processing
- Detect invalid or corrupted records
- Generate business-ready datasets
- Support analytics and BI reporting
- Store optimized analytical datasets

---

# 🏗️ Pipeline Architecture

```text
Raw CSV Data
      ↓
Data Extraction
(Pandas / PySpark)
      ↓
Data Quality Validation
- Null Checks
- Duplicate Checks
- Schema Validation
      ↓
Data Split
├── Valid Records
└── Invalid Records → Quarantine Layer
      ↓
Data Cleaning & Transformation
      ↓
Business KPI Aggregations
      ↓
Load Layer
├── Parquet Storage
└── SQLite Database
      ↓
Airflow DAG Scheduling Simulation