import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class VectorSearch:
    def __init__(self):
        self.code_database = [] # Stores snippets
        self.vectors = []        # Stores embeddings

    def add_to_index(self, snippet, vector):
        self.code_database.append(snippet)
        self.vectors.append(vector)

    def find_best_match(self, query_vector):
        # Using Cosine Similarity to find the closest code snippet
        similarities = cosine_similarity([query_vector], self.vectors)
        best_index = np.argmax(similarities)
        return self.code_database[best_index]