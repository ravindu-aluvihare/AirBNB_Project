from data_ingestion import run_pipeline
from data_validation import run_validation
from data_cleaning import run_cleaning_pipeline
from data_modeling import run_data_modeling
from database import load_duckdb
from train_model import train_model


def main():

    print("Starting Airbnb ETL Pipeline")

    
    run_pipeline()
    run_validation()
    run_cleaning_pipeline()
    run_data_modeling()
    load_duckdb()
    train_model()

    print("\nPipeline completed successfully")


if __name__ == "__main__":
    main()