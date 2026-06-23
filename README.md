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

### 4. Run tests

python -m pytest tests/

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
<img width="1340" height="575" alt="Screenshot 2026-06-23 165200" src="https://github.com/user-attachments/assets/d28cfbd9-c407-43b3-806d-4a89ca013959" />
<img width="982" height="442" alt="Screenshot 2026-06-23 165237" src="https://github.com/user-attachments/assets/0249db35-0d40-47e5-9f7b-906f17e621f5" />
<img width="958" height="481" alt="Screenshot 2026-06-23 165257" src="https://github.com/user-attachments/assets/b2184738-187e-4181-8459-04911af9ea5d" />



# Architecture

![Architecture](docs/architecture.png)

# Schema.png

![Schema](docs/Schema.png)

