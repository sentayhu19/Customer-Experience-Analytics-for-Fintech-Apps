import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import pandas as pd
from typing import Optional

sns.set(style="whitegrid")

def plot_sentiment_trends(df: pd.DataFrame, date_col: str = 'date', sentiment_col: str = 'sentiment', bank_col: str = 'bank'):
    """
    Plot sentiment trends over time for each bank.
    """
    df[date_col] = pd.to_datetime(df[date_col])
    trend = df.groupby([bank_col, pd.Grouper(key=date_col, freq='M')])[sentiment_col].value_counts().unstack().fillna(0)
    for bank in df[bank_col].unique():
        trend.loc[bank].plot(kind='line', title=f'Sentiment Trend for {bank}')
        plt.xlabel('Month')
        plt.ylabel('Count')
        plt.legend(title='Sentiment')
        plt.show()

def plot_rating_distribution(df: pd.DataFrame, rating_col: str = 'rating', bank_col: str = 'bank'):
    """
    Plot rating distributions for each bank.
    """
    for bank in df[bank_col].unique():
        sns.histplot(df[df[bank_col] == bank][rating_col], bins=5, kde=True)
        plt.title(f'Rating Distribution for {bank}')
        plt.xlabel('Rating')
        plt.ylabel('Count')
        plt.show()

def plot_keyword_cloud(df: pd.DataFrame, text_col: str = 'review', bank: Optional[str] = None, bank_col: str = 'bank'):
    """
    Generate a word cloud from review text for all banks or a specific bank.
    """
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt

    if bank:
        texts = df[df[bank_col] == bank][text_col]
    else:
        texts = df[text_col]
    text = ' '.join(texts.astype(str))
    wc = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.title(f'Keyword Cloud {"for " + bank if bank else "(All Banks)"}')
    plt.show()
