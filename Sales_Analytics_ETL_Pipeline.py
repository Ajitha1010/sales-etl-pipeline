# Databricks notebook source
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

# COMMAND ----------

customers_path = "/Volumes/workspace/default/data/olist_customers_dataset.csv"

customers_df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load(customers_path)

customers_df.show(5)
customers_df.printSchema()
customers_df.count()

# COMMAND ----------

from pyspark.sql.functions import col
customers_df.filter(
    col("customer_id").isNull()
).show()
clean_df = customers_df.dropna().dropDuplicates()
print("Before cleaning:", customers_df.count())
print("After cleaning:", clean_df.count())
clean_df = clean_df.withColumnRenamed(
    "customer_city",
    "city"
)

# COMMAND ----------

from pyspark.sql.functions import count

city_summary = clean_df.groupBy("city") \
    .agg(count("*").alias("total_customers")) \
    .orderBy("total_customers", ascending=False)

city_summary.show(10)

# COMMAND ----------

city_summary.write.mode("overwrite") \
    .saveAsTable("city_summary_table")

# COMMAND ----------

spark.sql("SELECT * FROM city_summary_table").show()

# COMMAND ----------

orders_path = "/Volumes/workspace/default/data/olist_orders_dataset.csv"

orders_df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load(orders_path)

orders_df.show(5)
orders_df.printSchema()

# COMMAND ----------

joined_df = orders_df.join(
    clean_df,
    on="customer_id",
    how="inner"
)

joined_df.show(5)
joined_df.count()

# COMMAND ----------

from pyspark.sql.functions import count

orders_by_city = joined_df.groupBy("city") \
    .agg(
        count("order_id").alias("total_orders")
    ) \
    .orderBy("total_orders", ascending=False)

orders_by_city.show(10)


# COMMAND ----------

status_summary = joined_df.groupBy("order_status") \
    .count()

status_summary.show()

# COMMAND ----------

orders_by_city.write \
    .mode("overwrite") \
    .saveAsTable("orders_by_city_table")

# COMMAND ----------

spark.sql("""
SELECT * 
FROM orders_by_city_table
LIMIT 10
""").show()

# COMMAND ----------

orders_by_city.toPandas().to_csv(
    "/tmp/orders_by_city.csv",
    index=False
)

# COMMAND ----------

display(orders_by_city)

# COMMAND ----------

display(status_summary)