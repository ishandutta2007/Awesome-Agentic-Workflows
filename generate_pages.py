import os
import re

base_dir = r"C:\Users\ishan\Documents\Projects\Awesome-Agentic-Workflows"
os.makedirs(os.path.join(base_dir, 'pages'), exist_ok=True)

pages_data = [
    {
        "search": r"\*   \*\*Reflection & Self-Correction:\*\* (The agent generates an output.*)",
        "replace": r"*   [**Reflection & Self-Correction:**](pages/reflection-self-correction.md) \1",
        "filename": "reflection-self-correction.md",
        "title": "Reflection & Self-Correction",
        "mermaid": "graph TD\n    A[Generate Output] --> B{Evaluate against Rubric}\n    B -- Needs Improvement --> C[Refine Output]\n    C --> B\n    B -- Passes --> D[Deliver Final Result]",
        "detail": "Reflection and self-correction allow agents to critically analyze their own outputs before finalizing them. This mimics human editing and ensures higher quality and correctness."
    },
    {
        "search": r"\*   \*\*Tool Use \(Function Calling\):\*\* (The agent identifies when it lacks.*)",
        "replace": r"*   [**Tool Use (Function Calling):**](pages/tool-use.md) \1",
        "filename": "tool-use.md",
        "title": "Tool Use (Function Calling)",
        "mermaid": "sequenceDiagram\n    Agent->>Tool: Identify missing info, call Tool\n    Tool-->>Agent: Return data\n    Agent->>User: Provide informed response",
        "detail": "By leveraging external tools, APIs, and code execution environments, agents can overcome the limitations of their pre-trained knowledge base and interact dynamically with the real world."
    },
    {
        "search": r"\*   \*\*Planning \(Decomposition\):\*\* (The agent breaks down a large.*)",
        "replace": r"*   [**Planning (Decomposition):**](pages/planning.md) \1",
        "filename": "planning.md",
        "title": "Planning (Decomposition)",
        "mermaid": "graph TD\n    A[Complex Goal] --> B[Sub-task 1]\n    A --> C[Sub-task 2]\n    A --> D[Sub-task 3]\n    B --> E[Execute and Update Plan]",
        "detail": "Planning involves decomposing high-level, non-deterministic objectives into manageable, step-by-step tasks. Agents can dynamically adjust the plan as they progress and learn new information."
    },
    {
        "search": r"\*   \*\*Multi-Agent Collaboration:\*\* (Splitting a complex workflow.*)",
        "replace": r"*   [**Multi-Agent Collaboration:**](pages/multi-agent-collaboration.md) \1",
        "filename": "multi-agent-collaboration.md",
        "title": "Multi-Agent Collaboration",
        "mermaid": "graph LR\n    A[Writer Agent] <--> B[Critic Agent]\n    A <--> C[Coder Agent]\n    B <--> C",
        "detail": "Collaboration between specialized agents allows for complex problem solving. Distinct personas share context, review each other's work, and bring specialized skills to a joint task."
    },
    {
        "search": r"\*   \*\*Sequential / Linear Chains:\*\* (A deterministic pipeline.*)",
        "replace": r"*   [**Sequential / Linear Chains:**](pages/sequential-chains.md) \1",
        "filename": "sequential-chains.md",
        "title": "Sequential / Linear Chains",
        "mermaid": "graph LR\n    A[Agent A] -->|Structured Output| B[Agent B] -->|Structured Output| C[Agent C]",
        "detail": "Sequential chains offer a highly predictable, deterministic pipeline where outputs from one agent feed directly into the next. Ideal for well-defined, multi-step processing tasks."
    },
    {
        "search": r"\*   \*\*Hierarchical \(Router / Supervisor\):\*\* (A centralized \"Manager\" agent.*)",
        "replace": r"*   [**Hierarchical (Router / Supervisor):**](pages/hierarchical-supervisor.md) \1",
        "filename": "hierarchical-supervisor.md",
        "title": "Hierarchical (Router / Supervisor)",
        "mermaid": "graph TD\n    A[Manager Agent] --> B[Specialist 1]\n    A --> C[Specialist 2]\n    B --> A\n    C --> A\n    A --> D[Final Response]",
        "detail": "A hierarchical structure uses a centralized supervisor agent to evaluate intents, delegate tasks to sub-agents, and aggregate results. This pattern ensures coordinated problem-solving."
    },
    {
        "search": r"\*   \*\*Decentralized \(Choreography\):\*\* (Agents operate independently.*)",
        "replace": r"*   [**Decentralized (Choreography):**](pages/decentralized-choreography.md) \1",
        "filename": "decentralized-choreography.md",
        "title": "Decentralized (Choreography)",
        "mermaid": "graph TD\n    A[Message Queue] --> B[Agent 1]\n    A --> C[Agent 2]\n    B --> A\n    C --> A",
        "detail": "Decentralized agents react to events and message queues independently, without a central controller. This architecture is highly scalable and resilient."
    },
    {
        "search": r"\*   \*\*Human-in-the-Loop \(HITL\) Workflows:\*\* (The agent executes autonomous loops.*)",
        "replace": r"*   [**Human-in-the-Loop (HITL) Workflows:**](pages/hitl.md) \1",
        "filename": "hitl.md",
        "title": "Human-in-the-Loop (HITL) Workflows",
        "mermaid": "graph LR\n    A[Agent Process] --> B{Hard Breakpoint}\n    B -- Requires Approval --> C[Human Operator]\n    C -- Approved --> D[Execute Action]",
        "detail": "HITL integrates human oversight at critical junctures. This is essential for high-stakes actions like financial transactions, ensuring safety and compliance."
    },
    {
        "search": r"\*   \*\*State-Machine Graph Networks:\*\* (Workflows modeled as directed graphs.*)",
        "replace": r"*   [**State-Machine Graph Networks:**](pages/state-machine.md) \1",
        "filename": "state-machine.md",
        "title": "State-Machine Graph Networks",
        "mermaid": "graph TD\n    A[State 1] -->|Condition X| B[State 2]\n    B -->|Condition Y| C[State 3]\n    C -->|Loop Condition| A",
        "detail": "Modeling workflows as state machines provides precise control over transitions, loops, and conditional logic. Frameworks like LangGraph excel in this paradigm."
    },
    {
        "search": r"\*   \*\*Application:\*\* (Autonomous bug fixing, patch generation.*)",
        "replace": r"*   [**Application:**](pages/swe-application.md) \1",
        "filename": "swe-application.md",
        "title": "Software Engineering Application",
        "mermaid": "graph TD\n    A[Issue Created] --> B[Agent Analyzes Repo]\n    B --> C[Agent Creates Patch]\n    C --> D[Tests Run]\n    D --> E[PR Submitted]",
        "detail": "Agentic workflows revolutionize software engineering by autonomously resolving bugs, generating code patches, and performing repository maintenance tasks."
    },
    {
        "search": r"\*   \*\*Workflow Variant:\*\* \*\*Multi-Agent Coding Loop\*\* \((.*)\)",
        "replace": r"*   [**Workflow Variant:**](pages/swe-workflow.md) **Multi-Agent Coding Loop** (\1",
        "filename": "swe-workflow.md",
        "title": "Multi-Agent Coding Loop",
        "mermaid": "graph LR\n    A[Planner] --> B[Coder]\n    B --> C[Executor]\n    C --> D[Critic]\n    D -- Rewrite Request --> B",
        "detail": "This workflow involves multiple specialized agents working together to iteratively write, test, and refine code."
    },
    {
        "search": r"\*   \*\*Framework Examples:\*\* (Devin-style systems.*)",
        "replace": r"*   [**Framework Examples:**](pages/swe-frameworks.md) \1",
        "filename": "swe-frameworks.md",
        "title": "Software Engineering Framework Examples",
        "mermaid": "graph TD\n    A[Frameworks] --> B[Devin-style systems]\n    A --> C[SWE-agent]\n    A --> D[Open-source Coding Workspaces]",
        "detail": "Various frameworks support autonomous coding tasks, ranging from closed-source Devin-style systems to open-source alternatives like SWE-agent."
    },
    {
        "search": r"\*   \*\*Application:\*\* (End-to-end resolution of complex user issues.*)",
        "replace": r"*   [**Application:**](pages/support-application.md) \1",
        "filename": "support-application.md",
        "title": "Customer Support Application",
        "mermaid": "graph TD\n    A[User Request] --> B[Agent Triage]\n    B --> C{Complex Issue?}\n    C -- Yes --> D[Specialized Resolution]\n    C -- No --> E[Quick Reply]",
        "detail": "Agents can resolve complex user issues end-to-end, managing workflows like refunds and account migrations autonomously."
    },
    {
        "search": r"\*   \*\*Workflow Variant:\*\* \*\*Hierarchical Supervisor with Tool Access\*\* \((.*)\)",
        "replace": r"*   [**Workflow Variant:**](pages/support-workflow.md) **Hierarchical Supervisor with Tool Access** (\1",
        "filename": "support-workflow.md",
        "title": "Hierarchical Supervisor with Tool Access",
        "mermaid": "graph TD\n    A[Router] --> B[Specialist 1]\n    A --> C[Specialist 2]\n    B --> D[Database Tool]\n    C --> E[HITL Trigger]",
        "detail": "A hierarchical setup where a router assigns support tickets to specialists equipped with database tools, escalating to humans when necessary."
    },
    {
        "search": r"\*   \*\*Application:\*\* (Synthesizing massive, unstructured web data.*)",
        "replace": r"*   [**Application:**](pages/market-research.md) \1",
        "filename": "market-research.md",
        "title": "Market Research Application",
        "mermaid": "graph TD\n    A[Unstructured Web Data] --> B[Agent Scraper Fleet]\n    B --> C[Data Synthesizer]\n    C --> D[Structured Intelligence Report]",
        "detail": "Agents gather and synthesize immense amounts of unstructured data from the web, converting it into actionable, structured intelligence reports."
    },
    {
        "search": r"\*   \*\*Workflow Variant:\*\* \*\*Parallel Web-Scraping & Synthesizer Teams\*\* \((.*)\)",
        "replace": r"*   [**Workflow Variant:**](pages/market-workflow.md) **Parallel Web-Scraping & Synthesizer Teams** (\1",
        "filename": "market-workflow.md",
        "title": "Parallel Web-Scraping & Synthesizer Teams",
        "mermaid": "graph TD\n    A[Orchestrator] --> B[Search Agent 1]\n    A --> C[Search Agent 2]\n    B --> D[Analyst Agent]\n    C --> D",
        "detail": "Parallel agents handle web scraping, navigating paywalls and pagination, while an analyst agent merges the gathered data."
    },
    {
        "search": r"\*   \*\*Application:\*\* (Clinical trial matching.*)",
        "replace": r"*   [**Application:**](pages/health-legal-application.md) \1",
        "filename": "health-legal-application.md",
        "title": "Healthcare & Legal Application",
        "mermaid": "graph TD\n    A[Patient Data / Contract] --> B[Agent Analysis]\n    B --> C[Compliance Cross-referencing]\n    C --> D[Final Audit Report]",
        "detail": "In high-compliance fields, agents assist with clinical trial matching and auditing contracts against complex regulatory frameworks."
    },
    {
        "search": r"\*   \*\*Workflow Variant:\*\* \*\*Reflection & Fact-Checking Chain\*\* \((.*)\)",
        "replace": r"*   [**Workflow Variant:**](pages/health-legal-workflow.md) **Reflection & Fact-Checking Chain** (\1",
        "filename": "health-legal-workflow.md",
        "title": "Reflection & Fact-Checking Chain",
        "mermaid": "graph TD\n    A[Extractor] --> B[Legal Auditor]\n    B --> C[Verifier]\n    C -- Hallucination Found --> A\n    C -- Verified --> D[Final Output]",
        "detail": "A chain focused on accuracy, where an extractor pulls information, an auditor cross-references laws, and a verifier double-checks for hallucinations."
    },
    {
        "search": r"\*   \*\*Token Loop Cascades:\*\* (Agents getting stuck in infinite loops.*)",
        "replace": r"*   [**Token Loop Cascades:**](pages/token-loop-cascades.md) \1",
        "filename": "token-loop-cascades.md",
        "title": "Token Loop Cascades",
        "mermaid": "graph TD\n    A[Agent Encounters Error] --> B[Agent Attempts Fix]\n    B --> C{Fix Successful?}\n    C -- No --> B\n    B -.-> D[Spiraling API Costs]",
        "detail": "A critical failure mode where agents get caught in infinite loops trying to resolve an error, leading to runaway token consumption and high API costs."
    },
    {
        "search": r"\*   \*\*State Drift:\*\* (As an agent executes 20\+ turns.*)",
        "replace": r"*   [**State Drift:**](pages/state-drift.md) \1",
        "filename": "state-drift.md",
        "title": "State Drift",
        "mermaid": "graph LR\n    A[Turn 1: Clear Goal] --> B[Turn 10: Mixed Context]\n    B --> C[Turn 20: Irrelevant Focus]",
        "detail": "Over long interactions, an agent's context window can become cluttered with irrelevant tool outputs, causing it to lose track of the original goal."
    },
    {
        "search": r"\*   \*\*Non-Deterministic Routing:\*\* (Small shifts in LLM weights.*)",
        "replace": r"*   [**Non-Deterministic Routing:**](pages/non-deterministic-routing.md) \1",
        "filename": "non-deterministic-routing.md",
        "title": "Non-Deterministic Routing",
        "mermaid": "graph TD\n    A[Input X] --> B[Router Agent]\n    B -- Run 1 --> C[Sub-agent A]\n    B -- Run 2 --> D[Sub-agent B]",
        "detail": "The inherent non-determinism of LLMs can cause routers to make inconsistent delegation decisions for identical inputs, complicating reliability."
    }
]

# Write markdown files
for page in pages_data:
    filepath = os.path.join(base_dir, 'pages', page['filename'])
    content = f"# {page['title']}\n\n{page['detail']}\n\n## Diagram\n\n```mermaid\n{page['mermaid']}\n```\n\n[<- Back to Home](../README.md)"
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Update README.md
readme_path = os.path.join(base_dir, 'README.md')
with open(readme_path, 'r', encoding='utf-8') as f:
    readme_content = f.read()

for page in pages_data:
    readme_content = re.sub(page['search'], page['replace'], readme_content, count=1)

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(readme_content)

print("Pages generated and README updated successfully.")
