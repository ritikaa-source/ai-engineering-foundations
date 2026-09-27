# AI Engineering Foundations

Hands-on AI engineering practice covering the progression from direct LLM API integration to LangChain, conversation memory, tool calling, agents, and simple AI applications.

> **Learning project:** These exercises were completed as part of AI Engineering learning through Scaler Academy and have been organized and documented here for learning and portfolio purposes.

## Learning Journey

```text
LLM APIs
   ↓
OpenAI-compatible APIs
   ↓
Web Scraping
   ↓
LLM Summarization
   ↓
Gradio AI Applications
   ↓
LangChain
   ↓
Prompt Templates + Output Parsers
   ↓
Conversation Memory
   ↓
Tool Calling
   ↓
Agent Loop
   ↓
AI Chat Application
```

## Repository Structure

### 01 — LLM API & AI Applications
Covers OpenAI/Groq API integration, environment-based configuration, web scraping, website summarization, model comparison, and Gradio interfaces.

See [`01-llm-api-and-ai-apps/README.md`](01-llm-api-and-ai-apps/README.md).

### 02 — LangChain, Memory & Agents
Introduces LangChain pipelines, conversation history, function/tool calling, a basic agent loop, and a Gradio chat application.

See [`02-langchain-memory-and-agents/README.md`](02-langchain-memory-and-agents/README.md).

## Architecture Overview

### Website Summarizer
```text
User URL → Requests → BeautifulSoup → Clean page content → LLM → Markdown summary → Gradio
```

### LangChain Pipeline
```text
Input → ChatPromptTemplate → ChatOpenAI → StrOutputParser → Text output
```

### Tool-Calling Agent
```text
User question → LLM → Tool decision → get_price() → Tool result → LLM → Final response
```

## Setup

```bash
git clone <your-github-repository-url>
cd ai-engineering-foundations
python -m venv .venv
```

Windows PowerShell:
```powershell
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:
```bash
source .venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and add your own credentials. Never commit `.env`.

## Important Notes

- Model names and third-party APIs can change over time; update `.env` if a model is retired.
- These are learning exercises, not production-ready systems.
- The agent uses an in-memory dictionary to demonstrate tool calling.
- Respect website terms, robots directives, rate limits, and applicable laws when adapting the scraper.

## Key Engineering Concepts

- LLM API integration
- OpenAI-compatible APIs
- Prompt engineering
- Environment-based configuration
- Web content extraction
- LLM summarization
- LangChain
- Prompt templates
- Output parsers
- Conversation history
- Function/tool calling
- Agent execution loops
- Gradio AI interfaces

## Portfolio Context

This repository represents foundational AI engineering work in a broader portfolio. More advanced projects build on these concepts with RAG, vector search, event-driven architecture, and agentic AI workflows.

## License

Add the license that matches how you want to distribute this code before publishing publicly.
