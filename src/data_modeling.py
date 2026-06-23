import os
import json
import pandas as pd


def load_config():
    with open("./config/config.json", "r") as file:
        return json.load(file)


def run_data_modeling():

    config = load_config()

    # read clean dt
    clean_data_path = os.path.join(
        config["data_dir"],
        "processed",
        "listings_cleaned.csv"
    )

    print("Reading cleaned dataset...")
    df = pd.read_csv(clean_data_path, low_memory=False)

    # create model output directory
    model_dir = "./models"

    os.makedirs(model_dir, exist_ok=True)

    
    # dimension Table: Geography

    geography_cols = [
        "id",
        "neighbourhood_cleansed",
        "latitude",
        "longitude"
    ]

    dim_geography = df[geography_cols].copy()

    # rename listing id
    dim_geography.rename(
        columns={"id": "listing_id"},
        inplace=True
    )

    # create surrogate key
    dim_geography.insert(
        0,
        "geography_key",
        range(1, len(dim_geography) + 1)
    )

    dim_geography.to_csv(
        os.path.join(model_dir, "dim_geography.csv"),
        index=False
    )

    # dimension Table: Hosts

    host_cols = [
        "host_id",
        "host_name",
        "host_since",
        "host_is_superhost",
        "host_identity_verified"
    ]

    dim_hosts = df[host_cols].copy()

    # keep unique hosts
    dim_hosts = dim_hosts.drop_duplicates(
        subset=["host_id"]
    )

    # create surrogate key
    dim_hosts.insert(
        0,
        "host_key",
        range(1, len(dim_hosts) + 1)
    )

    dim_hosts.to_csv(
        os.path.join(model_dir, "dim_hosts.csv"),
        index=False
    )

    # fact Table: Listings

    fact_cols = [
        "id",
        "host_id",
        "room_type",
        "price_clean",
        "number_of_reviews",
        "review_scores_rating"
    ]

    fact_listings = df[fact_cols].copy()

    fact_listings.rename(
        columns={"id": "listing_id"},
        inplace=True
    )

    fact_listings.to_csv(
        os.path.join(model_dir, "fact_listings.csv"),
        index=False
    )

    
    print("\n Star Schema Modeling Completed")
    print(f" dim_geography rows : {len(dim_geography)}")
    print(f" dim_hosts rows     : {len(dim_hosts)}")
    print(f" fact_listings rows : {len(fact_listings)}")


if __name__ == "__main__":
    run_data_modeling()