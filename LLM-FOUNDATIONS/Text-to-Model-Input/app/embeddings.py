import numpy as np


class EmbeddingLayer:

    def __init__(self, vocab_size: int, embedding_dim: int):
        self.embedding_matrix = np.random.randn(
            vocab_size,
            embedding_dim
        )

    def lookup(self, token_ids):
        return self.embedding_matrix[token_ids]