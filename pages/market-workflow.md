# Parallel Web-Scraping & Synthesizer Teams

Parallel agents handle web scraping, navigating paywalls and pagination, while an analyst agent merges the gathered data.

## Diagram

```mermaid
graph TD
    A[Orchestrator] --> B[Search Agent 1]
    A --> C[Search Agent 2]
    B --> D[Analyst Agent]
    C --> D
```

[<- Back to Home](../README.md)