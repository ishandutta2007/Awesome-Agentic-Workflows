# Reflection & Fact-Checking Chain

A chain focused on accuracy, where an extractor pulls information, an auditor cross-references laws, and a verifier double-checks for hallucinations.

## Diagram

```mermaid
graph TD
    A[Extractor] --> B[Legal Auditor]
    B --> C[Verifier]
    C -- Hallucination Found --> A
    C -- Verified --> D[Final Output]
```

[<- Back to Home](../README.md)