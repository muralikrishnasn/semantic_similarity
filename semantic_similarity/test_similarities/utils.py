import seaborn as sns

from scipy.spatial import distance
from sklearn.metrics.pairwise import cosine_similarity


def similarity(first, second):
    sim = 1 - distance.cosine(first, second)

    return sim


def plot_similarity(labels_y, labels_x, features_y, features_x):
    corr = cosine_similarity(features_y, features_x)
    sns.set(font_scale=1.2)
    g = sns.heatmap(
        corr,
        xticklabels=labels_x,
        yticklabels=labels_y,
        vmin=0,
        vmax=1,
        cmap="YlOrRd")
    g.set_xticklabels(labels_x, rotation=90)
    g.set_yticklabels(labels_y, rotation=0)
