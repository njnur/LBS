from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
# from src.api.dependencies import get_query_token, get_token_header
# from src.api.routes import pois, users
from src.db.mongodb import connect_to_mongo, close_mongo_connection
from src.core.config import settings


# Initialize the FastAPI app
app = FastAPI(
    title="Location-Based Service API",
    description="An API for managing and querying Points of Interest and User Locations.",
    version="1.0.0",
)

# Middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Event handlers for database connection
@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()


@app.on_event("shutdown")
async def shutdown_event():
    await close_mongo_connection()


# Exception handling
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )


# Dependency injection for specific routes
# app.include_router(
#     pois.router,
#     prefix="/pois",
#     tags=["pois"],
#     dependencies=[Depends(get_token_header)],
#     responses={404: {"description": "Not found"}},
# )
#
# app.include_router(
#     users.router,
#     prefix="/users",
#     tags=["users"],
#     dependencies=[Depends(get_query_token)],
# )


# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the Location-Based Service API"}

# Additional advanced routes and functionalities can be added here

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
