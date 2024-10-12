from fastapi import FastAPI

app = FastAPI(
    docs_url="/"
)


@app.get("/api/v1/users")
async def root():
    return {"message": "Hello World"}