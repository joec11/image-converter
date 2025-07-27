# Standard Library Imports
from io import BytesIO
import logging
import os

# Third-Party Library Imports
from fastapi import APIRouter, HTTPException, File, UploadFile, Form
from fastapi.responses import JSONResponse
from PIL import Image

# Initialize the API router
router = APIRouter()

# Route to convert images to the specified format
@router.post("/convert")
async def convert_images(
    file: UploadFile = File(...),
    toFormat: str = Form(...)
):
    """
    Convert images to the specified format.

    Args:
        format_convert (formatConvert): The formatConvert object encapsulated in a Pydantic model.

    Returns:
        JSONResponse: A JSON response containing the query and formatted response.
    """
    try:
        # Log the incoming fromFormat and toFormat formats
        logging.info(f"file: {file.filename}")
        logging.info(f"toFormat: {toFormat}")

        # Read the file asynchronously
        file_contents = await file.read()

        # Convert the in-memory byte data to a file-like object
        image_bytes = BytesIO(file_contents)

        # Name the new file with the previous filename and the new file format
        newFile = f"{os.path.splitext(os.path.basename(file.filename))[0]}.{toFormat}"

        # Open the fromFormat file and save is as the toFormat file
        with Image.open(image_bytes) as img:
            img.save(newFile)

        formatConvert_response = f"Converted {file.filename} to {newFile}"
        logging.info(formatConvert_response)

        response = {
            "formatConvert_response": formatConvert_response
        }
        
        return JSONResponse(content=response, status_code=200)

    except Exception as e:
        # Handle and log unexpected errors
        logging.error(f"An error occurred: {e}")

        return JSONResponse(
            content={
                "formatConvert_response": f"Conversion Failed\n{e}"
            },
        status_code=500)
