from sklearn.feature_extraction.text import TfidfVectorizer
import fasttext
import fasttext.util
import tensorflow_hub as hub
import pandas as pd

from laserembeddings import Laser
from sentence_transformers import SentenceTransformer


class FastText:
    def __init__(self):
        self.initialized = False

    def initialize(self):

        if self.initialized:
            return

        fasttext.util.download_model('en', if_exists='ignore')  # English
        self.ft = fasttext.load_model('cc.en.300.bin')

        self.initialized = True

    def get_sentence_vec(self, sentences):

        self.initialize()

        sentence_vectors = [self.ft.get_sentence_vector(x) for x in sentences]

        return sentence_vectors


class LaserModel:

    def get_sentence_vec(self, sentences):

        laser = Laser()
        sentence_embeddings = laser.embed_sentences(sentences, lang='en')

        return sentence_embeddings


class SentenceBert:
    def __init__(self):
        self.initialized = False

    def initialize(self):

        if self.initialized:
            return

        self.model = SentenceTransformer('bert-large-nli-stsb-mean-tokens')

        self.initialized = True

    def get_sentence_vec(self, sentences):

        self.initialize()

        sentence_embeddings = self.model.encode(sentences)

        return sentence_embeddings


class Tfidf:

    def __init__(self):
        self.initialized = False

    def initialize(self):

        if self.initialized:
            return

        train_df = pd.pandas.read_table(
            '../sts_similarities/stsbenchmark/sts-train.csv',
            error_bad_lines=False,
            skip_blank_lines=True,
            usecols=[5, 6],
            names=["s1", "s2"])

        train_sentences = []

        for row in train_df.itertuples(index=False):
            train_sentences.extend((str(row[0]), str(row[1])))

        self.vectorizer = TfidfVectorizer()
        self.vectorizer.fit(train_sentences)

        self.initialized = True

    def get_sentence_vec(self, sentences):

        self.initialize()

        sentence_vectors = self.vectorizer.transform(
            sentences).toarray().tolist()

        return sentence_vectors


class Use:
    def __init__(self):
        self.initialized = False

    def initialize(self):

        if self.initialized:
            return

        module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
        self.model = hub.load(module_url)

        self.initialized = True

    def get_sentence_vec(self, sentences):

        self.initialize()

        sentence_embeddings = self.model(sentences)

        return sentence_embeddings
