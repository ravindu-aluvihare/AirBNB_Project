import os
import json
import pandas as pd


def load_config():
    # load configuration file
    with open("./config/config.json", "r") as file:
        return json.load(file)


def run_validation():

    # load config
    config = load_config()

    # path to raw listings dataset
    raw_data_path = os.path.join(
        config["data_dir"],
        "listings.csv.gz"
    )

    print("Reading raw dataset...")

    # read dataset
    df = pd.read_csv(
        raw_data_path,
        compression="gzip",
        low_memory=False
    )

    print("\n========== DATA VALIDATION ==========")

    
    total_rows = len(df)
    print(f"Total rows: {total_rows}")

    # duplicate IDs
    duplicate_ids = df["id"].duplicated().sum()
    print(f"Duplicate IDs: {duplicate_ids}")

    # missing values
    print("\nMissing Values")

    columns_to_check = [
        "id",
        "host_id",
        "price",
        "room_type"
    ]

    missing_values = {}

    for col in columns_to_check:
        missing_values[col] = int(df[col].isnull().sum())
        print(f"{col}: {missing_values[col]}")

    # clean price for validation
    df["price"] = (
        df["price"]
        .astype(str)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
    )

    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    # negative prices
    negative_prices = (df["price"] < 0).sum()
    print(f"\nNegative prices: {negative_prices}")

    # room types
    print("\nRoom Types")
    print(df["room_type"].value_counts())

    print("\nValidation completed.")

    
    # save validation rep. 
    

    report_dir = config.get("report_dir", "./report")
    os.makedirs(report_dir, exist_ok=True)

    validation_report = {
        "total_rows": int(total_rows),
        "duplicate_ids": int(duplicate_ids),
        "negative_prices": int(negative_prices),
        "missing_values": missing_values
    }

    report_path = os.path.join(report_dir, "validation_report.json")

    with open(report_path, "w") as file:
        json.dump(validation_report, file, indent=4)

    print(f"\nValidation report saved at: {report_path}")


if __name__ == "__main__":
    run_validation()