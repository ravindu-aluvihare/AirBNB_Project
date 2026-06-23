# Airbnb Pipeline

## Overview

This project builds an end-to-end Data Engineering pipeline using Airbnb Amsterdam dataset. It includes ingestion, validation, cleaning, star schema modeling, analytics, machine learning, and dashboard visualization.

---

## Architecture

Raw Data → Validation → Cleaning → Star Schema → DuckDB → EDA → ML → Dashboard

---

## Tech Stack

* Python
* Pandas
* DuckDB
* Scikit-learn
* Streamlit
* Docker

---

## Project Structure

* data/
* models/
* report/
* src/
* dashboard/
* tests/

---

## How to Run

### 1. Install dependencies

pip install -r requirements.txt

### 2. Run pipeline

python src/main.py

### 3. Run dashboard

streamlit run dashboard/app.py

---

## Key Features

* Data validation layer
* Star schema modeling
* DuckDB analytical database
* Statistical analysis (ANOVA)
* Machine learning price prediction
* Interactive dashboard
* Dockerized pipeline


# Dashboard Preview

<img width="1545" height="2000" alt="1" src="https://github.com/user-attachments/assets/bb03aa36-861a-4fec-8883-3b8f9c6a0f9b" /><img width="1545" height="2000" alt="2" src="https://github.com/user-attachments/assets/d76cfd59-091c-4484-bb44-5523fd995d7d" />



# Architecture

![Architecture](docs/architecture.png)

# Schema.png

![Schema](docs/Schema.png)

