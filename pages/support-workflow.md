# Hierarchical Supervisor with Tool Access

A hierarchical setup where a router assigns support tickets to specialists equipped with database tools, escalating to humans when necessary.

## Diagram

```mermaid
graph TD
    A[Router] --> B[Specialist 1]
    A --> C[Specialist 2]
    B --> D[Database Tool]
    C --> E[HITL Trigger]
```

[<- Back to Home](../README.md)