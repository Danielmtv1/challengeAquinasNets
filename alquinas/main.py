import uvicorn
from fastapi import FastAPI

from routes.routes import router
from bd.migrations import run_alembic_autogenerate

run_alembic_autogenerate()

app = FastAPI(
        title="Challenge Alquinas",
        description="Alquinas Challenge is an API that "
        "receives a JSON for FBI Api : "
        "and save this information in the bd",
        version="0.0.1"
)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)
