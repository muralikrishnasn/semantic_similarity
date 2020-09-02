from sklearn.feature_extraction.text import TfidfVectorizer

import fasttext
import fasttext.util

from laserembeddings import Laser

from sentence_transformers import SentenceTransformer

import tensorflow as tf
import tensorflow_hub as hub

from scipy.spatial import distance


def tfidf(sentences):
    vectorizer = TfidfVectorizer()
    sentence_vectors = vectorizer.fit_transform(sentences).toarray().tolist()

    return sentence_vectors


def fasttext(sentences):
    sentence_vectors = [ft.get_sentence_vector(x) for x in sentences]

    return sentence_vectors


def laser(sentences):
    laser = Laser()
    sentence_embeddings = laser.embed_sentences(sentences, lang='en')

    return sentence_embeddings


def sentence_bert(sentences):
    model = SentenceTransformer('bert-large-nli-stsb-mean-tokens')
    sentence_embeddings = model.encode(sentences)
    return sentence_embeddings


def use(sentences):
    module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
    model = hub.load(module_url)
    sentence_embeddings = model(sentences)
    return sentence_embeddings


def cosine_similarity(first, second):
    return distance.cosine(first, second)
