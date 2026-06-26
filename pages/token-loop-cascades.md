# Token Loop Cascades

A critical failure mode where agents get caught in infinite loops trying to resolve an error, leading to runaway token consumption and high API costs.

## Diagram

```mermaid
graph TD
    A[Agent Encounters Error] --> B[Agent Attempts Fix]
    B --> C{Fix Successful?}
    C -- No --> B
    B -.-> D[Spiraling API Costs]
```

[<- Back to Home](../README.md)