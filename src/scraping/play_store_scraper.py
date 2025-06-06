import pandas as pd
from google_play_scraper import Sort, reviews
from datetime import datetime
from pathlib import Path

BANK_APPS = [
    {"name": "Commercial Bank of Ethiopia", "app_id": "com.combanketh.mobilebanking"},
    {"name": "Bank of Abyssinia", "app_id": "com.boa.boaMobileBanking"},
    {"name": "Dashen Bank", "app_id": "com.dashen.dashensuperapp"}
]

REVIEWS_PER_BANK = 400
OUTPUT_FILE = Path(__file__).parent.parent.parent / "data" / "clean_reviews.csv"


def fetch_reviews(app_id, bank_name, count):
    all_reviews = []
    result, _ = reviews(app_id, lang='en', country='us', sort=Sort.NEWEST, count=count)
    if not result:
        print(f"Warning: No reviews found for {bank_name} ({app_id})")
    for r in result:
        all_reviews.append({
            "review": r.get("content", ""),
            "rating": r.get("score"),
            "date": r.get("at"),
            "bank": bank_name,
            "source": "Google Play"
        })
    return all_reviews



def preprocess(df):
    df = df.drop_duplicates(subset=["review", "bank"]).dropna(subset=["review", "rating", "date"])
    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")
    return df


def main():
    all_data = []
    for bank in BANK_APPS:
        all_data.extend(fetch_reviews(bank["app_id"], bank["name"], REVIEWS_PER_BANK))
    df = pd.DataFrame(all_data)
    df = preprocess(df)
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"Saved {len(df)} clean reviews to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
