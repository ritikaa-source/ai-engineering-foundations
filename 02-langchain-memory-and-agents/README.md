# 02 — LangChain, Memory & Agents

This module builds on LLM fundamentals and introduces LangChain pipelines, conversation history, function/tool calling, and a small agent-based application.

> **Learning project:** These exercises were completed as part of AI Engineering learning through Scaler Academy.

| File | Purpose |
|---|---|
| `scraper.py` | URL → readable page content |
| `summarizer_langchain.py` | Prompt → model → output parser |
| `memory_demo.py` | Conversation history supplied explicitly |
| `memory_chat.py` | Conversation history built dynamically |
| `agent.py` | LLM + tool + execution loop |
| `app.py` | Gradio chat UI over the agent |
| `ai_engineering_langchain.html` | Interactive/reference learning page |

## Run

```bash
python summarizer_langchain.py
python memory_demo.py
python memory_chat.py
python agent.py
python app.py
```

## Agent Flow

```text
User → LLM → Tool decision → get_price() → Tool result → LLM → Final response
```

The example intentionally uses a small in-memory price dictionary. It demonstrates tool-calling mechanics rather than production agent infrastructure.

## Concepts

LangChain · ChatPromptTemplate · MessagesPlaceholder · output parsers · conversation history · function/tool calling · agent loops · Gradio ChatInterface

##############################################

AI Engineering - LangChain & Your First Agent (runnable code)
Every file here matches a code block from the Class 2 deck. They are self-contained — run any one of them directly.

One-time setup
# 1. create & activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. install everything
pip install -r requirements.txt

# 3. add your key
#    copy .env.example to a file named .env, then paste your OpenAI key inside
cp .env.example .env            # Windows: copy .env.example .env
Get a key at https://platform.openai.com/api-keys (add a little billing credit).

What to run (in deck order)
## Files and How to Run

| # | File                      | What it demonstrates                                                                             | Run                              |
| - | ------------------------- | ------------------------------------------------------------------------------------------------ | -------------------------------- |
| 1 | `scraper.py`              | Class 1 helper — extracts page text from a URL                                                   | `python scraper.py`              |
| 2 | `summarizer_langchain.py` | Block 10 — rebuilds the summarizer using LangChain: **Prompt → Model → Output Parser**           | `python summarizer_langchain.py` |
| 3 | `memory_demo.py`          | Block 10 — demonstrates conversation memory with message history entered manually                | `python memory_demo.py`          |
| 4 | `memory_chat.py`          | Block 10 — demonstrates conversation memory that builds automatically during a chat loop         | `python memory_chat.py`          |
| 5 | `agent.py`                | Block 11 — demonstrates a first tool-using AI agent                                              | `python agent.py`                |
| 6 | `app.py`                  | Block 12 — runs the tool-using agent through a Gradio chat UI and can create a public share link | `python app.py`                  |


Notes
1. All files use the cheap gpt-4o-mini model.
2. summarizer_langchain.py imports fetch_website_contents from scraper.py, so keep them in the same folder.
3. app.py imports agent from agent.py — same folder.
4. Never commit .env. A .gitignore is included that already ignores it.
5. Stop a running app
6. Press Ctrl + C in the terminal.