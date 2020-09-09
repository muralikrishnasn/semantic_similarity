from sklearn.feature_extraction.text import TfidfVectorizer
import fasttext
import fasttext.util
import tensorflow_hub as hub

from laserembeddings import Laser
from sentence_transformers import SentenceTransformer
from scipy.spatial import distance
import pandas as pd


def fasttext_vectorizer(sentences):
    fasttext.util.download_model('en', if_exists='ignore')  # English
    ft = fasttext.load_model('cc.en.300.bin')
    sentence_vectors = [ft.get_sentence_vector(x) for x in sentences]

    return sentence_vectors


def laser_embeddings(sentences):
    laser = Laser()
    sentence_embeddings = laser.embed_sentences(sentences, lang='en')

    return sentence_embeddings


def bert_embeddings(sentences):
    model = SentenceTransformer('bert-large-nli-stsb-mean-tokens')
    sentence_embeddings = model.encode(sentences)

    return sentence_embeddings


def use_embeddings(sentences):
    module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
    model = hub.load(module_url)
    sentence_embeddings = model(sentences)

    return sentence_embeddings


def cosine_similarity(first, second):
    similarity = 1 - distance.cosine(first, second)

    return similarity


class TfidfModel:

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
