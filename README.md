# 📊 PhonePe Transaction Insights

## Overview
PhonePe Transaction Insights is a data engineering and analytics project built on the PhonePe Pulse dataset. It ingests the published JSON data, loads it into a MySQL schema, and powers analysis queries and a Streamlit dashboard to explore transactions, users, devices, and insurance activity across India.

## Key Features
- **ETL pipeline** that parses PhonePe Pulse JSON files and populates MySQL tables.
- **SQL-driven analysis** that answers business questions around transactions, user growth, and insurance adoption.
- **Interactive Streamlit dashboard** for filtering by state, year, quarter, and device brand.
- **Reusable query library** for analytics and visualization notebooks.

## Project Architecture
1. **Source data**: PhonePe Pulse JSON files under `pulse/data/...`.
2. **ETL**: `main.py` reads JSON files, validates fields, and inserts rows into MySQL.
3. **Storage**: `db_init.sql` defines the relational schema.
4. **Analytics**:
   - `queries.py` defines SQL queries.
   - `fetch_analysis.py` and `connect_fetch_analysis.ipynb` run analyses.
5. **Visualization**: `dashboard.py` provides the Streamlit dashboard.

## Repository Structure
- `main.py` — ETL loader that ingests Pulse JSON and writes to MySQL.
- `db_init.sql` — Database schema for all PhonePe Pulse tables.
- `queries.py` — SQL query catalog used across analyses and dashboard.
- `fetch_analysis.py` — Python script for chart-based analysis.
- `connect_fetch_analysis.ipynb` — Notebook with exploratory analysis.
- `dashboard.py` — Streamlit dashboard implementation.
- `pulse/` — PhonePe Pulse data directory (JSON files).

## Prerequisites
- **Python 3.9+**
- **MySQL 8+**
- Python dependencies:
  - `mysql-connector-python`
  - `pandas`
  - `seaborn`
  - `matplotlib`
  - `streamlit`
  - `python-dotenv`

## Environment Configuration
Create a `.env` file in the project root and provide your MySQL credentials:

```env
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=phonepe_data
```

> ✅ Tip: Ensure `.env` is listed in `.gitignore` and never committed.

## Database Setup
Initialize the schema before running the ETL:

```bash
mysql -u <user> -p < db_init.sql
```This creates the `phonepe_data` database and required tables.
## Running the ETL
Load the PhonePe Pulse data into MySQL:

```bash
python main.py

```The ETL logs any skipped rows into `missing_*_log.txt` files for review.

## Running the Dashboard
Start the Streamlit dashboard:

```bash

streamlit run dashboard.py
```
```

The dashboard provides filters for:
- **State**
- **Year**
- **Quarter**
- **Device Brand**

## Analytics & Case Studies
Use `queries.py` with `fetch_analysis.py` or the notebook to explore:
- Transaction volume by state, year, and quarter
- Device brand dominance across regions
- District-level transaction and app open trends
- Insurance adoption and growth signals
- User growth over time

## Troubleshooting
- **Empty dashboards or charts**: Verify your `.env` values and confirm MySQL is running.
- **Missing data**: Ensure the `pulse/` directory contains the PhonePe Pulse JSON files.
- **ETL errors**: Check `missing_*_log.txt` files to review skipped records.

## Conclusion
PhonePe Transaction Insights turns raw Pulse data into actionable insights by combining a structured ETL pipeline, a relational data model, and interactive visual analytics. It provides a solid foundation for further exploration—whether you want to add more business questions, enhance visualizations, or deploy the dashboard for wider use.
## Database Setup
Initialize the schema before running the ETL:
