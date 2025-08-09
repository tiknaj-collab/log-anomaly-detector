from sklearn.ensemble import IsolationForest
from sklearn.feature_extraction.text import TfidfVectorizer

class LogAnomalyDetector:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.model = IsolationForest(contamination=0.1)

    def fit(self, logs):
        X = self.vectorizer.fit_transform(logs)
        self.model.fit(X)

    def predict(self, logs):
        X = self.vectorizer.transform(logs)
        return self.model.predict(X)  # -1 = anomaly, 1 = normal
