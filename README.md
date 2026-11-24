# 🧠 AI Multi-Agent Software Engineering Tutorial

This tutorial teaches you how to use a multi-agent LLM system (powered by OpenHands) to:

- Generate specifications  
- Generate pytest tests  
- Implement Python code  
- Generate review reports  
- Maintain full traceability across SPEC → TEST → CODE → REVIEW  

You will interact with the system through a CLI menu in `my_agents.py`.

---
# 🤖 What Is OpenHands?

OpenHands is an **agentic framework** that enables LLMs to operate as structured software-development agents.  
It provides controlled tool usage (file editing, terminal execution, reasoning loops) inside a reproducible sandbox.

OpenHands comes in *multiple* forms, depending on how you want to use it:

### 🖥️ 1. OpenHands Desktop GUI (Full Development Environment)
- A full graphical environment where an AI agent edits your repository.
- Includes a browser-based VS Code interface.
- Best for manual experiments or interactive agent development.

### ☁️ 2. OpenHands Cloud (Hosted)
- A managed online environment that runs agents remotely.
- Useful when you need GPU acceleration or shared workspaces.
- Same agent capabilities, but running in the cloud.

### 🧩 3. OpenHands SDK (Programmatic / Library Mode)
- A Python library (`openhands-sdk`, `openhands-tools`, `openhands-workspace`)
- Allows you to **embed OpenHands agents into your own application**.
- You define the agents, prompts, tools, and workflow.
- Agents run inside a sandboxed workspace, fully controlled by your code.

👉 **This tutorial uses the SDK version.**

You are not opening the GUI.  
You are not connecting to the cloud.

Instead, the project integrates OpenHands **directly into Python code**. 

---

# 🤖 What Are Agentic Systems?

Agentic systems extend LLMs beyond chat responses by giving them:

- **Tools** (file editor, terminal, workspace)  
- **Role-specific instructions**  
- **Persistent context**  
- **Structured multi-step execution**  

Instead of returning text, agents can:

- Read/write files  
- Modify code  
- Run pytest  
- Inspect the workspace  
- Produce review reports  

This enables full automation of software engineering workflows.

---

# 📁 Project Structure Overview

This project has a series of agents to support the development of a calculator project. Your repository has the following architecture:

```
workspace/
│
├── docs/                  # Project-wide prompt
├── reviews/               # Reviewer-generated code reviews
├── specs/                 # Analyst-generated specifications
├── src/                   # Coder-generated Python implementation
├── tests/                 # Tester-generated pytest tests
│
├── agents/
│   ├── analyst.*
│   ├── tester.*
│   ├── coder.*
│   └── reviewer.*
│
├── requirements.txt       # CLI interface
├── my_agents.py           # CLI interface
└── Dockerfile             # Execution environment
```

The entire pipeline forms an iterative loop:

```
SPEC → TESTS → CODE → REVIEW → (repeat)
```

---

# 🟦 1st Step — Explore the Already-Implemented “Add” Feature

Before using any agents, explore the **existing Add functionality** of the calculator program.

You will find:

```
specs/ft-add.md            → Analyst-created specification
tests/add/                 → Tester-generated test suite
src/calculator.py          → Coder’s implementation
reviews/rv-add.md          → Reviewer’s analysis (if present)
```

Open these files and observe how they relate:

1. **Specification** defines Acceptance Criteria  
2. **Tester** generates one test file per AC  
3. **Coder** implements code until tests pass  
4. **Reviewer** analyzes the entire chain and generates traceability

This is the blueprint for all features you will develop.

---

# ⚙️ Configuring the `.env` File

The multi-agent system requires a `.env` file so the agents know **which LLM to call**, **where the API is hosted**, and **how to communicate with your remote LLM (e.g., ChatGPT or Ollama server)**.

You must create a `.env` file in the **project root** with the following structure (use the one provided to you).

---

# 🐳 1. Running the Project Inside Docker

OpenHands requires a controlled reproducible environment, so everything is run in Docker.

## ✔ 1.1 Build the Docker image
On root of the project run this. This will create a new image based on the Dockerfile with the OpenHands SDK.

```
docker build -t ai-se-agents .
```

## ✔ 1.2 Run the container

This mounts your project directory as `/workspace`. This will create a volume that shares your project (so you can edit your code with your favorite IDE) and we then execute the code through a terminal to the container. **Run this in the root folder of the project.**

```
docker run -it --rm \
  -v "$(pwd)":/workspace \
  -w /workspace \
  ai-se-agents bash
```

You will now be inside the isolated development environment. You will run your code from here! i.e., **python my_agents.py**

---

# ▶️ 2. Start the Multi-Agent Application

Inside the container:

```
python my_agents.py
```

You will see:

