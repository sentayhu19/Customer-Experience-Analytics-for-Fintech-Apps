# Customer Experience Analytics for Fintech Apps

This project analyzes customer satisfaction with mobile banking apps by collecting and processing user reviews from the Google Play Store for three Ethiopian banks: Commercial Bank of Ethiopia (CBE), Bank of Abyssinia (BOA), and Dashen Bank.

## Features
- Scrape Google Play Store reviews
- Sentiment and theme analysis
- Store cleaned data in Oracle DB
- Visualize insights and generate reports

## Structure
- `data/` - Raw and processed datasets
- `notebooks/` - Jupyter notebooks for analysis
- `src/` - Source code (scraping, processing, db, visualization)
- `reports/` - Generated reports and figures
- `tests/` - Unit tests

## Methodology

### 1. Data Collection
- Reviews are scraped from the Google Play Store for each bank's official mobile app using the `google-play-scraper` Python package.
- For each bank, a configurable number of the most recent reviews are fetched, including review text, rating, date, bank name, and source.

### 2. Data Cleaning & Preprocessing
- **Deduplication:** Duplicate reviews for the same bank are removed to ensure unique feedback is analyzed.
- **Missing Data Handling:** Rows with missing review text, rating, or date are dropped to maintain data quality.
- **Date Normalization:** All review dates are converted to the ISO format `YYYY-MM-DD` for consistency.
- **Column Standardization:** The cleaned dataset contains the following columns: `review`, `rating`, `date`, `bank`, `source`.

### 3. Data Export
- The cleaned data is saved as a CSV file in the `data/` directory for further analysis and reporting.

## Setup
Install dependencies:
```
pip install -r requirements.txt
```

