# Reflection & Self-Correction

Reflection and self-correction allow agents to critically analyze their own outputs before finalizing them. This mimics human editing and ensures higher quality and correctness.

## Diagram

```mermaid
graph TD
    A[Generate Output] --> B{Evaluate against Rubric}
    B -- Needs Improvement --> C[Refine Output]
    C --> B
    B -- Passes --> D[Deliver Final Result]
```

[<- Back to Home](../README.md)