```
==============================================
  AI Multi-Agent Development Application
==============================================
Active Spec: None selected
----------------------------------------------
1) Choose active specification
2) Generate or update a specification (Analyst)
3) Generate or replace tests (Developer Tests)
4) Implement or update code (Developer Code)
5) Review implementation and tests (Reviewer)
6) Exit
----------------------------------------------
```

---

# 🧪 3. Warm-Up Task: Subtraction Feature (Included)

Your repository already contains:

```
specs/ft-subtract.md
```

Your job:

1. Select the spec  
2. Generate tests  
3. Implement code  
4. Generate a review  

Let’s go step-by-step.

---

# Step 1 — Select the subtraction spec

Start the app:

```
python my_agents.py
```

Choose:

```
1) Choose active specification
```

Select:

```
ft-subtract.md
```

---

# Step 2 — Generate tests for subtraction

Choose:

```
3) Generate or replace tests (Developer Tests)
```

This creates:

```
tests/subtract/
```

with test files:

```
ac_01_*.py
ac_02_*.py
...
ac_05_*.py
```

Each test corresponds to one Acceptance Criterion.

---

# Step 3 — Implement subtraction

Choose:

```
4) Implement or update code (Developer Code)
```

The Coder agent:

- Reads the tests  
- Reads the spec  
- Modifies only `src/calculator.py`  
- Runs pytest  
- Repeats until **all tests pass**  

---

# Step 4 — Generate a review

Choose:

```
5) Review implementation and tests (Reviewer)
```

This produces:

```
reviews/rv-subtract.md
```

The review includes:

- Summary  
- Issues & risks  
- Alignment with specification  
- A full traceability matrix  
- Recommendations  

---

# 🧮 4. Student Task: Add Multiplication Functionality

Now you repeat the entire flow yourself.

## 4.1 Use the Analyst to generate a spec

Choose:

```
2) Generate or update a specification (Analyst)
```

Example input:

```
Create a full software specification for adding multiplication functionality to the Calculator class. Include functional requirements, acceptance criteria, inputs/outputs, and edge cases.
```

A file will be created:

```
specs/ft-multiply.md
```

## 4.2 Select the new specification

```
1) Choose active specification
```

Pick:

```
ft-multiply.md
```

## 4.3 Generate tests

```
3) Generate or replace tests (Developer Tests)
```

Produces:

```
tests/multiply/
```

## 4.4 Implement code

```
4) Implement or update code (Developer Code)
```

Coder modifies:

```
src/calculator.py
```

until all tests pass.

## 4.5 Generate review

```
5) Review implementation and tests (Reviewer)
```

Review appears under:

```
reviews/rv-multiply.md
```

---

# ➗ 5. Student Task: Implement Division

Repeat the exact same workflow:

- Generate the division specification  
- Activate it  
- Generate tests  
- Implement code  
- Generate a reviewer report  
- Compare the traceability matrix with previous features  

---

# 📘 6. What You Should Observe

As you complete each feature, pay attention to:

### 🧩 Analyst
- How clear the functional requirements are  
- How acceptance criteria are structured  

### 🧪 Tester
- How ACs turn into files  
- How one AC becomes one pytest file  

### 🧑‍💻 Coder
- How code evolves to satisfy tests  
- No code is ever written without tests  

### 📝 Reviewer
- Completeness of test coverage  
- Whether code truly matches the spec  
- The traceability matrix linking AC → Test → Code  

---

# 🔧 Optional Extension: Adding a Repo Manager Agent

This section introduces an optional advanced task for students:  
**designing a new “Repo Manager Agent” responsible for repository maintenance.**

This teaches:
- Separation of responsibilities between agents  
- Safe automation of version control  
- Git workflows in multi-agent systems  
- How LLM agents can support DevOps tasks  
- How to create new agent prompts and integrate them into the application  

---

## 🧠 Why Add a Repo Agent?

Currently your system has:

- Analyst → writes specifications  
- Tester → generates tests  
- Coder → writes source code  
- Reviewer → evaluates quality  

But **no agent manages the repository**, meaning commits, diffs, and tagging must be done manually.

A Repo Manager Agent provides structure and repeatability.

---

## 🎯 Goal of the Repo Manager Agent

The new agent should:

- Stage modified files  
- Commit them with a clean, structured commit message  
- Show diffs on request  
- Never modify code, tests, or specs  
- Only perform repository management tasks  

This mirrors real-world DevOps and multi-agent coding workflows.

---

# ✅ End of Tutorial

You now understand the complete multi-agent SE workflow powered by LLMs:

```
SPECIFICATION → TESTS → IMPLEMENTATION → REVIEW → TRACEABILITY
```

This pipeline enforces:

- High-quality specifications  
- Automated, deterministic test generation  
- Correct-by-construction implementation  
- Auditable traceability  
- Rigorous software engineering discipline  

Happy coding!  
