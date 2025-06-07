import pandas as pd
import oracledb
import sys
from db_config import ORACLE_DB_CONFIG

def insert_banks(conn, banks):
    cursor = conn.cursor()
    bank_ids = {}
    for bank in banks:
        cursor.execute(
            "MERGE INTO banks b USING (SELECT :name AS name, :app_id AS app_id FROM dual) d ON (b.name=d.name) " +
            "WHEN NOT MATCHED THEN INSERT (name, app_id) VALUES (:name, :app_id) RETURNING id INTO :id",
            {"name": bank["name"], "app_id": bank["app_id"], "id": bank_ids.setdefault(bank["name"], None)}
        )
        cursor.execute("SELECT id FROM banks WHERE name=:name", {"name": bank["name"]})
        bank_ids[bank["name"]] = cursor.fetchone()[0]
    return bank_ids

def insert_reviews(conn, df, bank_ids):
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute(
            "INSERT INTO reviews (bank_id, review, rating, review_date, source, sentiment_label, sentiment_score) " +
            "VALUES (:bank_id, :review, :rating, TO_DATE(:review_date, 'YYYY-MM-DD'), :source, :sentiment_label, :sentiment_score)",
            {
                "bank_id": bank_ids[row["bank"]],
                "review": row["review"],
                "rating": row["rating"],
                "review_date": row["date"],
                "source": row["source"],
                "sentiment_label": row.get("sentiment_label", None),
                "sentiment_score": row.get("sentiment_score", None)
            }
        )
    conn.commit()

if __name__ == "__main__":
    csv_path = sys.argv[1] if len(sys.argv) > 1 else "data/reviews_with_sentiment.csv"
    df = pd.read_csv(csv_path)
    banks = [
        {"name": "Commercial Bank of Ethiopia", "app_id": "com.combanketh.mobilebanking"},
        {"name": "Bank of Abyssinia", "app_id": "com.boa.boaMobileBanking"},
        {"name": "Dashen Bank", "app_id": "com.dashen.dashensuperapp"}
    ]
    conn = oracledb.connect(**ORACLE_DB_CONFIG)
    bank_ids = insert_banks(conn, banks)
    insert_reviews(conn, df, bank_ids)
    print("Inserted reviews:", len(df))