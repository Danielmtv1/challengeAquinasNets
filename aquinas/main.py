import uvicorn
from fastapi import FastAPI
from bd.conect_db import engine, SessionLocal, Base  # noqa
from domain.models.wanted import Wanted # noqa
from routes.routes import router
from bd.migrations import run_alembic_autogenerate

run_alembic_autogenerate()

app = FastAPI(
    title="Alquinas Challenge",
    description="The Alquinas Challenge API fetches data from the FBI API "
                "and stores it in the database.",
    version="0.0.1"
)
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)
