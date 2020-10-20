import numpy as np
import pandas as pd
import nltk
from sklearn.base import BaseEstimator, TransformerMixin


class Length_Comments(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return pd.Series(X).apply(len)