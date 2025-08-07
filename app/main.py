from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI(title="Flipping")


@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url="/docs")
