from datetime import datetime


def extract():
    print("Extracting e-commerce CSV data")


def transform():
    print("Running PySpark transformations")


def validate():
    print("Performing data quality checks")


def load():
    print("Saving analytics tables")


if __name__ == "__main__":

    print("Starting DAG:", datetime.now())

    extract()
    transform()
    validate()
    load()

    print("Pipeline completed")