import os
import duckdb
import pandas as pd


def load_duckdb():

    print("Connecting to DuckDB...")

    # create database directory
    os.makedirs("./database", exist_ok=True)

    # connect to DuckDB
    con = duckdb.connect("./database/airbnb.duckdb")

    # load CSV files (model layer)
    dim_geography = pd.read_csv("./models/dim_geography.csv")
    dim_hosts = pd.read_csv("./models/dim_hosts.csv")
    fact_listings = pd.read_csv("./models/fact_listings.csv")

    # register DataFrames into DuckDB
    con.register("dim_geography_df", dim_geography)
    con.register("dim_hosts_df", dim_hosts)
    con.register("fact_listings_df", fact_listings)

    # create tables in DuckDB from registered dataframes
    con.execute("""
        CREATE OR REPLACE TABLE dim_geography AS
        SELECT * FROM dim_geography_df
    """)

    con.execute("""
        CREATE OR REPLACE TABLE dim_hosts AS
        SELECT * FROM dim_hosts_df
    """)

    con.execute("""
        CREATE OR REPLACE TABLE fact_listings AS
        SELECT * FROM fact_listings_df
    """)

    print("Tables loaded successfully.")

    # row counts check
    result = con.execute("""
        SELECT
            (SELECT COUNT(*) FROM dim_geography) AS geography_rows,
            (SELECT COUNT(*) FROM dim_hosts) AS host_rows,
            (SELECT COUNT(*) FROM fact_listings) AS fact_rows
    """).fetchdf()

    print("\nRow Counts:")
    print(result)

    con.close()

    print("DuckDB database created successfully.")


if __name__ == "__main__":
    load_duckdb()