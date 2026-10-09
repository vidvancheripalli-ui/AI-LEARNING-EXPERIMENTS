# AI Engineering Projects

This document is the master catalogue of projects, experiments, labs,
and major systems built throughout the AI Engineering Journey.

Projects are not created merely to increase the number of repositories.

Each project exists to answer one or more of the following questions:

- Can I implement this concept?
- Do I actually understand this technology?
- Can I integrate multiple concepts into a system?
- Can I solve a real engineering problem?
- Can I evaluate whether the system works?
- Can I deploy and operate it?
- Can I explain the architectural decisions behind it?

---

# 1. Project Philosophy

The projects follow a progression:

```text
Concept
   ↓
Small Implementation
   ↓
Focused Project
   ↓
Integrated System
   ↓
Production-Oriented System

Not every project needs to be production-grade.

Small projects exist primarily for understanding.

Major projects exist to demonstrate system-level engineering.

2. Project Categories

Projects are divided into four broad categories.

2.1 Foundation Projects

Small projects designed to understand fundamental AI concepts.

Examples:

Text-to-Model-Input
Mini Transformer
Mini-GPT

These projects deliberately avoid unnecessary production complexity.

2.2 Engineering Projects

Projects designed to practice building usable AI software.

Examples:

LLM Engineering Playground
Semantic Search Engine
Tool-Using AI Agent

These emphasize APIs, architecture, integration and reliability.

2.3 Major AI Systems

Large projects combining multiple concepts into realistic systems.

Examples:

KnowledgeOS
Real-World Multi-Agent System

These are intended to demonstrate substantial AI engineering ability.

2.4 Supporting / Backend Projects

Projects that strengthen general software engineering and backend
capability.

Example:

Student RidePool

These projects are part of the engineering foundation even when AI is
not the primary feature.

3. Project Status

The following statuses are used throughout this document.

Status	Meaning
🧠 Learning	Concepts are currently being studied
🔜 Next	Next project to build
🚧 In Progress	Implementation currently underway
🧪 Experiment	Small experimental project
🟡 Planned	Planned but not started
🔄 Iterating	Initial implementation complete, improvements ongoing
✅ Completed	Project completed and documented
🚀 Deployed	Project deployed and operational
📦 Archived	Completed or intentionally discontinued

A project can have multiple relevant states.

For example:

🚀 Deployed + 🔄 Iterating
4. Master Project Catalogue
#	Project	Category	Primary Area	Status
1	Text-to-Model-Input	Foundation	LLM Foundations	✅ Completed
2	Mini Transformer	Foundation	Transformers	🔜 Next
3	Mini-GPT	Foundation	Language Models	🟡 Planned
4	LLM Engineering Playground	Engineering	LLM Engineering	🟡 Planned
5	Semantic Search Engine	Engineering	Embeddings	🟡 Planned
6	KnowledgeOS	Major System	Advanced RAG	🟡 Planned
7	Tool-Using AI Agent	Engineering	Agents	🟡 Planned
8	Real-World Multi-Agent System	Major System	Multi-Agent AI	🟡 Planned
9	Student RidePool	Backend System	Backend Engineering	🚧 In Progress
10	Classical ML Prediction System	Learning Project	Machine Learning	🟡 Planned
11	PyTorch Deep Learning Project	Learning Project	Deep Learning	🟡 Planned
12	LoRA / QLoRA Experiment	Experiment	Fine-Tuning	🟡 Planned
13	Multimodal AI Experiment	Experiment	Multimodal AI	🟡 Planned
14	MCP Tool Server	Engineering	AI Interoperability	🟡 Planned
15	RAG Evaluation Lab	Supporting Project	AI Evaluation	🟡 Planned
16	AI Observability Lab	Supporting Project	Observability	🟡 Planned

The catalogue will evolve as the roadmap progresses.

Projects may be added, merged, split, or removed when doing so
improves the learning path.

5. Project 1 — Text-to-Model-Input
Category

Foundation Project

Area

LLM Foundations

Status

✅ Completed

Objective

Understand what happens between raw text and the numerical representation
consumed by a neural network.

The complete pipeline is:

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
Concepts Demonstrated
Text representation
Tokenization
BPE / subword tokenization
Vocabulary
Token IDs
Sequence length
Embeddings
Embedding dimensions
Embedding lookup
Positional embeddings
Padding
Attention masks
Tensor / matrix shapes
Context length
Token-count implications
Technologies
Python
NumPy
tiktoken
FastAPI
Uvicorn
API
GET  /health
POST /tokenize
POST /model-input
Main Learning Outcome

Understand the transformation:

Human-readable text
        ↓
Discrete representation
        ↓
Numerical representation
        ↓
Model-ready input
Important Engineering Decisions
Use a real tokenizer rather than inventing a fake tokenizer.
Use tiktoken for practical tokenizer exposure.
Use NumPy to make embedding lookup explicit.
Use a learnable positional embedding matrix.
Perform padding on token IDs before embedding lookup.
Expose the pipeline through FastAPI.
Documentation

The project contains:

docs/
├── architecture.md
├── design-decisions.md
├── tradeoffs.md
├── api.md
├── workflows.md
├── learning-notes.md
└── diagrams/
6. Project 2 — Mini Transformer
Category

Foundation Project

Area

Transformers

Status

🔜 Next

Objective

Understand and implement the core components of a Transformer.

Concepts
Query
Key
Value
Q/K/V projections
Dot-product attention
Scaling
Softmax
Attention weights
Causal masking
Self-attention
Multi-head attention
Feed-forward networks
Residual connections
Layer normalization
Transformer blocks
Intended Pipeline
Token IDs
   ↓
Embeddings
   ↓
Positional Information
   ↓
Q/K/V
   ↓
Self-Attention
   ↓
Multi-Head Attention
   ↓
Residual + LayerNorm
   ↓
Feed-Forward Network
   ↓
Residual + LayerNorm
   ↓
Transformer Output
Main Learning Outcome

Understand the fundamental computation behind Transformer-based models.

7. Project 3 — Mini-GPT
Category

Foundation Project

Area

Decoder-Only Language Models

Status

🟡 Planned

Objective

Combine the Transformer concepts into a small decoder-only language
model.

Core Pipeline
Text
 ↓
Tokenizer
 ↓
Token IDs
 ↓
Embeddings
 ↓
Positional Information
 ↓
Transformer Blocks
 ↓
Linear Projection
 ↓
Logits
 ↓
Next Token Prediction
 ↓
Autoregressive Generation
Concepts
Decoder-only architecture
Causal attention
Next-token prediction
Logits
Cross-entropy loss
Training loop
Autoregressive generation
Sampling
Main Learning Outcome

Understand the end-to-end mechanics of a small language model.

8. Project 4 — LLM Engineering Playground
Category

Engineering Project

Area

LLM Application Engineering

Status

🟡 Planned

Objective

Build a backend playground for understanding practical LLM
application development.

Features
Multiple model providers
Prompt templates
System instructions
Streaming
Structured outputs
JSON schemas
Pydantic validation
Tool calling
Token tracking
Latency measurement
Error handling
Retries
Timeouts
Architecture
Client
  ↓
FastAPI
  ↓
LLM Service Layer
  ↓
Model Provider
  ↓
Response Processing
  ↓
Validation
  ↓
Client
Main Learning Outcome

Move from understanding LLM internals to building applications
around real LLM APIs.

9. Project 5 — Semantic Search Engine
Category

Engineering Project

Area

Embeddings & Vector Search

Status

🟡 Planned

Objective

Understand semantic search before introducing the complexity of
full RAG.

Pipeline
Documents
   ↓
Chunking
   ↓
Embedding Model
   ↓
Vectors
   ↓
Vector Database

Query
   ↓
Query Embedding
   ↓
Similarity Search
   ↓
Top-K Results
Concepts
Embeddings
Vector spaces
Cosine similarity
Dot product
Top-k retrieval
Metadata filtering
Vector indexing
HNSW
pgvector
Qdrant
Main Learning Outcome

Understand how semantic retrieval works independently of generation.

10. Project 6 — KnowledgeOS
Category

Major AI System

Area

Advanced RAG

Status

🟡 Planned

Objective

Build a production-oriented knowledge intelligence platform.

KnowledgeOS is the primary RAG project of this journey.

Core Pipeline
                    DOCUMENTS
                        ↓
                  INGESTION
                        ↓
               PARSING / CLEANING
                        ↓
                    CHUNKING
                        ↓
                METADATA EXTRACTION
                        ↓
                   EMBEDDINGS
                        ↓
                 VECTOR STORAGE


USER QUERY
    ↓
QUERY ANALYSIS
    ↓
QUERY REWRITING
    ↓
HYBRID RETRIEVAL
(Dense + BM25)
    ↓
RERANKING
    ↓
CONTEXT SELECTION
    ↓
LLM
    ↓
GROUNDED ANSWER
    ↓
CITATIONS
Features
Ingestion
PDF
HTML
Markdown
DOCX
CSV
Text
Cleaning
Metadata
Version tracking
Retrieval
Dense retrieval
Sparse retrieval
BM25
Hybrid retrieval
Metadata filtering
Query rewriting
Multi-query retrieval
Query decomposition
Reranking
Parent-child retrieval
Context compression
Generation
Grounded responses
Citation enforcement
Insufficient evidence detection
Source attribution
Evaluation
Retrieval evaluation
Answer evaluation
Faithfulness
Groundedness
Citation correctness
Regression testing
Production
Authentication
Rate limiting
Background ingestion
Caching
Observability
Token/cost tracking
Latency tracking
Main Learning Outcome

Learn how to engineer a serious RAG system rather than a simple:

PDF → Vector DB → LLM

application.

11. Project 7 — Tool-Using AI Agent
Category

Engineering Project

Area

AI Agents

Status

🟡 Planned

Objective

Build an agent that can decide when to use external tools and
execute them.

Architecture
User
 ↓
Agent
 ↓
Observe State
 ↓
Decide Action
 ↓
Select Tool
 ↓
Execute Tool
 ↓
Observe Result
 ↓
Continue / Terminate
 ↓
Final Response
Tools

Potential tools:

Search
Calculator
Database
Files
APIs
RAG
Reliability
Tool validation
Timeouts
Retries
Permission checks
Error handling
Human approval where appropriate
Main Learning Outcome

Understand the difference between a normal LLM application and an
agentic system.

12. Project 8 — Real-World Multi-Agent System
Category

Major AI System

Area

Multi-Agent AI

Status

🟡 Planned

Objective

Build a genuinely useful multi-agent system where multiple agents
provide real value rather than being artificially added.

Possible Architecture
                    User
                      ↓
                 Supervisor
                /    |    \
               ↓     ↓     ↓
           Agent A Agent B Agent C
               \     |     /
                \    |    /
                 Shared State
                      ↓
                 Final Result

The final problem domain will be selected later based on actual
requirements.

Concepts
Supervisor agents
Worker agents
Planner / executor
Delegation
Shared state
Message passing
Parallel execution
Sequential execution
Recovery
Validation
Human-in-the-loop
Agent evaluation
Agent tracing
Main Learning Outcome

Understand when multi-agent architecture is useful and how to make
such systems reliable.

13. Project 9 — Student RidePool
Category

Backend Engineering Project

Area

Backend / Distributed-System Foundations

Status

🚧 In Progress

Objective

Build a real-world student ride-sharing / ride-pooling backend.

This project strengthens the engineering foundation required to build
AI systems later.

Core Areas
FastAPI
PostgreSQL
Authentication
Database modeling
API design
Transactions
Validation
Matching logic
Background processing
Backend architecture
Deployment
Main Learning Outcome

Develop strong backend engineering fundamentals that can later support
AI agents and production AI systems.

Relationship to AI Journey

This is not being abandoned simply because it is not primarily an AI
project.

AI systems are software systems.

The backend, database, reliability and API knowledge developed here
will be reused throughout the AI Engineering Journey.

14. Project 10 — Classical ML Prediction System
Category

Learning Project

Area

Machine Learning

Status

🟡 Planned

Objective

Build an end-to-end classical machine learning system.

Pipeline
Dataset
 ↓
EDA
 ↓
Cleaning
 ↓
Feature Engineering
 ↓
Train / Validation / Test
 ↓
Model Training
 ↓
Evaluation
 ↓
Model Selection
 ↓
Deployment
 ↓
FastAPI Prediction API
Models

Potential models:

Linear Regression
Logistic Regression
Decision Trees
Random Forest
Gradient Boosting
XGBoost
SVM
Main Learning Outcome

Understand the classical ML workflow from raw data to deployed
prediction service.

15. Project 11 — PyTorch Deep Learning Project
Category

Learning Project

Area

Deep Learning

Status

🟡 Planned

Objective

Build and train a neural network using PyTorch.

Concepts
Tensors
Datasets
DataLoaders
Neural networks
Forward pass
Loss
Backpropagation
Optimizers
Training
Validation
GPU
Model saving/loading
Main Learning Outcome

Understand the mechanics of deep learning training rather than only
using high-level model APIs.

16. Project 12 — LoRA / QLoRA Experiment
Category

Experiment

Area

Fine-Tuning

Status

🟡 Planned

Objective

Understand parameter-efficient fine-tuning.

Topics
Dataset preparation
Supervised fine-tuning
LoRA
QLoRA
PEFT
Quantization
Evaluation
Comparison
Base Model
     ↓
Evaluation

Fine-Tuned Model
     ↓
Evaluation

Compare Results
Main Learning Outcome

Understand when and why model fine-tuning is useful.

17. Project 13 — Multimodal AI Experiment
Category

Experiment

Area

Multimodal AI

Status

🟡 Planned

Objective

Build a system that processes more than one modality.

Potential capabilities:

Image understanding
OCR
Image embeddings
Speech-to-text
Text-to-speech
Multimodal RAG

The exact project will be selected later based on the learning
requirements at that stage.

18. Project 14 — MCP Tool Server
Category

Engineering Project

Area

AI Interoperability

Status

🟡 Planned

Objective

Understand how AI agents can discover and use standardized external
tools.

Topics
MCP server
MCP client
Tools
Resources
Prompts
Discovery
Execution
Permissions
Security
Architecture
AI Agent
   ↓
MCP Client
   ↓
MCP Server
   ↓
Tools / Resources
   ↓
External Systems
19. Project 15 — RAG Evaluation Lab
Category

Supporting Project

Area

AI Evaluation

Status

🟡 Planned

Objective

Build reusable evaluation infrastructure for RAG systems.

Evaluate
Retrieval relevance
Retrieval recall
Context relevance
Faithfulness
Groundedness
Answer relevance
Citation correctness

The lab should eventually be used to evaluate KnowledgeOS rather than
remaining an isolated toy project.

20. Project 16 — AI Observability Lab
Category

Supporting Project

Area

AI Observability

Status

🟡 Planned

Objective

Learn how to observe and debug AI systems.

Capture
Requests
Responses
Tokens
Cost
Latency
TTFT
Errors
Retrieval steps
Tool calls
Agent trajectories

The preferred approach is to instrument an existing project rather
than creating an unnecessary standalone application.

21. Project Relationships

The projects are intentionally connected.

Text-to-Model-Input
        ↓
Mini Transformer
        ↓
Mini-GPT
        ↓
LLM Engineering Playground
        ↓
Semantic Search Engine
        ↓
KnowledgeOS
        ↓
Tool-Using Agent
        ↓
Multi-Agent System
        ↓
Production AI Systems

Supporting engineering:

Student RidePool
      ↓
FastAPI
PostgreSQL
Auth
Transactions
Backend Architecture
      ↓
Used throughout later AI projects

ML foundation:

Classical ML
     ↓
Deep Learning
     ↓
Fine-Tuning
     ↓
ML Systems

Evaluation and observability:

RAG Evaluation
      ↓
Agent Evaluation
      ↓
Production Observability
22. Project Completion Standard

A project should not be marked complete simply because the code runs.

Before marking a substantial project as complete, verify:

Understanding
 I understand the concepts used.
 I can explain the architecture.
 I understand the important design decisions.
 I understand the major trade-offs.
 I can explain important failure cases.
Implementation
 Core functionality works.
 Important edge cases are considered.
 API works where applicable.
 Tests or sanity checks exist.
Engineering
 Error handling exists.
 Logging exists where useful.
 Configuration is separated appropriately.
 Secrets are not committed.
 Project structure is understandable.
Documentation
 README exists.
 Architecture is documented.
 Workflows are documented.
 Design decisions are documented.
 Trade-offs are documented.
 API is documented.
 Important learning notes are documented.
 Important debugging lessons are recorded.
Delivery
 Code is pushed to GitHub.
 Deployment completed when appropriate.
 Project can be demonstrated.
 I can explain the project without relying on the code editor.
23. What Counts as a Finished Project?

A finished project should leave behind three things:

                PROJECT
                   │
        ┌──────────┼──────────┐
        ↓          ↓          ↓
      CODE      KNOWLEDGE   EVIDENCE
        │          │          │
        ↓          ↓          ↓
    GitHub      Docs       Demo/API

The code proves that something was built.

The documentation proves that the engineering decisions were
understood.

The demo/deployment proves that the system can actually be used.

24. Project Evolution

Projects are allowed to evolve.

A project may be:

Built
 ↓
Tested
 ↓
Deployed
 ↓
Observed
 ↓
Improved
 ↓
Refactored
 ↓
Scaled

A project does not need to be perfect at version 1.

The important requirement is that improvements should be driven by
actual problems, measurements, or newly learned concepts.

25. Current Focus

Current project:

Text-to-Model-Input — Completed

Current learning topic:

Tokens and Embeddings

Next project:

Mini Transformer

Current priority:

Finish learning Tokens & Embeddings
              ↓
Understand Attention
              ↓
Build Mini Transformer
              ↓
Document Mini Transformer
              ↓
Continue to Mini-GPT
26. Final Objective

The purpose of this project portfolio is not to accumulate
repositories.

The objective is to create evidence that I can:

Understand
   ↓
Design
   ↓
Implement
   ↓
Evaluate
   ↓
Debug
   ↓
Deploy
   ↓
Observe
   ↓
Improve

AI systems in the real world.

The final portfolio should demonstrate not only that I can use AI
libraries, but that I understand the engineering behind the systems
I build.