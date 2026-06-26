# State Drift

Over long interactions, an agent's context window can become cluttered with irrelevant tool outputs, causing it to lose track of the original goal.

## Diagram

```mermaid
graph LR
    A[Turn 1: Clear Goal] --> B[Turn 10: Mixed Context]
    B --> C[Turn 20: Irrelevant Focus]
```

[<- Back to Home](../README.md)