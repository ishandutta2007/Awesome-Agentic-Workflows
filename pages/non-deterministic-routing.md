# Non-Deterministic Routing

The inherent non-determinism of LLMs can cause routers to make inconsistent delegation decisions for identical inputs, complicating reliability.

## Diagram

```mermaid
graph TD
    A[Input X] --> B[Router Agent]
    B -- Run 1 --> C[Sub-agent A]
    B -- Run 2 --> D[Sub-agent B]
```

[<- Back to Home](../README.md)