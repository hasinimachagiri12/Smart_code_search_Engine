from sentence_transformers import SentenceTransformer
import numpy as np

class CodeEmbedder:
    """
    Handles the generation of vector embeddings for code snippets 
    and natural language queries using a pre-trained Transformer model.
    """
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        # all-MiniLM-L6-v2 is a high-speed, industry-standard model 
        # that balances performance with low latency.
        print("Initializing Gen AI Embedding Model...")
        self.model = SentenceTransformer(model_name)

    def get_embeddings(self, text_list):
        """
        Converts a list of strings (code or queries) into a 
        NumPy array of embeddings.
        """
        if isinstance(text_list, str):
            text_list = [text_list]
            
        # The model encodes text into a 384-dimensional vector space
        embeddings = self.model.encode(text_list, show_progress_bar=False)
        return embeddings

    def calculate_similarity(self, vector_a, vector_b):
        """
        Computes the Cosine Similarity between two vectors.
        Higher values (closer to 1.0) indicate higher semantic similarity.
        """
        # Reshape to 2D arrays as required by scikit-learn or numpy logic
        a = vector_a.reshape(1, -1)
        b = vector_b.reshape(1, -1)
        
        # Manual Cosine Similarity: (A dot B) / (||A|| * ||B||)
        dot_product = np.dot(a, b.T)
        norm_a = np.linalg.norm(a)
        norm_b = np.linalg.norm(b)
        
        return dot_product / (norm_a * norm_b)

# Testing the module
if __name__ == "__main__":
    embedder = CodeEmbedder()
    
    snippet_1 = "def sort_list(items): return sorted(items)"
    snippet_2 = "import random; x = random.randint(0, 10)"
    
    vec1 = embedder.get_embeddings(snippet_1)
    vec2 = embedder.get_embeddings(snippet_2)
    
    print(f"Vector Dimensions: {vec1.shape}")
    print(f"Similarity Score: {embedder.calculate_similarity(vec1, vec2)}")