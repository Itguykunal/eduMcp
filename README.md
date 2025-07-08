# 📚 EduChain MCP Server for Claude Desktop

This project is an AI-powered **MCP (Model Context Protocol) server** built using the [EduChain](https://github.com/satvik314/educhain) library. It integrates with **Claude Desktop** and provides tools to generate educational content such as:

- ✅ Multiple Choice Questions (MCQs)
- ✅ Lesson Plans
- ✅ Flashcards

---

## ⚙️ Features

| Tool | Description |
|------|-------------|
| `generate_mcqs` | Generates multiple-choice questions based on a topic |
| `generate_lesson_plan` | Creates a structured lesson plan |
| `generate_flashcards` | Creates Q&A flashcards for study |

---

## 🚀 Setup Instructions

> These steps will guide you through installing everything and running the server with Claude Desktop.

---

### 🧰 Step 1: Install `uv` (if not already)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
````

---

### 🐍 Step 2: Create and activate a virtual environment

```bash
uv venv
source .venv/bin/activate
```

---

### 📦 Step 3: Install EduChain (from local GitHub repo)

```bash
uv pip install -e /absolute/path/to/educhain-main
```
If you haven’t already, first clone the [EduChain GitHub repository](https://github.com/satvik314/educhain):
then follow step 3
> Example:
>
> ```bash
> uv pip install -e /Users/kunal/Desktop/github/educhain-main
> ```

---

### 📦 Step 4: Install MCP + httpx

```bash
uv add "mcp[cli]" httpx
```

---

### 🧠 Step 5: Add Your API Key in `server.py`

In `server.py`, replace this line with your actual key:

```python
os.environ["OPENAI_API_KEY"] = "sk-..."  # ← Your OpenAI API key here
```

> ⚠️ This is not recommended for production but acceptable for testing/submission.

---

## ▶️ Running the Server

Make sure you're in the project folder and the virtual environment is activated.

Then run:

```bash
uv run server.py
```

If successful, you'll see:

```
✅ EduChain MCP FastMCP server is starting...
```

---

## 💻 Claude Desktop Configuration

Update your `claude_desktop_config.json` like this:

```json
{
  "mcpServers": {
    "educhain": {
      "command": "uv",
      "args": [
        "--directory",
        "/ABSOLUTE/PATH/TO/PARENT/FOLDER/eduMcp",
        "run",
        "server.py"
      ]
    }
  }
}
```

Restart Claude Desktop to reload the config.

---

## 💬 Example Prompts in Claude

```text
Use the `generate_mcqs` tool to create 3 questions on "Photosynthesis".

Use the `generate_lesson_plan` tool for "Newton's Laws of Motion".

Use the `generate_flashcards` tool to make flashcards on "The Solar System".
```

Made using [EduChain](https://github.com/satvik314/educhain) + Claude.
