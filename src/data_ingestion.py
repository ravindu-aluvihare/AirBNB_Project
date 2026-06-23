import os
import json
import requests
import pandas as pd
from tqdm import tqdm
from datetime import datetime


def load_config():
    with open("./config/config.json", "r") as file:
        return json.load(file)


def download_file(url, destination):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        total_size = int(response.headers.get("content-length", 0))

        with open(destination, "wb") as file, tqdm(
            total=total_size,
            unit="B",
            unit_scale=True,
            desc=os.path.basename(destination)
        ) as progress_bar:

            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
                    progress_bar.update(len(chunk))

        print(f"Downloaded {destination}")


    except Exception as e:
        print(f"Failed downloading {destination}: {e}")       


def run_pipeline():
    config = load_config()

    os.makedirs(config["data_dir"], exist_ok=True)
    os.makedirs(config["report_dir"], exist_ok=True)

    print("🚀 Starting data ingestion...")

    listings_url = config["files"]["listings"]
    calendar_url = config["files"]["calendar"]
    reviews_url = config["files"]["reviews"]

    listings_path = os.path.join(config["data_dir"], "listings.csv.gz")
    calendar_path = os.path.join(config["data_dir"], "calendar.csv.gz")
    reviews_path = os.path.join(config["data_dir"], "reviews.csv.gz")

    download_file(listings_url, listings_path)
    download_file(calendar_url, calendar_path)
    download_file(reviews_url, reviews_path)

    print("Data ingestion completed.")

# data Profiling

    df = pd.read_csv(
        listings_path,
        compression="gzip",
        low_memory=False
    )

    # create quality report
    report = {
        "city": config["city"],
        "timestamp": datetime.now().isoformat(),
        "total_rows": int(len(df)),
        "total_columns": int(len(df.columns)),
        "columns_quality": {
            "id": {
                "null_values": int(df["id"].isnull().sum()),
                "unique_values": int(df["id"].nunique())
            },
            "price": {
                "null_values": int(df["price"].isnull().sum()),
                "unique_values": int(df["price"].nunique())
            },
            "neighbourhood_cleansed": {
                "null_values": int(df["neighbourhood_cleansed"].isnull().sum()),
                "unique_values": int(df["neighbourhood_cleansed"].nunique())
            }
        }
    }

    report_path = os.path.join(
        config["report_dir"],
        "quality_report.json"
    )

    with open(report_path, "w") as file:
        json.dump(report, file, indent=4)

    print("Quality report generated successfully.")


# entry point
if __name__ == "__main__":
    run_pipeline()