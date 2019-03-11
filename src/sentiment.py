import nltk
import pandas as pd
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

nltk.download('stopwords')
pd.set_option('display.max_colwidth', 5500)


'''
    I wrote this in CollabLab / Jupyter and then copied it here...So 
    it may look funny all being in the init method
'''
class SentimentAnalyzer():

    def __init__(self):
        # Read from file or for online use I made a HTTP req
        txt = "https://raw.githubusercontent.com/wriazati/sentiment-analyzer/0251a64dffbb1cd9d9022c6cc016b10b863bd2c5/data/amazon_cells_labelled.txt"
        df = pd.read_csv(txt, sep="\t", header=None)
        df.columns = ['text', 'yval']

        # Create Vectorizer to convert plain text
        vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, max_features=20, stop_words='english')
        corpus = df.text

        # Define X and y
        X = vectorizer.fit_transform(corpus)
        y = df.yval

        # Optionally display topics
        lda = LatentDirichletAllocation()
        lda.fit(X)
        def display_topics(model, feature_names, no_top_words):
            for topic_idx, topic in enumerate(model.components_):
                print("Topic %d:" % (topic_idx))
                print(" ".join([feature_names[i]
                                for i in topic.argsort()[:-no_top_words - 1:-1]]))
        #display_topics(lda, vectorizer.get_feature_names(), 10)


        X_train, X_test, y_train, y_test = train_test_split(X, y)
        clf = SVC()
        clf.fit(X_train, y_train).score(X_test, y_test)

        self.vec = vectorizer
        self.clf = clf

    def predict(self, s):
        return self.clf.predict(self.vec.transform([s]))