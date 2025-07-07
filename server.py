import os
import sys
from typing import Any
from educhain import Educhain
from mcp.server.fastmcp import FastMCP

print("✅ EduChain MCP FastMCP server is starting...", file=sys.stderr)

# Set your OpenAI API key (required by Educhain)
os.environ["OPENAI_API_KEY"] = "sk-proj-..."

# Initialize Educhain client and MCP
client = Educhain()
mcp = FastMCP("educhain")

@mcp.tool()
def generate_mcqs(topic: str, num: int = 5) -> dict[str, Any]:
    """Generate multiple-choice questions on a topic."""
    try:
        result = client.qna_engine.generate_questions(topic=topic, num=num)
        return {"questions": result.model_dump()["questions"]}
    except Exception as e:
        return {"error": f"Failed to generate MCQs: {str(e)}"}

@mcp.tool()
def generate_lesson_plan(topic: str) -> dict[str, Any]:
    """Create a detailed lesson plan for a topic."""
    try:
        result = client.content_engine.generate_lesson_plan(topic=topic)
        return {"lesson_plan": result.model_dump()}
    except Exception as e:
        return {"error": f"Failed to generate lesson plan: {str(e)}"}
        
@mcp.tool()
def generate_flashcards(topic: str) -> dict[str, Any]:
    """Create flashcards for a topic."""
    try:
        result = client.content_engine.generate_flashcards(topic=topic)
        return {"flashcards": result.model_dump()}
    except Exception as e:
        return {"error": f"Failed to generate flashcards: {str(e)}"}

if __name__ == "__main__":
    mcp.run(transport="stdio")

