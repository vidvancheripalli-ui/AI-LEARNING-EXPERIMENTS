# AI Engineering Roadmap

This document defines the complete learning path for becoming a
production-ready AI Engineer.

The roadmap is designed around progressive capability building rather
than isolated technologies.

The objective is to move from understanding the foundations of modern
AI systems to designing, building, evaluating, deploying, securing,
and scaling real-world AI applications.

---

# 1. Roadmap Philosophy

This roadmap follows a progression:

```text
Understand
    ↓
Implement
    ↓
Build
    ↓
Evaluate
    ↓
Deploy
    ↓
Optimize
    ↓
Scale

The roadmap is project-driven.

A topic is not considered sufficiently learned merely because it has
been read or watched.

For important concepts, understanding should eventually be demonstrated
through implementation.

2. Overall Roadmap
                    AI ENGINEERING
                          │
          ┌───────────────┴────────────────┐
          │                                │
    AI APPLICATIONS                    AI FOUNDATIONS
          │                                │
          ↓                                ↓
   LLM Engineering                    ML Foundations
          ↓                                ↓
        RAG                         Deep Learning
          ↓                                ↓
      Evaluation                    ML Systems
          ↓
       Agents
          ↓
   Multi-Agent Systems
          ↓
   Production AI
          ↓
      Security
          ↓
  Interoperability

The practical learning path is:

1. LLM Foundations
2. LLM Engineering
3. Embeddings & Semantic Search
4. RAG
5. Evaluation & Observability
6. AI Agents
7. Multi-Agent Systems
8. AI Backend Engineering
9. Production AI
10. AI Security
11. Fine-Tuning
12. Multimodal AI
13. MCP & Agent Interoperability
14. Machine Learning
15. Deep Learning
16. ML Systems & MLOps
3. Phase 1 — LLM Foundations
Objective

Understand what happens inside modern language models instead of
treating LLMs as black-box APIs.

Topics
3.1 Text Representation

Learn:

Why machines cannot directly process raw text
Text representation
Vocabulary
Tokens
Token IDs
Sequence length
Tensor representation
3.2 Tokenization

Learn:

Character tokenization
Word tokenization
Subword tokenization
BPE
Vocabulary construction
Special tokens
Encoding
Decoding
Unknown tokens
Token counts
Tokenization effects on cost and context length
3.3 Embeddings

Learn:

Embedding vectors
Embedding dimensions
Embedding matrices
Embedding lookup
Semantic representation
Vector spaces
Similarity between vectors
Cosine similarity
Dot product
Euclidean distance
3.4 Positional Information

Learn:

Why order matters
Why self-attention needs positional information
Learned positional embeddings
Sinusoidal positional encoding
Relative positional information
Modern positional approaches conceptually
3.5 Attention

Learn:

Why attention was introduced
Query
Key
Value
Query-Key similarity
Dot-product attention
Scaling by √dₖ
Softmax
Attention weights
Weighted sum of values
Self-attention
Causal attention
Attention masking
3.6 Multi-Head Attention

Learn:

Why multiple heads are useful
Head dimensions
Parallel attention heads
Concatenation
Output projection
3.7 Transformer Architecture

Learn:

Transformer blocks
Feed-forward networks
Residual connections
Layer normalization
Attention + FFN
Encoder architecture
Decoder architecture
Encoder-decoder architecture
Decoder-only architecture
3.8 Language Model Generation

Learn:

Logits
Probability distributions
Softmax
Autoregressive generation
Temperature
Top-k
Top-p
Sampling
Greedy decoding
Context windows
KV cache
Projects
Project 1 — Text-to-Model-Input

Purpose:

Raw Text
   ↓
Tokens
   ↓
Token IDs
   ↓
Padding + Mask
   ↓
Embeddings
   ↓
Positional Information
   ↓
Model Input

Status:

Completed

Project 2 — Mini Transformer

Purpose:

Implement the major components of a Transformer directly.

Expected components:

Token embeddings
Positional information
Q/K/V projections
Self-attention
Scaling
Softmax
Causal masking
Multi-head attention
Feed-forward network
Residual connections
Layer normalization
Transformer block

Status:

Next

Project 3 — Mini-GPT

Purpose:

Combine the concepts learned in the previous projects into a small
decoder-only language model.

The objective is not to build a competitive LLM.

The objective is to understand the complete pipeline:

Text
 ↓
Tokenizer
 ↓
Token IDs
 ↓
Embeddings
 ↓
Transformer Blocks
 ↓
Logits
 ↓
Next-token prediction
 ↓
Generation
4. Phase 2 — LLM Engineering
Objective

Learn how to build applications around real LLMs.

The focus moves from:

"How does the model work?"

to:

"How do I build reliable software using the model?"

Topics
4.1 LLM APIs

Learn:

OpenAI-style APIs
Gemini APIs
Anthropic APIs
Open-source model APIs
API authentication
System instructions
User messages
Assistant messages
Streaming
Token usage
Context limits
Model selection
Rate limits
Retries
Timeouts
API failures
4.2 Prompt Engineering

Learn:

Zero-shot prompting
Few-shot prompting
Role prompting
Structured instructions
Constraints
Output formatting
Prompt decomposition
Prompt evaluation
4.3 Context Engineering

Learn:

What information should enter the context?
Context prioritization
Context compression
Context ordering
Context windows
Long-context limitations
Reducing irrelevant context
4.4 Structured Outputs

Learn:

JSON outputs
JSON schemas
Pydantic models
Validation
Parsing
Retry mechanisms
Output repair
Failure handling
4.5 Tool Calling

Learn:

Function calling
Tool schemas
Tool arguments
Tool execution
Tool results
Validation
Error handling
Permissions
Project
LLM Engineering Playground

A backend application for experimenting with:

Multiple LLM providers
Prompt templates
Structured outputs
Streaming
Tool calling
Token usage
Latency
Error handling

The project should expose the functionality through FastAPI.

5. Phase 3 — Embeddings & Semantic Search
Objective

Understand how semantic retrieval works before building full RAG systems.

Topics
Embeddings

Learn:

Sentence embeddings
Document embeddings
Query embeddings
Embedding models
Embedding dimensions
Normalization
Similarity metrics
Vector Search

Learn:

Cosine similarity
Dot product
Euclidean distance
Top-k retrieval
Similarity thresholds
Metadata filtering
Vector Databases

Learn deeply:

PostgreSQL + pgvector
Qdrant

Understand conceptually:

Pinecone
Weaviate
Other vector databases
Vector Indexing

Learn:

Why brute-force search does not scale
Approximate nearest-neighbor search
HNSW
Indexing trade-offs
Recall vs speed
Project
Semantic Search Engine

Build a system that:

Documents
   ↓
Chunking
   ↓
Embeddings
   ↓
Vector Database
   ↓
Query Embedding
   ↓
Similarity Search
   ↓
Top-K Results

Expose it through FastAPI.

6. Phase 4 — Retrieval-Augmented Generation
Objective

Learn how to build reliable RAG systems rather than simply
connecting an LLM to a vector database.

6.1 Document Ingestion

Learn:

PDF parsing
HTML parsing
Markdown parsing
DOCX parsing
CSV processing
Text cleaning
Metadata extraction
Document identification
Document versioning
6.2 Chunking

Learn:

Fixed-size chunking
Recursive chunking
Overlap
Semantic chunking
Metadata-aware chunking
Parent-child chunking

Understand the trade-off between:

Small chunks
    ↕
Large chunks
6.3 Retrieval

Learn:

Dense retrieval
Sparse retrieval
BM25
Hybrid retrieval
Metadata filtering
Query rewriting
Query expansion
Multi-query retrieval
Query decomposition
Context compression
6.4 Reranking

Learn:

Why initial retrieval is not always enough
Cross-encoder reranking
Candidate generation
Reranking
Top-k selection
6.5 Generation

Learn:

Context construction
Grounded generation
Citation generation
Insufficient evidence handling
Hallucination reduction
Source attribution
6.6 Advanced RAG

Learn conceptually and implement where useful:

Parent-child retrieval
Hybrid RAG
Agentic RAG
Contextual retrieval
Multimodal RAG
Graph RAG concepts
6.7 RAG Evaluation

Learn:

Retrieval relevance
Retrieval recall
Context relevance
Context precision
Answer relevance
Faithfulness
Groundedness
Citation correctness
Major Project — KnowledgeOS

A production-oriented knowledge intelligence platform.

Architecture:

                DOCUMENTS
                    │
                    ↓
             Ingestion Layer
                    │
                    ↓
        Parsing + Cleaning
                    │
                    ↓
              Chunking
                    │
                    ↓
        Metadata Extraction
                    │
                    ↓
              Embeddings
                    │
                    ↓
          Vector Database
                    │
                    │
USER QUERY ─────────┘
     │
     ↓
Query Analysis
     ↓
Query Rewriting
     ↓
Hybrid Retrieval
(Dense + BM25)
     ↓
Reranking
     ↓
Context Selection
     ↓
LLM
     ↓
Grounded Answer
     ↓
Citations

KnowledgeOS should eventually include:

Multi-document ingestion
Intelligent chunking
Metadata
Dense retrieval
BM25
Hybrid search
Reranking
Query rewriting
Multi-query retrieval
Parent-child retrieval
Context compression
Citation enforcement
Insufficient-evidence detection
Document version tracking
RAG evaluation
Latency tracking
Token/cost tracking
Observability
Authentication
Rate limiting
Background ingestion
7. Phase 5 — Evaluation & Observability
Objective

Move from:

"The AI works."

to:

"I can measure whether the AI works."

Evaluation

Learn:

Golden datasets
Test cases
Expected outputs
Regression testing
Human evaluation
Rule-based evaluation
LLM-as-a-judge
Pairwise comparison
RAG Evaluation

Measure:

Retrieval relevance
Recall
Context relevance
Faithfulness
Groundedness
Answer relevance
Citation correctness
Agent Evaluation

Measure:

Task completion
Tool selection
Tool arguments
Trajectory quality
Evidence usage
Final answer quality
Observability

Learn:

Structured logging
LLM request logs
Token usage
Cost
Latency
TTFT
Throughput
Error rates
Tracing
Retrieval traces
Tool traces
Agent trajectories
Projects
RAG Evaluation Lab

Build evaluation infrastructure for KnowledgeOS.

AI Observability Lab

Instrument an existing AI system rather than creating an isolated
toy system.

8. Phase 6 — AI Agents
Objective

Understand how an LLM can operate as a system that observes,
decides, acts and evaluates results.

Topics
Agent Fundamentals

Learn:

What makes an application an agent?
Agent loop
Observation
Reasoning/planning
Action
Tool execution
Tool results
State
Termination
Tools

Implement tools for:

Search
Calculator
Database
APIs
Files
RAG
Reliability

Learn:

Retries
Timeouts
Tool failures
Validation
Permissions
Human-in-the-loop
Guardrails
Memory

Learn:

Short-term memory
Long-term memory
State
Persistence
Checkpointing
LangGraph

Learn:

Nodes
Edges
Conditional routing
Cycles
State
Persistence
Checkpoints
Human-in-the-loop
Streaming
Project — Tool-Using AI Agent

Build an agent capable of:

User
 ↓
Agent
 ↓
Decide whether a tool is required
 ↓
Select tool
 ↓
Execute tool
 ↓
Observe result
 ↓
Continue / terminate
 ↓
Final response

The system should expose its functionality through FastAPI.

9. Phase 7 — Multi-Agent Systems
Objective

Understand when multiple specialized agents are actually useful and
how to coordinate them reliably.

Topics

Learn:

Supervisor architecture
Worker agents
Planner / executor
Sequential agents
Parallel agents
Delegation
Shared state
Message passing
Result passing
Recovery
Retries
Validation
Human approval
Evaluation

Learn how to evaluate:

Task completion
Agent selection
Tool selection
Tool arguments
Agent trajectories
Evidence
Final quality
Major Project — Real-World Multi-Agent System

Build a genuinely useful multi-agent system around a real problem.

The architecture should emerge from the problem rather than forcing
multiple agents into a system unnecessarily.

Possible architecture:

                User
                  │
                  ↓
             Supervisor
            /     |      \
           ↓      ↓       ↓
       Agent A  Agent B  Agent C
           \      |      /
            \     |     /
             ↓    ↓    ↓
              Shared State
                   ↓
              Final Result

The final problem domain will be selected based on whether multiple
agents provide genuine value.

10. Phase 8 — AI Backend Engineering
Objective

Become capable of building the backend infrastructure required by
real AI applications.

FastAPI

Learn:

Routing
Pydantic
Dependency injection
Middleware
Async programming
Background tasks
Streaming
WebSockets
Authentication
Error handling
PostgreSQL

Learn:

SQL
Joins
Indexes
Transactions
Constraints
Normalization
Query optimization
Connection pooling
Redis

Learn:

Caching
TTL
Sessions
Pub/Sub
Queues
Rate limiting
Reliability

Learn:

Retries
Timeouts
Idempotency
Rate limiting
Circuit breakers
Background workers
Queues
11. Phase 9 — Production AI
Objective

Learn how to take an AI application from:

localhost

to:

reliable production service
Docker

Learn:

Images
Containers
Dockerfiles
Volumes
Networks
Environment variables
Multi-stage builds
Cloud

Focus on one major cloud platform first.

Learn:

Compute
Storage
Databases
IAM
Secrets
Networking
HTTPS
Logging
CI/CD

Learn:

GitHub Actions
Automated testing
Build pipelines
Docker builds
Deployment
Environment management
Performance

Learn:

Streaming
Async inference
Caching
Batching
Concurrency
Throughput
Latency
TTFT
Cost Optimization

Learn:

Model selection
Context reduction
Caching
Model routing
Token optimization
Monitoring
12. Phase 10 — AI Security
Objective

Understand the unique security problems introduced by AI systems.

Topics

Learn:

API key security
Secrets management
Authentication
Authorization
Input validation
Output validation
Prompt injection
Indirect prompt injection
Jailbreaks
Data leakage
PII protection
Agent Security

Learn:

Excessive agency
Tool abuse
Permission boundaries
Sandboxing
Human approval
Audit logs
Tool authorization

Security should be integrated into major projects rather than treated
only as theory.

13. Phase 11 — Fine-Tuning
Objective

Understand when prompting and RAG are insufficient and when model
adaptation becomes useful.

Topics

Learn:

Pretraining
Instruction tuning
Supervised fine-tuning
Dataset preparation
Evaluation
LoRA
QLoRA
PEFT
Adapters
Quantization
8-bit models
4-bit models
Project
LoRA / QLoRA Experiment

Build a small fine-tuning pipeline.

Compare:

Base Model
     vs
Fine-Tuned Model

using a defined evaluation dataset.

The goal is understanding the process and trade-offs rather than
training a large model.

14. Phase 12 — Multimodal AI
Objective

Understand AI systems that operate beyond text.

Topics

Learn:

Vision-language models
Image understanding
OCR
Image embeddings
Speech-to-text
Text-to-speech
Audio understanding
Multimodal RAG
Multimodal agents
Project
Multimodal AI Experiment

Build a useful application involving at least one non-text modality.

15. Phase 13 — MCP & Agent Interoperability
Objective

Understand how AI systems can discover and interact with external
tools and services through standardized interfaces.

MCP

Learn:

MCP clients
MCP servers
Tools
Resources
Prompts
Discovery
Execution
Permissions
Security
Agent Interoperability

Learn conceptually:

Agent-to-agent communication
APIs
Webhooks
Event-driven communication
Agent protocols
Project
MCP Tool Server

Build an MCP server exposing useful tools and connect it to an
AI agent.

16. Phase 14 — Machine Learning Foundations

This phase provides the classical ML foundation necessary for
understanding the broader AI ecosystem.

It does not aim to turn the journey into a pure Data Science roadmap.

Topics
Data

Learn:

Data exploration
Cleaning
Feature engineering
Missing values
Outliers
Encoding
Scaling
Supervised Learning

Learn:

Linear regression
Logistic regression
Decision trees
Random forests
Gradient boosting
XGBoost
SVM
KNN
Unsupervised Learning

Learn:

K-Means
PCA
Clustering concepts
Dimensionality reduction
Model Evaluation

Learn:

Train/validation/test split
Cross-validation
Bias
Variance
Overfitting
Underfitting
Regularization
Feature selection
Class imbalance
Data leakage
Metrics

Learn:

Accuracy
Precision
Recall
F1
ROC-AUC
PR-AUC
MAE
MSE
RMSE
R²
Project
Classical ML Prediction System

Build an end-to-end ML prediction service.

Pipeline:

Data
 ↓
Cleaning
 ↓
Feature Engineering
 ↓
Training
 ↓
Validation
 ↓
Evaluation
 ↓
Model Selection
 ↓
Deployment
 ↓
FastAPI Prediction Service
17. Phase 15 — Deep Learning
Objective

Understand neural networks and the foundations behind modern deep
learning systems.

Neural Networks

Learn:

Tensors
Layers
Activations
Forward propagation
Loss functions
Backpropagation
Gradient descent
Optimization

Learn:

SGD
Adam
Learning rate
Batch size
Weight decay
Dropout
Batch normalization
Early stopping
Architectures

Learn:

CNNs
RNNs
LSTMs
GRUs
Attention
Transformers
PyTorch

Learn:

Tensors
Dataset
DataLoader
Models
forward()
Loss functions
Optimizers
Training loops
Validation
GPU usage
Saving/loading models
Project
PyTorch Deep Learning Project

Build and deploy a complete deep learning application.

18. Phase 16 — ML Systems & MLOps
Objective

Understand what happens after a machine learning model has been
trained.

Topics

Learn:

Data pipelines
Feature engineering pipelines
Training pipelines
Offline evaluation
Model deployment
Model serving
Monitoring
Data drift
Distribution shift
Model degradation
Retraining
Continual learning
Experiment tracking
ML infrastructure
Reference

Primary reference:

Designing Machine Learning Systems — Chip Huyen

19. Continuous Engineering Skills

These skills are developed throughout the roadmap rather than being
isolated into one phase.

Git & GitHub

Practice:

Branching
Commits
Pull requests
Rebasing
Merge conflicts
Git history
Repository organization
Testing

Practice:

Unit tests
Integration tests
API tests
Evaluation tests
Regression tests
Linux

Practice:

CLI
Processes
Environment variables
Networking basics
File systems
Permissions
Software Engineering

Practice:

Clean code
Modular design
Separation of concerns
Error handling
Logging
Configuration
Dependency management
API design
20. Project Progression

The complexity of projects should increase gradually.

                    Complexity
                       ↑
                       │
                       │                 KnowledgeOS
                       │                    /
                       │                  /
                       │          Multi-Agent
                       │             /
                       │       Tool Agent
                       │          /
                       │    Semantic Search
                       │       /
                       │  Mini Transformer
                       │     /
                       │ Text-to-Model-Input
                       │
                       └────────────────────────→
                              Time

The objective is not to make every project huge.

Small projects should teach specific concepts.

Major projects should demonstrate system-level engineering.

21. Learning vs Project Work

A critical distinction is maintained throughout the roadmap.

Learning Topics

These are concepts that must be understood.

Examples:

Attention
BPE
Embeddings
BM25
Reranking
KV Cache
LoRA
Backpropagation
Projects

These are systems used to prove and reinforce understanding.

Examples:

Text-to-Model-Input
Mini Transformer
KnowledgeOS
Multi-Agent System
Student RidePool

A project may contain many learning topics.

A learning topic may also appear in multiple projects.

22. Project Documentation Requirement

Every substantial project should eventually contain:

README.md

docs/
├── architecture.md
├── design-decisions.md
├── tradeoffs.md
├── api.md
├── workflows.md
├── learning-notes.md
└── diagrams/

Documentation should capture the actual engineering process.

It should not become a copy of a textbook.

23. Definition of Mastery

A topic is considered sufficiently learned when I can:

Explain the concept in my own words.
Explain why it exists.
Implement its basic form.
Use the relevant abstraction/library correctly.
Identify common failure modes.
Explain important trade-offs.
Debug a basic implementation.
Explain how it fits into a larger system.

For advanced topics, I should additionally be able to discuss:

Scalability
Reliability
Security
Cost
Performance
Evaluation
24. Application Strategy

The roadmap is intentionally not a prerequisite checklist where every
phase must be completed before applying for internships.

Applications should begin once the foundation is strong enough to
demonstrate meaningful AI engineering ability.

Target point:

LLM Foundations
      ↓
LLM Engineering
      ↓
Embeddings
      ↓
RAG
      ↓
First serious project
      ↓
START APPLYING
      ↓
Continue learning while applying

The objective is to avoid waiting until the entire roadmap is finished.

Learning and applications should happen in parallel.

25. Final Capability Target

By the end of the roadmap, I should be capable of taking a problem
from:

Real-world problem
      ↓
Requirements
      ↓
System design
      ↓
Model / LLM selection
      ↓
Data / retrieval architecture
      ↓
Backend implementation
      ↓
Evaluation
      ↓
Security
      ↓
Deployment
      ↓
Monitoring
      ↓
Optimization
      ↓
Production system

The final objective is not:

"I know AI technologies."

It is:

"I can engineer AI systems."