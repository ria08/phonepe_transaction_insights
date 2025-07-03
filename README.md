# 📊 PhonePe Pulse Data Analysis & Interactive Dashboard

This project is a complete data analysis and visualization pipeline built on top of the **PhonePe Pulse GitHub dataset**. It extracts, transforms, and loads (ETL) JSON data into a MySQL database, performs SQL-based business analysis, and presents interactive visual insights via a **Streamlit dashboard**.

---

## Project Overview

PhonePe, one of India’s leading digital payment platforms, has shared rich datasets that reveal user and transaction behavior across states, districts, devices, and categories. This project aims to explore that data and answer real-world business questions such as:

- Which states and quarters have the highest digital transactions?
- How do different device brands perform in terms of user engagement?
- Which districts drive the most transaction volume or app opens?
- What is the growth potential for PhonePe's insurance services?

---
## Technologies Used

- **Python** (Pandas, Seaborn, Matplotlib)
- **MySQL** for data storage and queries
- **SQLAlchemy / mysql-connector-python** for DB connectivity
- **Streamlit** for dashboard creation
- **Git & GitHub** for version control
- **PhonePe Pulse JSON data**


---

## Technologies Used

- **Python** (Pandas, Seaborn, Matplotlib)
- **MySQL** for data storage and queries
- **SQLAlchemy / mysql-connector-python** for DB connectivity
- **Streamlit** for dashboard creation
- **Git & GitHub** for version control
- **PhonePe Pulse JSON data**

---

## Business Case Studies Solved

1. **Decoding Transaction Dynamics**  
   → Understand patterns by state, quarter, and category.

2. **Device Dominance & User Engagement**  
   → Analyze engagement across mobile brands and regions.

3. **Insurance Growth & Penetration**  
   → Track insurance adoption and identify expansion zones.

4. **Transaction Trends for Market Expansion**  
   → Spot top and underperforming states/districts.

5. **User Engagement & Growth Strategy**  
   → Track registered users, app opens, and trends over time.

---

## Setup Instructions




```bash
git clone https://github.com/your-username/phonepe_transaction_insights.git
cd phone_transaction_insights

##Configure Environment Variables

Create a `.env` file in the project root with your MySQL credentials:

> Make sure `.env` is listed in `.gitignore` and never pushed to GitHub.

---

##Run ETL Script

This script extracts JSON data from the PhonePe Pulse GitHub structure and pushes it into MySQL tables.

```bash
python main.py

##Run Dashboard
streamlit run dashboard.py
