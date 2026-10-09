# Learning Guidelines

This document defines the rules I will follow throughout the
AI Engineering Journey.

The goal is to build genuine understanding and engineering ability,
not simply finish courses or collect technologies.

---

## 1. Learn → Build → Understand

The core learning loop is:

```text
Learn concept
    ↓
Implement directly in project
    ↓
Test
    ↓
Encounter problems
    ↓
Research
    ↓
Understand
    ↓
Document
    ↓
Move on
```

Avoid unnecessary toy experiments when the concept can be learned
directly through the actual project.

---

## 2. Understand Before Using Abstractions

For important technologies, I should understand what happens underneath
before relying entirely on a high-level library.

I don't need to recreate production libraries, but I should understand
the underlying mechanism.

### Example

Don't only use:

```text
Vector Database
```

Understand:

```text
Embedding → Vector → Similarity → Index → Retrieval
```

---

## 3. Every Technology Needs a Reason

For every important technology or architectural choice, understand:

- What problem does it solve?
- Why do I need it?
- Why did I choose it?
- What are the alternatives?
- What are the trade-offs?
- When would another option be better?

---

## 4. Avoid Resource Overload

Use a small number of strong resources.

Do not continuously switch between:

- Courses
- YouTube playlists
- Books
- Tutorials
- Blog posts

A new resource should only be introduced when the current resource
cannot answer an important question.

Primary references should remain stable throughout the journey.

---

## 5. Projects Are the Main Proof of Learning

Reading a concept is not enough.

Important concepts should appear in working code.

```text
Theory
  ↓
Implementation
  ↓
Project
  ↓
Understanding
```

Projects should solve meaningful problems wherever possible.

---

## 6. Don't Build Unnecessary Complexity

Start with the simplest correct implementation.

Then introduce complexity only when there is a reason.

```text
Correct
  ↓
Reliable
  ↓
Performant
  ↓
Scalable
  ↓
Production-ready
```

Do not add technologies simply because they look impressive.

---

## 7. Debugging Is Learning

When something breaks:

1. Reproduce the problem.
2. Understand the error.
3. Identify the root cause.
4. Fix it.
5. Understand why the fix works.
6. Document important lessons.

Do not blindly copy fixes from the internet.

---

## 8. Documentation Is Part of the Project

A substantial project is not complete until its important decisions
and workflows are documented.

### Document

- Architecture
- Data/request flow
- Design decisions
- Trade-offs
- APIs
- Important bugs
- Learning notes

Documentation should capture engineering reasoning, not copy
textbook definitions.

---

## 9. Build for Understanding, Then Improve

For every project:

```text
Version 1
  ↓
Make it work
  ↓
Understand it
  ↓
Test it
  ↓
Improve reliability
  ↓
Improve performance
  ↓
Consider scalability
```

Do not prematurely optimize.

---

## 10. FastAPI as a Repeated Skill

Meaningful AI projects should expose their core functionality through
FastAPI where appropriate.

This provides repeated practice with:

- API design
- Pydantic
- Validation
- Async programming
- Streaming
- Error handling
- Authentication
- AI service integration

Small projects should not be overloaded with unnecessary backend
complexity.

---

## 11. Every Project Must Be Explainable

After completing a project, I should be able to explain:

- What problem it solves
- How it works
- Its architecture
- Why major technologies were chosen
- Important alternatives
- Major failure cases
- How it could scale

If I cannot explain it, I don't consider the learning complete.

---

## 12. Don't Leave Projects Half-Finished

Avoid starting another major project simply because something new
looks interesting.

Before moving on:

```text
Build
 ↓
Test
 ↓
Document
 ↓
Push
 ↓
Deploy when appropriate
 ↓
Complete
```

Small experiments may be abandoned when they have served their learning
purpose, but major projects should be properly finished.

---

## 13. Learn Mathematics Just in Time

Mathematics will not be treated as a separate massive prerequisite.

When a concept requires mathematics:

```text
Encounter concept
    ↓
Identify required math
    ↓
Learn only what is necessary
    ↓
Apply it
```

The goal is practical mathematical understanding relevant to AI
engineering.

---

## 14. Evaluate, Don't Assume

A system working once does not prove that it works well.

Where appropriate, measure:

- Accuracy
- Retrieval quality
- Answer quality
- Groundedness
- Latency
- Cost
- Reliability
- Task completion

Move from:

> "It works."

to:

> "I can demonstrate how well it works."

---

## 15. Build in Public-Quality Standards

Code should be written as if another engineer will eventually read it.

Prioritize:

- Clear structure
- Meaningful names
- Modular design
- Error handling
- Configuration management
- Tests
- Secure secrets
- Useful documentation

---

## 16. Interview Readiness Is a Side Effect of Understanding

I should not memorize interview answers separately from learning.

If I genuinely understand:

```text
Why?
How?
Alternative?
Trade-off?
Failure?
Scale?
```

then I should be able to discuss the project naturally in interviews.
