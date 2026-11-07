# docqa-agent

Document Q&A agent: ask questions about your documents and get answers with sources.

> Work in progress. Features are listed below only when they are implemented.

## Status

- [x] FastAPI service with health checks
- [x] PostgreSQL + pgvector via Docker Compose
- [x] CI: ruff and pytest on GitHub Actions
- [ ] Ingestion: PDF and Markdown parsing, chunking, embeddings
- [ ] Retrieval on pgvector
- [ ] `/ask` endpoint with citations
- [ ] LangGraph agent with tools
- [ ] Evaluation pipeline
- [ ] MCP server

## Quickstart

    cp .env.example .env
    docker compose up --build

Then check the service:

    curl localhost:8000/health
    curl localhost:8000/health/db

## Development

This project uses [uv](https://docs.astral.sh/uv/).

    uv sync
    uv run ruff check .
    uv run pytest
    uv run uvicorn app.main:app --reload

Add a dependency with `uv add <package>` (or `uv add --dev <package>`), and commit `uv.lock`.

## Tech stack

Python, FastAPI, SQLAlchemy (async), Pydantic, PostgreSQL, pgvector, uv, Docker, GitHub Actions