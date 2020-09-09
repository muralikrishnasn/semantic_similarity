import seaborn as sns
import numpy as np

from scipy.spatial import distance


def cosine_similarity(first, second):
    similarity = 1 - distance.cosine(first, second)

    return similarity


def plot_similarity(labels_y, labels_x, features_y, features_x):
    corr = np.inner(features_y, features_x)
    corr_norm = corr / np.linalg.norm(corr)
    sns.set(font_scale=1.2)
    g = sns.heatmap(
        corr_norm,
        xticklabels=labels_x,
        yticklabels=labels_y,
        vmin=0,
        vmax=1,
        cmap="YlOrRd")
    g.set_xticklabels(labels_x, rotation=90)
    g.set_yticklabels(labels_y, rotation=0)
