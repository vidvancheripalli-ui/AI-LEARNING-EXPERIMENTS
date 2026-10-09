# API Documentation

The Text-to-Model-Input project exposes its core functionality through
a FastAPI application.

Base URL during local development:

```text
http://127.0.0.1:8000
```

Interactive API documentation is available through FastAPI's generated
documentation when the server is running.

---

# 1. GET `/health`

Checks whether the API is running.

## Request

```http
GET /health
```

No request body is required.

## Response

```json
{
  "status": "healthy"
}
```

---

# 2. POST `/tokenize`

Converts raw text into tokens and token IDs.

## Request

```http
POST /tokenize
Content-Type: application/json
```

### Body

```json
{
  "text": "Hello world"
}
```

The request is validated using the `TextRequest` Pydantic schema.

---

## Response

```json
{
  "text": "Hello world",
  "tokens": [
    "Hello",
    " world"
  ],
  "token_ids": [
    15496,
    995
  ],
  "token_count": 2
}
```

The exact token IDs and token boundaries depend on the tokenizer
encoding.

## Response Fields

| Field | Type | Description |
|---|---|---|
| `text` | string | Original input text |
| `tokens` | array | Human-readable token pieces |
| `token_ids` | array | Integer IDs assigned to the tokens |
| `token_count` | integer | Number of tokens |

---

# 3. POST `/model-input`

Transforms raw text into a model-ready numerical representation.

## Request

```http
POST /model-input
Content-Type: application/json
```

### Body

```json
{
  "text": "Hello world"
}
```

---

## Processing Pipeline

The endpoint performs:

```text
Text
 ↓
Tokenization
 ↓
Token IDs
 ↓
Padding
 ↓
Attention Mask
 ↓
Embedding Lookup
 ↓
Positional Embedding
 ↓
Final Model Input
```

---

## Response

The endpoint returns information describing the generated model input.

Example:

```json
{
  "text": "Hello world",
  "token_ids": [
    15496,
    995
  ],
  "attention_mask": [
    1,
    1
  ],
  "sequence_length": 2,
  "embedding_dimension": 128
}
```

## Response Fields

| Field | Type | Description |
|---|---|---|
| `text` | string | Original input text |
| `token_ids` | array | Original token IDs |
| `attention_mask` | array | Indicates real-token and padding positions |
| `sequence_length` | integer | Length of the final representation |
| `embedding_dimension` | integer | Size of each embedding vector |

The actual embedding matrix is intentionally not returned by the API
in the current implementation.

---

# 4. Request Validation

Requests use a Pydantic model:

```python
class TextRequest(BaseModel):
    text: str
```

Therefore the API expects a JSON object containing a `text` field.

Invalid request bodies are rejected by FastAPI/Pydantic validation.

---

# 5. Running the API

From the project root:

```bash
uvicorn app.main:app --reload
```

The important format is:

```text
uvicorn <module>:<application-object>
```

For this project:

```text
app.main:app
```

because the FastAPI instance is named `app`.

---

# 6. API Design Scope

The API is intentionally small.

The purpose is to expose the learning pipeline rather than build a
large production service.

Current endpoints:

```text
GET  /health
POST /tokenize
POST /model-input
```

Future projects will introduce more advanced API capabilities such as
streaming, authentication, background tasks, and more complex request
flows.
