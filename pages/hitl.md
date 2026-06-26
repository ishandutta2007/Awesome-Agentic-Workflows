# Human-in-the-Loop (HITL) Workflows

HITL integrates human oversight at critical junctures. This is essential for high-stakes actions like financial transactions, ensuring safety and compliance.

## Diagram

```mermaid
graph LR
    A[Agent Process] --> B{Hard Breakpoint}
    B -- Requires Approval --> C[Human Operator]
    C -- Approved --> D[Execute Action]
```

[<- Back to Home](../README.md)