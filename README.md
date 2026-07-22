# ConvoPro — Private, Local ChatGPT Clone

A self-hosted ChatGPT-style chat app that runs entirely on your own machine. No API keys, no
usage bills, no data leaving your network — every model runs locally through Ollama, and every
conversation is stored in your own MongoDB instance.

## Why this project

Most "build your own ChatGPT" tutorials wire straight into a paid cloud API. ConvoPro is the
alternative: a fully private chat assistant with persistent, searchable conversation history,
built for anyone who wants LLM chat without sending their data to a third party.

- **100% local inference** — powered by [Ollama](https://ollama.com), so any model you pull
  (Llama 3, Gemma 2, DeepSeek-R1, etc.) runs on your own hardware.
- **Persistent chat history** — every conversation is saved to MongoDB and reloadable from the
  sidebar, just like ChatGPT's conversation list.
- **Auto-generated chat titles** — the LLM itself summarizes each new conversation into a short,
  catchy title.
- **Multi-model support** — switch between any locally installed Ollama model from a dropdown.
- **Zero cloud cost** — no OpenAI/Anthropic API bill; everything runs on infrastructure you own.

## Tools & tech stack

| Purpose | Tool |
|---|---|
| UI | [Streamlit](https://streamlit.io) |
| LLM orchestration | [LlamaIndex](https://www.llamaindex.ai) |
| Local model runtime | [Ollama](https://ollama.com) |
| Database | [MongoDB](https://www.mongodb.com) via `pymongo` |
| Config management | `pydantic-settings` + `python-dotenv` |
| Language | Python |

## Architecture

```
main.py                  Streamlit UI: chat window, sidebar, model picker
├── services/
│   ├── chat_utilities.py   Builds the chat prompt and calls the LLM
│   ├── get_model_list.py   Reads available Ollama models from config
│   └── get_title.py        Asks the LLM to generate a short chat title
├── llm_factory/
│   └── get_llm.py          Creates and caches the Ollama LLM client
├── db/
│   ├── mongo.py             MongoDB connection
│   └── conversations.py     CRUD for conversations (create, append, list, fetch)
└── config/
    └── settings.py          Typed settings loaded from .env
```

## Getting started

1. Install [Ollama](https://ollama.com) and pull at least one model, e.g.:
   ```bash
   ollama pull gemma2:2b
   ```
2. Start a local MongoDB instance (or point at an existing one).
3. Copy `env_template.txt` to `.env` and fill in your values:
   ```
   MONGO_DB_URL="mongodb://localhost:27017/"
   MONGO_DB_NAME="chat_data"
   OLLAMA_URL="http://localhost:11434"
   OLLAMA_MODELS="gemma2:2b,deepseek-r1:1.5b"
   ```
4. Install dependencies and run:
   ```bash
   pip install -r requirements.txt
   streamlit run main.py
   ```
