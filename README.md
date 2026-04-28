Smart Code Search AI 
A high-performance search engine that bridges the gap between Generative AI and Classical Data Structures. This tool allows developers to find code snippets within a repository using natural language "intent" rather than just exact keyword matching.🛠️ Tech StackLanguage: Python 3.8+AI/ML: Sentence-Transformers (BERT-based embeddings), Scikit-LearnData Structures: Trie (Prefix Tree), HashMapsComputation: NumPy (Vectorized operations)💡 Key Features & Architecture1. Semantic Search (Gen AI)Unlike traditional grep or keyword searches, this engine uses Sentence-Transformers (all-MiniLM-L6-v2) to convert code snippets into 384-dimensional vectors.Benefit: It understands that a query for "sorting an array" should return a quick_sort or bubble_sort implementation, even if the word "sorting" isn't in the code.Logic: Uses Cosine Similarity to measure the mathematical distance between the user query and the code database.2. Fast Autocomplete (DSA)The project implements a Trie (Prefix Tree) to index all unique function names and keywords.Benefit: Provides $O(L)$ lookup time for real-time keyword suggestions as a user types.Complexity: Significantly more efficient than scanning a list of strings ($O(N \times L)$).📂 Project StructurePlaintextsmart-code-search-ai/
│
├── app.py             # Main entry point: Ties AI and DSA together
├── embeddings.py      # Logic for vector generation and similarity math
├── requirements.txt   # Project dependencies
└── README.md          # Documentation
Getting Started
1. Install DependenciesBashpip install -r requirements.txt
2. Run the DemoBashpython app.py
📈 Amazon SDE AlignmentThis project demonstrates key competencies required for the SDE role:Scalability: The use of vector embeddings and Tries shows an understanding of high-scale retrieval.Efficiency: Optimized vector math using NumPy and efficient data structures.Innovation: Applying Modern AI (Transformers) to solve a classic Software Engineering problem.requirements.txtTo make sure your code runs, create a file named requirements.txt and paste this in:Plaintextsentence-transformers
scikit-learn
numpy
Final Step for Success:Once you have these files on GitHub, your project is officially a Portfolio Piece. When you talk to the Amazon recruiter, mention that you used a Hybrid Search Approach—Trie for precision and Transformers for recall. This shows you don't just "use AI," but you know how to engineer it into a system.
