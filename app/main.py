from fastapi import FastAPI, HTTPException

from app.db import ping_db

app = FastAPI(title="docqa-agent")


@app.get("/health")
async def health() -> dict[str, str]:
    """Liveness check: the API process is up."""
    return {"status": "ok"}


@app.get("/health/db")
async def health_db() -> dict[str, str]:
    """Readiness check: the database is reachable."""
    try:
        await ping_db()
    except Exception as exc:
        raise HTTPException(status_code=503, detail="database unavailable") from exc
    return {"status": "ok"}