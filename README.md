# Jesh Chatbox Python

A unique Python AI chatbox project with a FastAPI backend, a stylish browser UI, and a configurable LLM adapter.

## What makes it good

- polished chat interface instead of a plain terminal bot
- works immediately in `mock` mode without needing an API key
- can connect to any OpenAI-compatible or chat-completions-compatible endpoint later
- clean separation between API routes, AI service logic, frontend assets, and config

## Project structure

```text
jesh-chatbox-python
├── app
│   ├── api
│   ├── services
│   ├── static
│   └── templates
├── tests
├── pyproject.toml
└── README.md
```

## Quick start

1. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -e .[dev]
```

3. Run the app:

```bash
uvicorn app.main:app --reload
```

4. Open the chat UI:

`http://127.0.0.1:8000`

## Optional real AI provider setup

The app defaults to `mock` mode, but you can point it to a real provider:

```bash
export LLM_MODE=remote
export LLM_API_URL=https://your-provider-endpoint
export LLM_API_KEY=your_api_key
export LLM_MODEL=your_model_name
uvicorn app.main:app --reload
```

## Available endpoints

- `GET /`
- `GET /api/health`
- `POST /api/chat`

## Example chat payload

```json
{
  "message": "Help me plan a Python AI portfolio project"
}
```

## Testing

```bash
pytest
```

## Notes

- This repo was scaffolded in an environment that had Python installed.
- Dependency installation and live run were not completed here because package install was not performed in this session.
- The codebase is ready for you to run locally and extend with authentication, chat history, or streaming responses.
