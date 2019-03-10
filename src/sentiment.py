import os
import io
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.decomposition import NMF
from sklearn.svm import SVC
import requests
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

NUM_TOPICS = 20
pd.set_option('display.max_colwidth', 5500)

class SentimentAnalyzer():
    def __init__(self):

        txt = "https://raw.githubusercontent.com/wriazati/sentiment-analyzer/0251a64dffbb1cd9d9022c6cc016b10b863bd2c5/data/amazon_cells_labelled.txt"
        df = pd.read_csv(txt, sep="\t", header=None)
        df.columns = ['text','yval']

        #vectorizer = CountVectorizer()
        vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, max_features=20, stop_words='english')
        corpus = df.text
        X = vectorizer.fit_transform(corpus)
        y = df.yval

        lda = LatentDirichletAllocation()
        lda.fit(X)

        def display_topics(model, feature_names, no_top_words):
            for topic_idx, topic in enumerate(model.components_):
                print("Topic %d:" % (topic_idx))
                print(" ".join([feature_names[i]
                                for i in topic.argsort()[:-no_top_words - 1:-1]]))

        display_topics(lda, vectorizer.get_feature_names(), 10)


        X_train, X_test, y_train, y_test = train_test_split(X, y)
        clf = SVC()
        clf.fit(X_train, y_train).score(X_test, y_test)

        self.vec = vectorizer
        self.clf = clf
        #
        # s = "This product does not work. it sucks. it is bad"
        # s = "This product is amazing. i love it. it is great"
        # ex = vectorizer.transform([s])
        # clf.predict(ex)

    def predict(self, s):
        return self.clf.predict(self.vec.transform([s]))