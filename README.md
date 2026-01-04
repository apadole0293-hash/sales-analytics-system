# Sales Analytics System

## 📌 Project Overview
The Sales Analytics System is a Python-based application designed to process, clean, analyze, and enrich sales transaction data.  
It reads raw sales data from a text file, validates and filters incorrect records, performs analytical calculations, enriches data using an external API, and generates a comprehensive sales report.

This project is built as part of a graded assignment and follows modular programming principles.

---

## 🗂️ Project Structure

sales-analytics-system
│
├── main.py
├── README.md
│
├── utils/
│ ├── init.py
│ ├── file_handler.py
│ ├── data_processor.py
│ ├── validator.py
│ ├── api_handler.py
│ └── report_generator.py
│
├── data/
│ └── sales_data.txt
│
└── output/
└── sales_report.txt



---

## ⚙️ Features Implemented

### 1. File Handling & Preprocessing
- Reads sales data from a pipe (`|`) separated text file
- Handles multiple file encodings safely
- Removes invalid or malformed rows
- Converts numeric fields into correct data types

### 2. Data Validation & Filtering
- Validates Transaction IDs and Customer IDs
- Filters records based on quantity, price, region, and sales amount
- Generates a validation summary

### 3. Data Processing & Analysis
- Calculates total revenue
- Performs region-wise sales analysis
- Identifies top-selling products
- Analyzes customer purchase behavior

### 4. API Integration
- Fetches product data from an external API
- Enriches sales records with product category, brand, and rating
- Handles API failures gracefully

### 5. Report Generation
- Generates a detailed sales report in text format
- Uses UTF-8 encoding to support special characters
- Saves output in the `output/` directory

---

## ▶️ How to Run the Project

### Prerequisites
- Python 3.10 or higher
- `requests` library

### Install Dependency
```bash
pip install requests


Run the Application
python main.py

output
output/sales_report.txt
