# Third-Party Library Imports
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from starlette.requests import Request

# Local Module Imports
from app.dependencies import get_settings
import importlib

# Initialize the API router and settings
router = APIRouter()
settings = get_settings()

# Route to render the Index HTML template
@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """
    Renders the Index HTML template.

    Args:
        request (Request): The HTTP request object.

    Returns:
        HTMLResponse: The rendered Index HTML template.
    """
    templates = importlib.import_module('app.main').templates
    return templates.TemplateResponse(settings.INDEX_HTML, {"request": request})
