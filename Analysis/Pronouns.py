import nltk
from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd

class Pronouns(BaseEstimator, TransformerMixin):

    def fit(self, X, y):
        return self

    def count_pronouns(self, comment):
        comment = comment.lower()
        tokens = nltk.word_tokenize(comment)

        pos_tags = [i[1] for i in nltk.pos_tag(tokens)]
        count = 0
        pronouns = ['PRP', 'PRP$', 'WP', 'WP$']
        for pos in pos_tags:
            if pos in pronouns:
                count += 1

        return count / len(tokens)

    def transform(self, X):
        return pd.Series(X).apply(self.count_pronouns)