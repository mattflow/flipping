from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from .tasks import add as add_task

app = FastAPI(title="Flipping")


@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url="/docs")


@app.get("/add")
async def add(x: int, y: int):
    result = add_task.delay(x, y)
    return {
        "task_id": result.id,
        "status": "Task submitted",
        "result": result.get(timeout=3),
    }
