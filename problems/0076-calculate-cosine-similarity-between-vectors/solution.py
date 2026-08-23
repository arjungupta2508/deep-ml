import numpy as np

def cosine_similarity(v1, v2):
    dot_product = np.dot(v1, v2)

    mag_v1 = np.linalg.norm(v1)
    mag_v2 = np.linalg.norm(v2)

    return  dot_product / (mag_v1 * mag_v2)

    