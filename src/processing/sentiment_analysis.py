import pandas as pd
from transformers import pipeline

sentiment_model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def compute_sentiment(texts):
    results = sentiment_model(list(texts))
    labels = [r['label'].lower() for r in results]
    scores = [r['score'] for r in results]
    return labels, scores

def add_sentiment(df, text_col="review"):
    labels, scores = compute_sentiment(df[text_col])
    df["sentiment_label"] = labels
    df["sentiment_score"] = scores
    return df

def aggregate_sentiment(df, by=["bank", "rating"]):
    return df.groupby(by)[["sentiment_score"]].mean().reset_index()
