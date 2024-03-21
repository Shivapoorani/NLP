import numpy as np
import warnings
from collections import defaultdict
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

class NaiveBayes:
    def __init__(self):
        self.prior = defaultdict(float)
        self.cond_prob = defaultdict(lambda: defaultdict(float))

    def fit(self, X, y):
        for c in np.unique(y):
            X_c = ' '.join(X[y == c])
            self.prior[c] = np.sum(y == c) / len(y)
            for word in X_c.split():
                self.cond_prob[c][word] += 1
            self.cond_prob[c].update({word: (self.cond_prob[c][word] + 1) / (len(X_c.split()) + len(set(X_c.split()))) for word in self.cond_prob[c]})

    def predict(self, X):
        epsilon = 1e-10
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            predictions = []
            for x in X:
                class_probs = {c: np.log(self.prior[c]) + sum(np.log(self.cond_prob[c].get(word, epsilon)) for word in x.split()) for c in self.prior}
                predicted_class = max(class_probs, key=class_probs.get)
                predictions.append(predicted_class)
        return predictions
if __name__ == "__main__":
    X = ["Hey, free coupons for you!", "Check out our latest products", "Free offer for you!", "Limited time offer: get 50% off"]
    y = ["spam", "ham", "spam", "ham"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    nb_model = NaiveBayes()
    nb_model.fit(X_train, y_train)
    predictions = nb_model.predict(X_test)
    accuracy = np.mean(predictions == y_test)
    print("Accuracy:", accuracy)
