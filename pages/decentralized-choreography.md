# Decentralized (Choreography)

Decentralized agents react to events and message queues independently, without a central controller. This architecture is highly scalable and resilient.

## Diagram

```mermaid
graph TD
    A[Message Queue] --> B[Agent 1]
    A --> C[Agent 2]
    B --> A
    C --> A
```

[<- Back to Home](../README.md)