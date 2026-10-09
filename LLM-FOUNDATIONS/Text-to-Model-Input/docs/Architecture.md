# Architecture

## 1. Overview

Text-to-Model-Input demonstrates the transformation of raw text into a
numerical representation suitable for a neural network.

The system follows this pipeline:

```text
Raw Text
   ↓
Tokenizer
   ↓
Token IDs
   ↓
Padding + Attention Mask
   ↓
Embedding Lookup
   ↓
Positional Information
   ↓
Final Model Input
```

The project exposes the pipeline through a FastAPI service.

---

## 2. High-Level Architecture

```text
                    Client
                      │
                      ▼
                ┌──────────┐
                │ FastAPI  │
                │  /API    │
                └────┬─────┘
                     │
                     ▼
                ┌──────────┐
                │Tokenizer │
                └────┬─────┘
                     │
                     ▼
                 Token IDs
                     │
                     ▼
          ┌─────────────────────┐
          │ Input Processor      │
          │ Padding + Masking    │
          └──────────┬──────────┘
                     │
             Padded Token IDs
                     │
                     ▼
          ┌─────────────────────┐
          │  Embedding Layer     │
          │  NumPy Matrix Lookup │
          └──────────┬──────────┘
                     │
              Token Embeddings
                     │
                     ▼
          ┌─────────────────────┐
          │ Positional Embedding │
          └──────────┬──────────┘
                     │
                     ▼
              Model Input
```

---

## 3. Components

### 3.1 FastAPI Application

**File:** `app/main.py`

Responsible for:

- Creating the FastAPI application
- Initializing the processing components
- Exposing API endpoints
- Coordinating the text-to-model-input pipeline

Endpoints:

```text
GET  /health
POST /tokenize
POST /model-input
```

---

### 3.2 Tokenizer

**File:** `app/tokenizer.py`

Responsible for converting text into token IDs and converting token IDs
back into text.

The project uses the GPT-2 encoding provided by `tiktoken`.

Main operations:

```text
Text → Token IDs
Token IDs → Text
Text → Human-readable tokens
```

The tokenizer is the first numerical representation of the input.

---

### 3.3 Input Processor

**File:** `app/input_processor.py`

Responsible for preparing token IDs for a fixed sequence length.

It performs:

- Padding
- Truncation
- Attention-mask creation

The output contains:

```text
Padded Token IDs
Attention Mask
```

The attention mask identifies real tokens and padding positions.

```text
1 → real token
0 → padding
```

---

### 3.4 Embedding Layer

**File:** `app/embeddings.py`

Responsible for converting token IDs into vectors.

The embedding matrix has the conceptual shape:

```text
vocabulary_size × embedding_dimension
```

For a token ID:

```text
token_id
   ↓
embedding_matrix[token_id]
   ↓
embedding vector
```

NumPy is used to make this lookup mechanism explicit.

---

### 3.5 Positional Embedding

**File:** `app/positional.py`

Responsible for adding positional information to token embeddings.

The project uses a learnable positional embedding matrix.

Conceptually:

```text
Token Embedding
      +
Position Embedding
      ↓
Final Representation
```

---

### 3.6 Schemas

**File:** `app/schemas.py`

Contains Pydantic request models used by the FastAPI API.

Currently the main request contains:

```text
text: str
```

---

## 4. End-to-End Data Flow

For a request such as:

```text
"Hello world"
```

the system performs:

```text
"Hello world"
      ↓
Tokenizer
      ↓
Token IDs
      ↓
Padding
      ↓
Attention Mask
      ↓
Embedding Lookup
      ↓
Token Embeddings
      ↓
Position Embeddings
      ↓
Addition
      ↓
Final Model Input
```

---

## 5. Important Ordering

The ordering of operations is intentional.

Correct:

```text
Text
 ↓
Tokenization
 ↓
Token IDs
 ↓
Padding + Mask
 ↓
Embedding
 ↓
Positional Information
```

Padding is performed on token IDs rather than embedding vectors.

This keeps sequence preparation separate from numerical vector
representation.

---

## 6. Scope

This project intentionally stops before implementing a Transformer.

It does not include:

- Self-attention
- Q/K/V
- Multi-head attention
- Feed-forward networks
- Transformer blocks
- Language-model training
- Next-token generation

Those concepts belong to the next projects in the journey.

---

## 7. Design Principle

The project prioritizes **understanding the underlying representation**
over production-scale model implementation.

The goal is to understand:

> How does human-readable text become the numerical input consumed by
> a neural network?

That understanding forms the foundation for the Transformer and LLM
projects that follow.
