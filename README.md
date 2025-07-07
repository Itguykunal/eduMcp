# EduChain MCP Server ✨

This project is a custom [MCP server](https://modelcontextprotocol.io) built using the [Educhain](https://github.com/satvik314/educhain) library. It enables Claude Desktop to dynamically generate educational content using AI.

## 🚀 Features

The server exposes 3 tools to Claude Desktop:

### 1. `generate_mcqs`
Generate multiple-choice questions for any topic.
- **Input**: topic (string), number of questions (default = 5)
- **Output**: A JSON list of MCQs

### 2. `generate_lesson_plan`
Create a detailed lesson plan for a given topic.
- **Input**: topic (string)
- **Output**: Structured plan with objectives, content, and duration

### 3. `generate_flashcards`
Generate study flashcards in Q&A format.
- **Input**: topic (string)
- **Output**: List of question-answer flashcards

## 🧠 How It Works

The server uses:
- `educhain` for content generation
- `FastMCP` from the `mcp` SDK to register tools
- `mcp.run(transport="stdio")` to communicate with Claude Desktop

## 📦 How to Run

1. Clone this repo and navigate to it
2. Install dependencies:
   ```bash
   uv venv
   source .venv/bin/activate
   uv pip install -e /path/to/educhain-main
   uv add "mcp[cli]" httpx
````

3. Run the server:

   ```bash
   uv run server.py
   ```

## 🔌 Claude Desktop Config

In your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "educhain": {
      "command": "uv",
      "args": ["run", "server.py"],
      "cwd": "/Users/kunal/Desktop/educhain"
    }
  }
}
```

## ✅ Example Prompts to Try in Claude

* Generate 3 MCQs on “Photosynthesis” using `generate_mcqs`
* Create a lesson plan on “Newton’s Laws” using `generate_lesson_plan`
* Make flashcards on “Python Basics” using `generate_flashcards`

```

---

## ✅ 2. `Sample_Responses.txt`

```

Prompt: Use the `generate_mcqs` tool to create 3 MCQs on "Photosynthesis"
Response:
Q1: What is the main product of photosynthesis?
A. Oxygen
B. Glucose
C. Carbon dioxide
D. Water
Answer: B

Q2: Which organelle performs photosynthesis?
A. Mitochondria
B. Nucleus
C. Ribosome
D. Chloroplast
Answer: D

---

Prompt: Use the `generate_lesson_plan` tool for "Python Loops"
Response:
{
"lesson\_plan": {
"title": "Python Loops",
"duration": "45 minutes",
"objectives": \["Understand for and while loops", "Use break and continue"],
...
}
}

---

Prompt: Use the `generate_flashcards` tool for "Solar System"
Response:
Q: What is the largest planet in our solar system?
A: Jupiter

Q: Which planet is known as the Red Planet?
A: Mars

````

---

## ✅ 3. `claude_desktop_config.json`

```json
{
  "mcpServers": {
    "educhain": {
      "command": "uv",
      "args": ["run", "server.py"],
      "cwd": "/Users/kunal/Desktop/educhain"
    }
  }
}
````

---

## ✅ 4. GitHub Instructions

Create a repo (e.g., `educhain-mcp`) and push:

```
- server.py
- README.md
- Sample_Responses.txt
- claude_desktop_config.json
```
