# Customer Experience Analytics for Fintech Apps

A modular and robust pipeline for analyzing customer experience and satisfaction with fintech mobile apps, focusing on Ethiopian banks: Commercial Bank of Ethiopia (CBE), Bank of Abyssinia (BOA), and Dashen Bank.

## Key Features
- Automated scraping of Google Play Store reviews
- Comprehensive data cleaning and preprocessing
- **Rating-based sentiment mapping** for robust sentiment analysis
- Extraction of key drivers and pain points using NLP
- Modular, maintainable codebase (analysis, recommendations, visualization, ethics)
- Insightful visualizations and actionable recommendations
- Professional reporting and export capabilities

## Project Structure
- `data/` — Raw and processed datasets
- `notebooks/` — Jupyter notebooks for analysis and reporting
- `src/` — Modular Python source code:
  - `analysis/` — Insights, sentiment, visualization, ethics modules
  - `recommendations/` — Automated improvement suggestions
- `reports/` — Generated reports and figures
- `tests/` — Unit tests

## Analysis Pipeline

### 1. Data Collection
- Reviews are scraped from the Google Play Store using the `google-play-scraper` Python package for each bank's official app.
- Each review includes: review text, rating, date, bank name, and source.

### 2. Data Cleaning & Preprocessing
- **Deduplication:** Remove duplicate reviews per bank.
- **Missing Data Handling:** Drop rows with missing review text, rating, or date.
- **Date Normalization:** Convert all dates to ISO format (`YYYY-MM-DD`).
- **Column Standardization:** Ensure columns: `review`, `rating`, `date`, `bank`, `source`.

### 3. Sentiment Mapping
- **Robust Sentiment Assignment:**
  - Reviews are assigned sentiment labels based on their star rating to mitigate issues from typos, sarcasm, or ambiguous review text.
  - Mapping logic:
    - Ratings **4 or 5** → `positive`
    - Ratings **1 or 2** → `negative`
    - Rating **3** → `neutral`
  - This sentiment is stored in the `derived_sentiment` column and used for all downstream analysis.

### 4. Modular Analysis & Visualization
- **Insights Extraction:** Identify top drivers (positive keywords) and pain points (negative keywords) for each bank using NLP.
- **Visualization:**
  - Sentiment trends over time
  - Rating distributions per bank
  - Word clouds for review themes
- **Recommendations:** Generate actionable suggestions for app improvement based on pain points and drivers.
- **Ethics:** Assess and note potential biases in review data.

### 5. Reporting
- All analysis and visualizations are integrated into professional, reproducible Jupyter notebooks and exported reports.

## Usage

### Setup
Install dependencies:
```bash
pip install -r requirements.txt
```

### Example Workflow
```python
import pandas as pd
from analysis.insights import extract_drivers_painpoints

def map_rating_to_sentiment(rating):
    if rating >= 4:
        return 'positive'
    elif rating <= 2:
        return 'negative'
    else:
        return 'neutral'

df = pd.read_csv('data/reviews_with_sentiment.csv')
df['derived_sentiment'] = df['rating'].apply(map_rating_to_sentiment)
insights = extract_drivers_painpoints(df, sentiment_col='derived_sentiment')
print(insights)
```

## Professional Practices
- Modular, reusable codebase for easy maintenance and extension
- Clear separation of analysis, visualization, and recommendations
- Ethical considerations and bias assessment included

## License
This project is licensed under the MIT License.

- **Column Standardization:** The cleaned dataset contains the following columns: `review`, `rating`, `date`, `bank`, `source`.

### 3. Data Export
- The cleaned data is saved as a CSV file in the `data/` directory for further analysis and reporting.

## Setup
Install dependencies:
```
pip install -r requirements.txt
```

