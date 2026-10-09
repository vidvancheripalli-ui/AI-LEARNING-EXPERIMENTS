# Design Decisions

This document records the important technical decisions made while
building Text-to-Model-Input and the reasoning behind them.

The goal is not to record every implementation detail, but to preserve
decisions that are useful for understanding, debugging, and explaining
the project later.

---

## DEC-001 — Use `tiktoken` for Tokenization

### Context

The project needs a real tokenizer so that the transformation from
text to token IDs can be understood using an actual tokenization system.

### Decision

Use `tiktoken`.

### Alternatives

- Build a custom tokenizer
- Hugging Face tokenizers
- A model-specific tokenizer implementation

### Reason

`tiktoken` provides a real BPE-based tokenizer while keeping the
implementation simple enough to inspect and understand.

The project is educational, so using a real tokenizer is more useful
than creating a simplified fake tokenizer.

### Trade-off

`tiktoken` is not representative of every tokenizer architecture used
by modern language models.

### Status

Accepted.

---

## DEC-002 — Use GPT-2 Encoding

### Context

`tiktoken` supports different encodings. The project needs a concrete
encoding to demonstrate tokenization and vocabulary lookup.

### Decision

Use the GPT-2 encoding.

### Reason

It provides a practical, deterministic tokenizer that can be used
locally without depending on a hosted model API.

The goal is to understand the tokenization mechanism, not to reproduce
the tokenizer of a specific production LLM.

### Trade-off

The tokenization behavior is specific to this encoding and should not
be assumed to represent every modern LLM tokenizer.

### Status

Accepted.

---

## DEC-003 — Use NumPy for the Embedding Layer

### Context

The project needs to demonstrate how token IDs become embedding
vectors.

### Decision

Implement the embedding matrix using NumPy.

### Reason

The core operation becomes explicit:

```text
token ID
   ↓
embedding matrix row
   ↓
embedding vector
```

Using NumPy avoids introducing a deep-learning framework before it is
necessary.

### Alternatives

- PyTorch
- TensorFlow

### Trade-off

This is an educational embedding implementation, not a trainable
production embedding system.

### Status

Accepted.

---

## DEC-004 — Use Randomly Initialized Embeddings

### Context

The project needs embedding vectors but is not intended to train an
embedding model.

### Decision

Initialize the embedding matrix with random values.

### Reason

The learning objective is to understand embedding lookup and tensor
shape, not semantic representation learning.

A real model would learn meaningful embedding values during training.

### Trade-off

The resulting vectors have no meaningful semantic relationships.

### Status

Accepted.

---

## DEC-005 — Use Learnable Positional Embeddings

### Context

Token embeddings alone do not explicitly represent where a token occurs
in a sequence.

### Decision

Use a positional embedding matrix and add positional vectors to token
embeddings.

### Reason

This directly demonstrates the idea that each sequence position can
have its own learned representation.

The implementation also prepares the conceptual foundation for
understanding Transformer inputs.

### Alternatives

- Sinusoidal positional encoding
- Relative positional representations
- Rotary positional embeddings (RoPE)

### Trade-off

This is not the only or necessarily the most modern positional
representation.

It is chosen because it is simple and intuitive for this foundational
project.

### Status

Accepted.

---

## DEC-006 — Pad Token IDs Before Embedding

### Context

Input sequences may have different lengths and need to be aligned
before being processed as a batch.

### Decision

Perform padding and attention-mask creation on token IDs before
embedding lookup.

### Correct Pipeline

```text
Text
 ↓
Token IDs
 ↓
Padding + Attention Mask
 ↓
Embedding Lookup
 ↓
Positional Information
```

### Reason

Padding is fundamentally a sequence-level operation on token IDs.

The attention mask can then directly identify which positions contain
real tokens and which contain padding.

### Important Lesson

Padding embedding vectors instead would mix sequence preparation with
the representation stage and is not the intended pipeline.

### Status

Accepted.

---

## DEC-007 — Expose the Pipeline Through FastAPI

### Context

The project should demonstrate not only the internal AI pipeline but
also how an AI capability can be exposed as a backend service.

### Decision

Use FastAPI.

### Reason

FastAPI provides:

- Simple API development
- Pydantic request validation
- Automatic API documentation
- Python-native AI integration
- A reusable backend skill for future projects

### Alternatives

- Flask
- Django
- Node.js / Express

### Trade-off

The API layer adds some code that is not necessary for understanding
tokenization itself, but it provides useful backend engineering practice.

### Status

Accepted.

---

## DEC-008 — Stop Before Implementing the Transformer

### Context

This project is the first project in the LLM foundations sequence.

### Decision

Stop the implementation after producing the final model input.

Do not implement:

- Self-attention
- Q/K/V
- Multi-head attention
- Transformer blocks
- Language-model training
- Text generation

### Reason

The purpose of this project is to establish the representation pipeline
before moving into Transformer internals.

The next project will build directly on this foundation.

### Status

Accepted.
