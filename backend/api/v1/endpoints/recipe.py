from helpers.settings import settings
from fastapi import APIRouter, File, UploadFile
from fastapi.responses import FileResponse

from models.user import *
from PIL import Image
from controller.recipe_controller import recipe_controller

router = APIRouter()


@router.post("/fromImage")
async def create_recipe_from_fridge_image(file: UploadFile = File(...)):
    with open(f"uploads/{file.filename}", "wb") as buffer:
        content = await file.read()
        buffer.write(content)
    image = Image.open(f"uploads/{file.filename}")
    image.save(f"uploads/{file.filename}")
    image_path = f"uploads/{file.filename}"

    return recipe_controller.create_recipe_from_image(image_path)


@router.post("/fromPromptText")
def create_recipe_from_prompt_text():
    pass
