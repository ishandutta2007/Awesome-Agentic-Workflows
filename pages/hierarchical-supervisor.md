# Hierarchical (Router / Supervisor)

A hierarchical structure uses a centralized supervisor agent to evaluate intents, delegate tasks to sub-agents, and aggregate results. This pattern ensures coordinated problem-solving.

## Diagram

```mermaid
graph TD
    A[Manager Agent] --> B[Specialist 1]
    A --> C[Specialist 2]
    B --> A
    C --> A
    A --> D[Final Response]
```

[<- Back to Home](../README.md)