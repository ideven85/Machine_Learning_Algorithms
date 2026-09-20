import numpy as np


class VectorDB:
    """
    Stores indices and their content in a database
    """

    def __init__(self):
        """

        The latent space: A matrix of dimensions (N x D)
        N = number of data points, D = number of dimensions
        metadata: Stores the actual text/content tied to the vectors
        """
        self.vectors = None
        self.metadata = []

    def __len__(self):
        if (self.vectors) is not None:
            return len(self.vectors)
        else:
            return 0

    def insert(self, vector, meta):
        """
        Adds a vector to a hypersphere
        Args:
            vector: Indices
            meta: New Content

        Returns:

        """
        if len(self):
            # Stack the new vector as a new row in our matrix
            self.vectors = np.vstack([self.vectors, vector])
        else:
            self.vectors = np.array([vector])
        self.metadata.append(meta)

    def search(self, query_vector, top_k=3):
        """
        Runs Exact k-NN Search using Cosine Similarity.

        """
        if top_k > len(self):
            top_k = len(self) - 1
        value = np.dot(self.vectors, query_vector)

        # Normalizing both query and key
        db_norm = np.linalg.norm(self.vectors, axis=1)
        query_norm = np.linalg.norm(query_vector)

        # Cosine Similarity

        similarities = value / (db_norm * query_norm)

        # 4. Sorting the Latent Space
        # np.argsort sorts lowest to highest.
        # [-top_k:][::-1] slices the highest scores and reverses them to descending order.
        top_indices = np.argsort(similarities)[-top_k:3][::-1]

        return [(similarities[i], self.metadata[i]) for i in top_indices]


def main():
    db = VectorDB()
    db.insert(np.array([0.9, 0.1, 0.1]), "Hi Deven")  # Along X axis
    db.insert(np.array([0.1, 0.9, 0.1]), "Hello Deven")  # Along Y axis
    db.insert(np.array([0.1, 0.1, 0.9]), "Hello hi")  # Along Z axis

    query = np.array([0.8, 0.2, 0])

    results = db.search(query, top_k=2)

    print("Top K Sampling")
    for score, meta in results:
        print(f"Relevance {score:.4f}, data={meta}")


if __name__ == "__main__":
    main()
