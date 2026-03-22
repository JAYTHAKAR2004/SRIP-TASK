from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def get_vectorizer():
    return TfidfVectorizer(max_features=5000, ngram_range=(1,2))

def get_model():
    return LogisticRegression(max_iter=1000)