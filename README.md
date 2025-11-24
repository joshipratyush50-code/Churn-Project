# Customer Churn Analysis – Telecom Dataset

## Executive Summary
This project analyzes 7,043 telecom customer records to uncover the key factors driving customer churn. Using Python, SQL, SQLite, and Tableau, it delivers a complete end-to-end workflow: data cleaning, SQL modeling, analytical database creation, and an interactive Tableau dashboard. The analysis identifies high-risk customer segments and outlines data-driven retention strategies with measurable financial impact.

## Dashboard Preview
![Dashboard Preview](dashboard_preview.png)

## Business Problem
Telecom companies face high acquisition costs and rising competition. Customer churn directly reduces Monthly Recurring Revenue (MRR), making retention a top priority.  
This project addresses three core questions:

1. Who is churning?
2. Why are they churning?
3. Which actions will reduce churn most effectively?

The analysis identifies customer behaviors, contract types, and payment methods most associated with attrition and quantifies the revenue at risk.

## Key Insights
(From Executive Summary)

- Month-to-month customers churn at **43%**, while two-year contract customers churn at **11%**.
- Customers using electronic checks churn at **48%**, versus ~16% for auto-pay customers.
- Churned customers pay **≈25% higher monthly charges**, indicating strong price sensitivity.
- A 10% reduction in churn among valuable month-to-month customers could preserve **~$1.2M in annual revenue**.

## Methodology

### 1. Data Preparation (Python)
- Cleaned missing and inconsistent values  
- Standardized categorical fields  
- Engineered tenure and churn indicators  
- Exported cleaned dataset to SQL and Tableau  

### 2. Database Modeling (SQLite)
- Built structured analytical database (`churn.db`)  
- Created tables for contract type, payment method, tenure, charges, and churn status  
- Performed SQL feature analysis  

### 3. Visualization (Tableau)
- Developed interactive dashboard with KPIs  
- Implemented filters for contract, payment method, internet service, gender, and tenure  
- Visualized churn by contract type, payment method, and monthly charges  

### 4. Reporting
- Compiled business implications and recommended actions  
- Quantified financial retention impact  
- Created executive-style summary (Executive Summary.docx)

## Tech Stack
- Python (pandas, numpy)
- SQL / SQLite
- Tableau
- Excel/CSV
- Documentation (Word, Markdown)

## Repository Structure
- churn_sql.py: Python + SQL pipeline for preprocessing
- churn.db: SQLite database with cleaned and modeled data
- dataset.csv: Raw dataset with 7,043 customer records
- Churn Dashboard.twb: Tableau dashboard
- Executive Summary.docx: Business insights and summary
- README.md: Project documentation


## Dashboard Features
- KPI cards for churn rate, total customers, and ARPU  
- Churn segmentation by contract type  
- Payment method analysis  
- Monthly charges comparison  
- Tenure-based filtering  
- Internet service and demographic segmentation  
- Fully interactive Tableau filters  

## How to Run the Project

### Step 1 — Generate the database
python churn_sql.py


### Step 2 — Explore the database
Open `churn.db` using:
- DB Browser for SQLite  
- VS Code SQL extensions  
- Python scripts  

### Step 3 — Launch the Tableau dashboard
1. Open `Churn Dashboard.twb` in Tableau Desktop  
2. Connect to `dataset.csv` or `churn.db`  
3. Use filters and KPIs to explore churn drivers  

## Skills Demonstrated
- Data Cleaning & Preprocessing  
- SQL Querying & Database Design  
- Exploratory Data Analysis (EDA)  
- Dashboard Design & Visualization (Tableau)  
- Business Intelligence Storytelling  
- Churn & Customer Analytics  
- KPI Development  

## Future Enhancements
- Predictive churn model (Logistic Regression, Random Forest)  
- Customer clustering (K-Means, Hierarchical)  
- Automated retention reporting  
- Real-time churn scoring with API pipelines  

## Project Purpose
This project demonstrates the ability to convert raw customer data into actionable insights that drive business decisions. It reflects practical skills in analytics, visualization, SQL modeling, and data-driven retention strategy—key capabilities for business analytics and data science roles.
