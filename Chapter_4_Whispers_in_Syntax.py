# Chapter 4: Whispers in the Syntax – How Bias Enters Code

import numpy as np
from numpy.linalg import norm

# Function to compute cosine similarity
def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (norm(vec1) * norm(vec2))

# Sample vectors (for demonstration)
man_vec = np.array([1, 0])
woman_vec = np.array([-1, 0])
programmer_vec = np.array([0, 1])

print("Similarity(man, programmer):", cosine_similarity(man_vec, programmer_vec))
print("Similarity(woman, programmer):", cosine_similarity(woman_vec, programmer_vec))

# Debiasing example (simple projection removal)
gender_direction = man_vec - woman_vec

def debias_vector(vector, gender_direction):
    projection = np.dot(vector, gender_direction) / np.dot(gender_direction, gender_direction)
    return vector - projection * gender_direction

debiased_vec = debias_vector(woman_vec, gender_direction)
print("Debiased Similarity(woman, programmer):", cosine_similarity(debiased_vec, programmer_vec))
