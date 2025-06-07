import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict

nlp = spacy.load("en_core_web_sm", disable=["ner", "parser"])
stopwords = nlp.Defaults.stop_words

def preprocess_texts(texts):
    def clean(text):
        doc = nlp(text.lower())
        return " ".join([t.lemma_ for t in doc if t.is_alpha and t.text not in stopwords])
    return [clean(t) for t in texts]

def extract_keywords(texts, ngram_range=(1,2), top_k=10):
    tfidf = TfidfVectorizer(ngram_range=ngram_range, stop_words=list(stopwords))
    X = tfidf.fit_transform(texts)
    features = tfidf.get_feature_names_out()
    scores = X.toarray().sum(axis=0)
    top_idx = scores.argsort()[::-1][:top_k]
    return [features[i] for i in top_idx]

def cluster_keywords(keywords):
    themes = defaultdict(list)
    theme_map = {
        "Account Access Issues": ["login", "access", "password", "account"],
        "Transaction Performance": ["transfer", "transaction", "delay", "fail", "slow"],
        "User Interface & Experience": ["ui", "interface", "design", "navigation", "crash"],
        "Customer Support": ["support", "help", "service", "response"],
        "Feature Requests": ["feature", "add", "request", "option"]
    }
    for kw in keywords:
        assigned = False
        for theme, keys in theme_map.items():
            if any(k in kw for k in keys):
                themes[theme].append(kw)
                assigned = True
                break
        if not assigned:
            themes["Other"].append(kw)
    return dict(themes)

def assign_themes(df, text_col="review"):
    texts = preprocess_texts(df[text_col])
    keywords = extract_keywords(texts, ngram_range=(1,2), top_k=20)
    theme_dict = cluster_keywords(keywords)
    return theme_dict
