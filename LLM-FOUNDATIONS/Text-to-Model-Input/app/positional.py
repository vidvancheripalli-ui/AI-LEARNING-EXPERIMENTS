import numpy as np


class PositionalEmbedding:
    def __init__(self, max_sequence_length: int, embedding_dim: int):
        self.position_matrix = np.random.randn(
            max_sequence_length,
            embedding_dim
        )

    def add_position(self, token_embeddings):
        sequence_length = token_embeddings.shape[0]

        position_embeddings = self.position_matrix[:sequence_length]

        return token_embeddings + position_embeddings