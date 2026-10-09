# Learning Notes

This document captures the important concepts learned while building
Text-to-Model-Input.

The focus is on understanding the concepts in my own words and
connecting them to the implementation.

---

# 1. Why Text Must Become Numbers

Neural networks operate on numerical representations rather than raw
human-readable text.

Therefore, an NLP pipeline must transform:

```text
Human Text
    ↓
Numerical Representation
```

This project focuses on the steps before a Transformer processes the
input.

---

# 2. Tokenization

Tokenization converts text into smaller units called tokens.

A token may represent:

- A word
- Part of a word
- Characters
- Punctuation
- Whitespace-related pieces

Modern language models commonly use subword tokenization.

Example:

```text
"unbelievable"
      ↓
["un", "believ", "able"]
```

The exact result depends on the tokenizer.

---

# 3. BPE and Subword Tokenization

Byte Pair Encoding (BPE) is a common approach for constructing a
subword vocabulary.

The basic idea is to represent frequent patterns as reusable tokens.

This provides a balance between:

```text
Character-level representation
        ↕
Word-level representation
```

Benefits include:

- Reasonable vocabulary size
- Ability to represent uncommon words
- Reuse of common subword patterns
- Better handling of words not explicitly present as whole vocabulary
  entries

---

# 4. Vocabulary and Token IDs

A tokenizer maintains a vocabulary that maps tokens to integer IDs.

Conceptually:

```text
"hello" → 1234
"world" → 5678
```

The integer itself has no semantic meaning.

It is simply an index into the vocabulary and, later, into an embedding
matrix.

---

# 5. Embedding Lookup

An embedding matrix can be represented as:

```text
Vocabulary Size × Embedding Dimension
```

For example:

```text
50,000 × 128
```

If the token ID is `42`:

```text
embedding_matrix[42]
```

returns a vector of length `128`.

Therefore:

```text
Token ID
   ↓
Row Lookup
   ↓
Embedding Vector
```

The embedding operation in this project is intentionally implemented
with NumPy so that this lookup remains visible.

---

# 6. What an Embedding Represents

An embedding is a dense numerical representation of a token.

In a trained model, embeddings can encode useful relationships between
tokens.

For example, related words may occupy nearby regions of the learned
vector space.

However, the embeddings in this project are randomly initialized.

Therefore, they do **not** contain meaningful semantic relationships.

The purpose here is to understand the mechanism, not semantic
representation learning.

---

# 7. Why Position Is Needed

Consider:

```text
"The dog chased the cat."
```

and:

```text
"The cat chased the dog."
```

The same words can appear in different positions and produce different
meanings.

Therefore, a model needs information about token order.

Token embeddings tell us approximately:

> What token is this?

Positional information tells us:

> Where is this token in the sequence?

The project combines them:

```text
Token Embedding
      +
Position Embedding
      ↓
Position-aware Representation
```

---

# 8. Padding

Different sequences can have different lengths.

For batch processing, sequences are often aligned to a common length.

Example:

```text
[10, 20, 30]

[10, 20]
```

can become:

```text
[10, 20, 30]
[10, 20,  0]
```

The additional value is a padding token ID.

Padding is performed on token IDs in this project.

---

# 9. Attention Mask

Padding creates positions that do not represent real input.

An attention mask identifies which positions are meaningful.

Example:

```text
Token IDs:

[10, 20, 30, 0, 0]

Mask:

[ 1,  1,  1, 0, 0]
```

Conceptually:

```text
1 → real token
0 → padding
```

The mask becomes important when we implement attention in the next
project.

---

# 10. Sequence Length and Embedding Dimension

These two dimensions represent different things.

### Sequence Length

How many token positions are present.

Example:

```text
512 tokens
```

### Embedding Dimension

How many numerical values represent each token.

Example:

```text
128 values per token
```

Therefore, a sequence representation can have shape:

```text
512 × 128
```

This distinction is fundamental when working with Transformer tensors.

---

# 11. Token Count Matters

Tokenization is not only a preprocessing detail.

Token count affects:

- Context-window usage
- API cost
- Latency
- Memory
- RAG chunk sizes
- Maximum input length

Therefore, understanding tokenization becomes important later when
building real LLM applications.

---

# 12. Model Input Pipeline

The complete conceptual pipeline learned in this project is:

```text
Raw Text
   ↓
Tokenization
   ↓
Token IDs
   ↓
Padding + Attention Mask
   ↓
Embedding Lookup
   ↓
Positional Information
   ↓
Model Input
```

This is the foundation for the Transformer.

---

# 13. Important Implementation Lesson

One of the most important corrections during implementation was the
ordering of padding and embedding.

Incorrect conceptual approach:

```text
Text
 ↓
Embeddings
 ↓
Padding
```

Correct approach:

```text
Text
 ↓
Token IDs
 ↓
Padding + Mask
 ↓
Embeddings
```

This helped establish the distinction between:

```text
Sequence preparation
        vs
Numerical representation
```

---

# 14. What This Project Does Not Teach Yet

This project intentionally stops before the Transformer computation.

Topics still to learn:

- Query, Key, Value
- Self-attention
- Scaled dot-product attention
- Softmax attention weights
- Causal masking
- Multi-head attention
- Feed-forward networks
- Residual connections
- Layer normalization
- Transformer blocks
- Next-token prediction

These become the focus of the Mini Transformer project.

---

# 15. Key Takeaway

The most important mental model from this project is:

```text
Text
 ↓
Discrete Tokens
 ↓
Token IDs
 ↓
Dense Vectors
 ↓
Position-aware Vectors
 ↓
Transformer
```

The Transformer does not directly understand words or strings.

It operates on numerical representations produced by this pipeline.

That is the foundation on which the rest of the LLM journey is built.
