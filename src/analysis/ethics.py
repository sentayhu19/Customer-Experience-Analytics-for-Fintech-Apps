import pandas as pd

def note_biases(df: pd.DataFrame, sentiment_col: str = 'sentiment', rating_col: str = 'rating') -> str:
    """
    Identify and note potential review biases in the dataset.
    """
    n_reviews = len(df)
    n_neg = (df[sentiment_col] == 'negative').sum()
    n_pos = (df[sentiment_col] == 'positive').sum()
    neg_ratio = n_neg / n_reviews if n_reviews else 0
    pos_ratio = n_pos / n_reviews if n_reviews else 0
    bias_note = (
        f"Out of {n_reviews} reviews, {n_neg} are negative ({neg_ratio:.1%}), "
        f"{n_pos} are positive ({pos_ratio:.1%}). "
    )
    if neg_ratio > 0.6:
        bias_note += "There is a notable negative skew, which may indicate review bias (e.g., dissatisfied customers more likely to leave feedback).\n"
    if pos_ratio > 0.6:
        bias_note += "There is a notable positive skew, which may indicate review bias (e.g., incentivized or solicited positive reviews).\n"
    bias_note += "Consider these biases when interpreting insights and recommendations."
    return bias_note
