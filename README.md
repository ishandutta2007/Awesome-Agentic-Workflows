<div align="center">
  <img src="assets/banner.svg" alt="Awesome Agentic Workflows Banner" width="800" />
</div>

<div align="center">
  <a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>
  <a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>
</div>

# ✨ Awesome-Agentic-Workflows ✨

**Keywords**: *Agentic Workflows, AI Agents, LLM Orchestration, Autonomous Systems, Multi-Agent Systems, GenAI*

## 🤖 The Agentic Workflows Map

> **A comprehensive reference guide for Agentic Workflows—architectural patterns, orchestration variants, design patterns, and real-world industrial deployments.**

Unlike traditional linear LLM pipelines (Prompt → Completion), Agentic Workflows give language models iterative control over execution loops, reasoning paths, tool usage, and self-correction. This repository acts as a taxonomy for building autonomous, resilient, and multi-agent systems.

---

## 🏗️ Core Architectural Design Patterns

The fundamental building blocks used to design autonomous workflows. Most complex agent systems combine multiple patterns from this list.

*   [**Reflection & Self-Correction:**](pages/reflection-self-correction.md) The agent generates an output, evaluates its own work against a rubric or test suite, and refines it iteratively before delivering the final result.
*   [**Tool Use (Function Calling):**](pages/tool-use.md) The agent identifies when it lacks information or capability, constructs parameters, executes external APIs/code execution environments, and ingests the response.
*   [**Planning (Decomposition):**](pages/planning.md) The agent breaks down a large, non-deterministic goal into a structured sequence of sub-tasks, executing them sequentially or dynamically updating the plan.
*   [**Multi-Agent Collaboration:**](pages/multi-agent-collaboration.md) Splitting a complex workflow into distinct personas or specialized agents (e.g., Writer, Critic, Coder) that interact, share a context window, and review each other's work.

---

## 🎛️ Orchestration & Topology Variants

How agents are structured, connected, and allowed to communicate within a computing infrastructure.

*   [**Sequential / Linear Chains:**](pages/sequential-chains.md) A deterministic pipeline where Agent A passes its structured output directly to Agent B. High predictability, low autonomy.
*   [**Hierarchical (Router / Supervisor):**](pages/hierarchical-supervisor.md) A centralized "Manager" agent evaluates user intent, delegates specific tasks to specialized sub-agents, aggregates their findings, and responds.
*   [**Decentralized (Choreography):**](pages/decentralized-choreography.md) Agents operate independently in a network or event-driven architecture, reacting to message queues or state changes without a central controller.
*   [**Human-in-the-Loop (HITL) Workflows:**](pages/hitl.md) The agent executes autonomous loops but hits hard breakpoints requiring human approval, feedback, or overriding authority (e.g., for financial transactions or code deployment).
*   [**State-Machine Graph Networks:**](pages/state-machine.md) Workflows modeled as directed graphs (nodes as agents/tools, edges as conditional transitions). Offers precise control over cycles and loops.

---

## 🚀 Real-World Applications by Domain

Where and how agentic workflows are replacing static automation in production.

### 💻 Software Engineering & DevOps
*   [**Application:**](pages/swe-application.md) Autonomous bug fixing, patch generation, and repository maintenance.
*   [**Workflow Variant:**](pages/swe-workflow.md) **Multi-Agent Coding Loop** (Planner agent outlines changes $\rightarrow$ Coder agent modifies files $\rightarrow$ Executor runs test suite $\rightarrow$ Critic agent analyzes stack traces and forces rewrites.
*   [**Framework Examples:**](pages/swe-frameworks.md) Devin-style systems, SWE-agent, open-source coding workspaces.

### 🎨 Enterprise Customer Support
*   [**Application:**](pages/support-application.md) End-to-end resolution of complex user issues (e.g., handling refunds, account migrations, and multi-step troubleshooting).
*   [**Workflow Variant:**](pages/support-workflow.md) **Hierarchical Supervisor with Tool Access** (Router triages sentiment $\rightarrow$ Specialist reads database schema $\rightarrow$ HITL triggers if refund exceeds a dollar threshold.

### 📊 Market Research & Data Analytics
*   [**Application:**](pages/market-research.md) Synthesizing massive, unstructured web data into structured competitive intelligence reports.
*   [**Workflow Variant:**](pages/market-workflow.md) **Parallel Web-Scraping & Synthesizer Teams** (Orchestrator spawns 5 parallel search agents $\rightarrow$ Each agent dynamically handles pagination/paywalls $\rightarrow$ Analyst agent merges data and filters contradictions.

### 💊 Healthcare & Legal Document Review
*   [**Application:**](pages/health-legal-application.md) Clinical trial matching, regulatory compliance cross-referencing, and contract auditing.
*   [**Workflow Variant:**](pages/health-legal-workflow.md) **Reflection & Fact-Checking Chain** (Extractor pulls contract clauses $\rightarrow$ Legal Auditor cross-references local laws $\rightarrow$ Verifier flags hallucinations back to Extractor.

---

## 🛠️ The Agentic Tooling Ecosystem

The industry-standard software frameworks used to orchestrate these workflows.

| Framework | Core Paradigm / Strength | Ideal For |
| :--- | :--- | :--- |
| **LangGraph** | Cyclic Graph-based state machines | Highly controllable loops and complex state management |
| **CrewAI** | Role-based, pragmatic multi-agent systems | Production-ready business process automation |
| **AutoGen** | Conversational, event-driven multi-agent chat | Highly autonomous, exploratory multi-agent interaction |
| **LlamaIndex Workflows**| Event-driven, data-centric agent routing | Advanced RAG and complex document-processing agents |

---

## ⚠️ Key Engineering Challenges in Agentic Systems

*   [**Token Loop Cascades:**](pages/token-loop-cascades.md) Agents getting stuck in infinite loops trying to solve an unresolvable error, exponentially scaling API billing costs.
*   [**State Drift:**](pages/state-drift.md) As an agent executes 20+ turns, the context window accumulates irrelevant tool outputs, causing the model to forget the original goal.
*   [**Non-Deterministic Routing:**](pages/non-deterministic-routing.md) Small shifts in LLM weights or prompt sensitivity can cause the routing agent to choose completely different downstream sub-agents for identical inputs.


## 🌟 Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007/Awesome-Agentic-Workflows&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Agentic-Workflows&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Agentic-Workflows&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Agentic-Workflows&type=date&legend=bottom-right" />
</picture>
</a>
</div>
