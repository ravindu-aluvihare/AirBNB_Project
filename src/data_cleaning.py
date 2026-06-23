import os
import json
import pandas as pd


def load_config():
    with open("./config/config.json", "r") as file:
        return json.load(file)


def clean_price(price_value): 
    if pd.isnull(price_value):
        return 0.0

    try:
        price_value = str(price_value)

        price_value = price_value.replace("$", "")

        price_value = price_value.replace(",", "")

        price_value = price_value.strip()

        return float(price_value)

    except ValueError:
        return 0.0


def run_cleaning_pipeline():
    config = load_config()

    raw_data_path = os.path.join(
        config["data_dir"],
        "listings.csv.gz"
    )

    print("Reading listings dataset")

    df = pd.read_csv(
        raw_data_path,
        compression="gzip",
        low_memory=False
    )

    
    print("Cleaning dataset...")

    # clean price column
    if "price" not in df.columns:
        raise ValueError("price column not found")

    df["price_clean"] = df["price"].apply(clean_price)

    # remove invalid prices
    df_filtered = df[df["price_clean"] > 0]

    # remove duplicate rows
    df_filtered = df_filtered.drop_duplicates()

    # remove missing id
    df_filtered = df_filtered.dropna(subset=["id"])

    # remove extreme price outliers
    df_filtered = df_filtered[
        df_filtered["price_clean"] < 10000
    ]

    # convert host_since to datetime
    if "host_since" in df_filtered.columns:
        df_filtered["host_since"] = pd.to_datetime(
            df_filtered["host_since"],
            errors="coerce"
        )

    # fill missing review scores with median
    if "review_scores_rating" in df_filtered.columns:
        df_filtered["review_scores_rating"] = (
            df_filtered["review_scores_rating"]
            .fillna(df_filtered["review_scores_rating"].median())
        )

    # create processed folder
    processed_dir = os.path.join(
        config["data_dir"],
        "processed"
    )

    os.makedirs(processed_dir, exist_ok=True)

    # save cleaned dataset
    clean_data_path = os.path.join(
        processed_dir,
        "listings_cleaned.csv"
    )

    df_filtered.to_csv(
        clean_data_path,
        index=False
    )


    print("\n===== Cleaning Summary =====")
    print(f"Rows before cleaning : {len(df)}")
    print(f"Rows after cleaning  : {len(df_filtered)}")
    print(f"Rows removed         : {len(df) - len(df_filtered)}")
    
    print("\nMissing values after cleaning")
    print(df_filtered.isnull().sum())

    


# entry point
if __name__ == "__main__":
    run_cleaning_pipeline()