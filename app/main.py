# FastAPI imports
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

# Local imports
from app.shared import logging
from app.routers import ui_routes, image_converter_routes

# Create an instance of FastAPI with configuration parameters
app = FastAPI(
    root_path="/api",
    title="FastAPI with Image Converter",
    version="0.0.1",
    contact={
        "name": "API Support",
        "url": "https://github.com/joec11/image_converter",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT"
    },
)

# Configure CORS middleware to allow requests from specified origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this to match your frontend app's URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Event handler for application startup
@app.on_event("startup")
async def startup_event():
    """
    Event handler for application startup.

    Logs the startup event.
    """
    logging.info("FastAPI application starting up.")

# Event handler for application shutdown
@app.on_event("shutdown")
async def shutdown_event():
    """
    Event handler for application shutdown.

    Logs the shutdown event.
    """

    logging.info("FastAPI application shutting down.")

# Include router for the User Interface routes
app.include_router(ui_routes.router)

# Include router for the Image Converter routes
app.include_router(image_converter_routes.router)
