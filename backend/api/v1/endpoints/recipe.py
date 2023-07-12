import json
from helpers.settings import settings
from fastapi import APIRouter, File, UploadFile, Request
from fastapi.responses import FileResponse

from models.user import *
from PIL import Image
from controller.recipe_controller import recipe_controller
from controller.voice_recognition_controller import voice_recognition_controller

router = APIRouter()


@router.post("/fromImageOld")
async def create_recipe_from_fridge_image(file: UploadFile = File(...)):
    with open(f"uploads/{file.filename}", "wb") as buffer:
        content = await file.read()
        buffer.write(content)
    image = Image.open(f"uploads/{file.filename}")
    image.save(f"uploads/{file.filename}")
    image_path = f"uploads/{file.filename}"

    return recipe_controller.create_recipe_from_image(image_path)

@router.post("/fromImage")
async def test_func(request: Request):
    form_data = await request.form()
    choices = json.loads(form_data["choices"])

    with open(f"uploads/{form_data['file'].filename}", "wb") as buffer:
        content = await form_data["file"].read()
        buffer.write(content)
    image = Image.open(f"uploads/{form_data['file'].filename}")
    image.save(f"uploads/{form_data['file'].filename}")
    image_path = f"uploads/{form_data['file'].filename}"

    return recipe_controller.create_recipe_from_image(image_path, choices)

@router.post("/fromVoice")
async def test_func(request: Request):
    form_data = await request.form()
    # choices = json.loads(form_data["choices"])

    with open(f"uploads/{form_data['file'].filename}", "wb") as buffer:
        content = await form_data["file"].read()
        buffer.write(content)

    transcript = await voice_recognition_controller.get_transcript(f"uploads/{form_data['file'].filename}")
    result = recipe_controller.create_recipe_from_prompt_text(transcript)
    print(result)
    return result


@router.post("/fromPromptText")
def create_recipe_from_prompt_text():
    pass

@router.get("/image/{image_path}")
def get_image(image_path):
    return FileResponse(f"covers/{image_path}")