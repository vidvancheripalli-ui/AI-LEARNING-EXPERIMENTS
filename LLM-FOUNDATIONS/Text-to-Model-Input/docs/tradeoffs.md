# Trade-offs

This document records the important trade-offs accepted in
Text-to-Model-Input.

The project prioritizes **learning and clarity** over production
complexity.

---

## 1. `tiktoken` vs Custom Tokenizer

### Chosen

`tiktoken`

### Alternative

Build a tokenizer from scratch.

### Benefit

A real tokenizer makes the project closer to how actual LLM systems
process text.

### Cost

The internal implementation of the tokenizer itself is not built by us.

### Why this is acceptable

The learning objective is to understand tokenization, token IDs, and
their role in the model-input pipeline, not to implement BPE from
scratch.

---

## 2. `tiktoken` vs Hugging Face Tokenizers

### Chosen

`tiktoken`

### Alternative

Hugging Face tokenizers.

### Benefit

Simple API and easy local experimentation.

### Cost

Less exposure to the broader Hugging Face tokenizer ecosystem.

### Why this is acceptable

Hugging Face will become more relevant when working with actual
open-source models and fine-tuning later in the journey.

---

## 3. NumPy vs PyTorch for Embeddings

### Chosen

NumPy

### Alternative

PyTorch.

### Benefit

Makes embedding lookup extremely explicit and keeps the project focused
on the underlying operation.

### Cost

The implementation does not provide:

- Automatic differentiation
- GPU acceleration
- Model training
- Production deep-learning functionality

### Why this is acceptable

None of those capabilities are required for this project's learning
objective.

---

## 4. Random Embeddings vs Trained Embeddings

### Chosen

Random initialization.

### Alternative

Train embeddings or load pretrained embeddings.

### Benefit

Keeps the focus on the mechanics of embedding lookup.

### Cost

The resulting vectors do not contain useful semantic information.

### Why this is acceptable

Semantic representation learning is outside the scope of this project.

---

## 5. Learnable Positional Embeddings vs Sinusoidal Encoding

### Chosen

Learnable positional embeddings.

### Alternatives

- Sinusoidal positional encoding
- Relative positional representations
- Rotary positional embeddings

### Benefit

Very straightforward to understand:

```text
token embedding + position embedding
```

### Cost

It requires a predefined maximum sequence length and does not represent
the more modern positional techniques used by many current models.

### Why this is acceptable

The purpose here is to understand why positional information exists,
not to select the best positional method for a production LLM.

---

## 6. Padding Before Embedding vs Padding After Embedding

### Chosen

Padding token IDs before embedding.

### Alternative

Pad embedding vectors after lookup.

### Benefit

Keeps sequence preparation at the token-ID level and makes the
attention mask straightforward.

### Cost

The implementation must maintain a clear distinction between token
representation and vector representation.

### Why this is acceptable

This separation is conceptually cleaner and aligns with the intended
model-input pipeline.

---

## 7. FastAPI vs No API

### Chosen

FastAPI API.

### Alternative

A standalone Python script.

### Benefit

Provides practical backend experience and makes the project usable
through HTTP.

### Cost

Adds API and validation code that is not required for the core
tokenization/embedding demonstration.

### Why this is acceptable

FastAPI is a recurring backend skill throughout the AI Engineering
Journey, so the additional complexity has learning value.

---

## 8. Educational Implementation vs Production Implementation

### Chosen

Educational implementation.

### Alternative

Use production-grade model/tokenizer frameworks throughout.

### Benefit

The internal steps remain visible and understandable.

### Cost

The implementation is not optimized for:

- Large-scale inference
- GPU execution
- Training
- Distributed systems
- Production model serving

### Why this is acceptable

Production optimization is intentionally deferred to later projects.

---

## 9. Limited Project Scope vs Building a Full Transformer

### Chosen

Stop after producing the model input.

### Alternative

Continue directly into attention and Transformer implementation.

### Benefit

Creates a clean conceptual boundary:

```text
Project 1
Text → Model Input

Project 2
Model Input → Transformer Computation
```

### Cost

Some functionality is intentionally left for the next project.

### Why this is acceptable

Separating the projects makes the learning progression easier to
understand and debug.

---

# Overall Trade-off

The central trade-off of this project is:

```text
Production Complexity
        ↕
Learning Transparency
```

This project deliberately chooses **learning transparency**.

Later projects will progressively shift the balance toward:

```text
Learning
   ↓
Correctness
   ↓
Reliability
   ↓
Performance
   ↓
Scalability
   ↓
Production Readiness
```
