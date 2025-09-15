from fastapi import FastAPI
from api.v1 import all_routers

app = FastAPI(
    title="Geometry API",
    description="An API for drawing geometric shapes.",
    version="1.0.0",
)

for router in all_routers:
    app.include_router(router)


@app.get("/", tags=["General"])
async def root():
    return {"message": "Welcome to the Geometry API! Visit /docs for documentation."}

@app.get("/health", tags=["General"])
def health_check():
    return {"status": "ok"}
