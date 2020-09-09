from scipy.spatial import distance


def cosine_similarity(first, second):
    similarity = 1 - distance.cosine(first, second)

    return similarity
