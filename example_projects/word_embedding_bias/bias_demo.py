import numpy as np

# Dummy embeddings for demo (not real word vectors)
embeddings = {
    "man": np.array([1.0, 0.0]),
    "woman": np.array([-1.0, 0.0]),
    "programmer": np.array([0.5, 1.0]),
    "nurse": np.array([-0.5, 1.0])
}

def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

print("Similarity(man, programmer):", cosine_similarity(embeddings["man"], embeddings["programmer"]))
print("Similarity(woman, programmer):", cosine_similarity(embeddings["woman"], embeddings["programmer"]))

# Debiasing (simple)
gender_direction = embeddings["man"] - embeddings["woman"]
def debias_vector(vector, gender_direction):
    return vector - np.dot(vector, gender_direction) / np.dot(gender_direction, gender_direction) * gender_direction

debiased = {w: debias_vector(v, gender_direction) for w, v in embeddings.items()}
print("Debiased Similarity(woman, programmer):", cosine_similarity(debiased["woman"], debiased["programmer"]))
