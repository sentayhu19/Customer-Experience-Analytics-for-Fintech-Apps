import pandas as pd
from collections import Counter
from typing import Tuple, List, Dict

def extract_drivers_painpoints(df: pd.DataFrame, sentiment_col: str = 'sentiment', text_col: str = 'review_text', bank_col: str = 'bank', keywords_col: str = 'keywords') -> Dict[str, Dict[str, List[str]]]:
    """
    Identify top drivers and pain points for each bank based on sentiment and keywords.
    Returns a dictionary: {bank: {'drivers': [...], 'painpoints': [...]}}
    """
    results = {}
    for bank in df[bank_col].unique():
        bank_df = df[df[bank_col] == bank]
        # Drivers: Top keywords/themes in positive reviews
        pos_keywords = bank_df[bank_df[sentiment_col] == 'positive'][keywords_col].sum()
        drivers = [kw for kw, _ in Counter(pos_keywords).most_common(3)]
        # Pain points: Top keywords/themes in negative reviews
        neg_keywords = bank_df[bank_df[sentiment_col] == 'negative'][keywords_col].sum()
        painpoints = [kw for kw, _ in Counter(neg_keywords).most_common(3)]
        results[bank] = {'drivers': drivers, 'painpoints': painpoints}
    return results

def compare_banks(df: pd.DataFrame, bank_col: str = 'bank', sentiment_col: str = 'sentiment') -> pd.DataFrame:
    """
    Compare banks by sentiment counts and return a summary DataFrame.
    """
    return df.groupby([bank_col, sentiment_col]).size().unstack(fill_value=0)
