# Tool Use (Function Calling)

By leveraging external tools, APIs, and code execution environments, agents can overcome the limitations of their pre-trained knowledge base and interact dynamically with the real world.

## Diagram

```mermaid
sequenceDiagram
    Agent->>Tool: Identify missing info, call Tool
    Tool-->>Agent: Return data
    Agent->>User: Provide informed response
```

[<- Back to Home](../README.md)