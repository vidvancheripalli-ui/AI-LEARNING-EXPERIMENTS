from fastapi import FastAPI

from app.tokenizer import Tokenizer
from app.embeddings import EmbeddingLayer
from app.positional import PositionalEmbedding
from app.input_processor import InputProcessor

from app.schemas import TextRequest


app = FastAPI(
    title="Text-to-Model-Input API",
    description="Transforms raw text into a numerical model representation.",
    version="1.0.0"
)


tokenizer = Tokenizer()

vocab_size = tokenizer.encoding.n_vocab
embedding_dim = 128

embedding_layer = EmbeddingLayer(
    vocab_size=vocab_size,
    embedding_dim=embedding_dim
)

positional_embedding = PositionalEmbedding(
    max_sequence_length=512,
    embedding_dim=embedding_dim
)

input_processor = InputProcessor(
    pad_token_id=0
)


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/tokenize")
def tokenize(request: TextRequest):
    tokens = tokenizer.tokenize(request.text)
    token_ids = tokenizer.encode(request.text)

    return {
        "text": request.text,
        "tokens": tokens,
        "token_ids": token_ids,
        "token_count": len(token_ids)
    }