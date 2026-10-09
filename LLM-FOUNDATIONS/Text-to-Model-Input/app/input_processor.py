import numpy as np


class InputProcessor:

    def __init__(self, pad_token_id: int):
        self.pad_token_id = pad_token_id

    def pad_sequences(self, sequences, max_length=None):
        if max_length is None:
            max_length = max(len(sequence) for sequence in sequences)

        padded = []
        masks = []

        for sequence in sequences:
            sequence = sequence[:max_length]

            padding_length = max_length - len(sequence)

            padded_sequence = sequence + (
                [self.pad_token_id] * padding_length
            )

            attention_mask = (
                [1] * len(sequence) +
                [0] * padding_length
            )

            padded.append(padded_sequence)
            masks.append(attention_mask)

        return np.array(padded), np.array(masks)