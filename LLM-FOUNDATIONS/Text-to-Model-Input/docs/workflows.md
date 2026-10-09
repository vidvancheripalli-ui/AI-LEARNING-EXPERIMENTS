# Workflows

This document describes the important workflows inside
Text-to-Model-Input.

The goal is to understand not only what each component does, but how
data moves through the complete system.

---

# 1. Tokenization Workflow

Endpoint:

```text
POST /tokenize
```

Flow:

```text
Client
  ↓
FastAPI
  ↓
Request Validation
  ↓
Tokenizer
  ↓
Token IDs
  ↓
Decode Individual IDs
  ↓
JSON Response
```

### Step-by-step

1. The client sends raw text.
2. FastAPI validates the request.
3. `Tokenizer.encode()` converts the text into token IDs.
4. Each token ID can be decoded individually to inspect the token piece.
5. The API returns the original text, tokens, token IDs and token count.

---

# 2. Complete Model-Input Workflow

Endpoint:

```text
POST /model-input
```

Flow:

```text
Client
  ↓
FastAPI
  ↓
Request Validation
  ↓
Tokenizer
  ↓
Token IDs
  ↓
Padding + Attention Mask
  ↓
Embedding Lookup
  ↓
Positional Embedding
  ↓
Final Model Input
  ↓
Response
```

---

## Step 1 — Receive Text

Example:

```text
"Hello world"
```

The text is received through the API request.

---

## Step 2 — Tokenize

The tokenizer converts the text into integer token IDs.

Conceptually:

```text
"Hello world"
      ↓
[ token_1, token_2 ]
      ↓
[ id_1, id_2 ]
```

The token IDs are the discrete numerical representation of the text.

---

## Step 3 — Pad the Sequence

The input processor determines the required sequence length.

If multiple sequences have different lengths, shorter sequences can be
padded.

Example:

```text
Original:

[10, 25, 42]

Padded:

[10, 25, 42, 0, 0]
```

The padding token ID is used for the additional positions.

---

## Step 4 — Create the Attention Mask

At the same time, an attention mask is created.

Example:

```text
Token IDs:

[10, 25, 42, 0, 0]

Attention Mask:

[ 1,  1,  1, 0, 0]
```

Meaning:

```text
1 → actual token
0 → padding
```

The mask will later be useful when the Transformer performs attention.

---

## Step 5 — Embedding Lookup

Each token ID is used as an index into the embedding matrix.

Conceptually:

```text
Token IDs
    ↓
Embedding Matrix
    ↓
Token Embeddings
```

If the embedding dimension is 128:

```text
3 tokens
   ↓
3 × 128 matrix
```

Each row represents one token's vector.

---

## Step 6 — Add Positional Information

The corresponding positional vectors are selected and added to the
token embeddings.

```text
Token Embeddings
       +
Position Embeddings
       ↓
Final Input Representation
```

This allows the representation to contain information about both:

- What token is present
- Where the token occurs

---

## Step 7 — Produce Model Input

The resulting matrix is the numerical representation that can be passed
to a neural network.

Conceptually:

```text
Sequence Length × Embedding Dimension
```

For example:

```text
512 × 128
```

if the sequence is padded to 512 positions and the embedding dimension
is 128.

---

# 3. Padding Workflow

The padding logic follows:

```text
Input Sequence
      ↓
Determine Maximum Length
      ↓
Truncate if Necessary
      ↓
Calculate Padding Length
      ↓
Append Padding IDs
      ↓
Create Attention Mask
      ↓
Return Both
```

The token IDs and mask must remain aligned.

Example:

```text
IDs:
[12, 45, 87, 0, 0]

Mask:
[ 1,  1,  1, 0, 0]
```

---

# 4. Embedding Workflow

The embedding layer performs a simple lookup.

```text
Token ID
   ↓
Index into embedding matrix
   ↓
Vector
```

For multiple tokens:

```text
[12, 45, 87]
      ↓
Embedding Matrix
      ↓
[
  vector_12,
  vector_45,
  vector_87
]
```

The embedding operation does not calculate semantic similarity itself.
It simply retrieves the vector associated with each token ID.

---

# 5. Positional Embedding Workflow

For a sequence of length `N`:

```text
Token Embeddings
       +
First N positional embeddings
       ↓
Position-aware representations
```

The position matrix is sliced to the current sequence length before
addition.

---

# 6. End-to-End Example

Input:

```text
"Hello world"
```

Conceptual transformation:

```text
RAW TEXT
"Hello world"
      ↓
TOKENIZATION
["Hello", " world"]
      ↓
TOKEN IDS
[15496, 995]
      ↓
PADDING
[15496, 995, 0, 0, ...]
      ↓
ATTENTION MASK
[1, 1, 0, 0, ...]
      ↓
EMBEDDING LOOKUP
[
  vector_15496,
  vector_995,
  vector_0,
  vector_0,
  ...
]
      ↓
POSITIONAL INFORMATION
Token Embeddings + Position Embeddings
      ↓
FINAL MODEL INPUT
Sequence Length × Embedding Dimension
```

The exact token IDs depend on the selected tokenizer encoding.

---

# 7. Health Check Workflow

Endpoint:

```text
GET /health
```

Flow:

```text
Client
  ↓
FastAPI
  ↓
Health Endpoint
  ↓
{"status": "healthy"}
```

This endpoint does not run the text-processing pipeline.

It exists to verify that the API service is running.

---

# 8. Startup Workflow

The application initializes its reusable components when the module is
loaded.

Conceptually:

```text
Application Start
      ↓
Create FastAPI App
      ↓
Initialize Tokenizer
      ↓
Determine Vocabulary Size
      ↓
Create Embedding Layer
      ↓
Create Positional Embedding
      ↓
Create Input Processor
      ↓
Start API Server
```

These components can then be reused across incoming requests.

---

# 9. Important Architectural Boundary

This project ends at:

```text
Final Model Input
```

The next stage:

```text
Model Input
    ↓
Attention
    ↓
Transformer Block
    ↓
Model Output
```

belongs to the Mini Transformer project.

This boundary keeps the learning progression clear.
