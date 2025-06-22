from fastapi import FastAPI
from converter.router import router as converter_router

app = FastAPI()
app.include_router(converter_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
