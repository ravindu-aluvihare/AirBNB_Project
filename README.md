# Airbnb Data Engineering Pipeline

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


