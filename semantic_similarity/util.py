from sklearn.feature_extraction.text import TfidfVectorizer
import fasttext
import fasttext.util
import tensorflow as tf
import tensorflow_hub as hub

from laserembeddings import Laser
from sentence_transformers import SentenceTransformer
from scipy.spatial import distance


def tfidf_vectorizer(sentences):
    vectorizer = TfidfVectorizer()
    sentence_vectors = vectorizer.fit_transform(sentences).toarray().tolist()

    return sentence_vectors


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
