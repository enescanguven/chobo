import os
import json
import openai
from controller.object_detection_controller import object_detection_controller
from helpers.dalle_helper import DallEHelper

openai.api_key = os.getenv("OPENAI_API_KEY")


class RecipeController():
    def __init__(self) -> None:
        pass

    def create_recipe_from_image(self, image_path):
        print(image_path)
        ingredients = object_detection_controller.get_fridge_contents(image_path)
        prompt = "Sana verdiğim malzeme listesinden bana bir yemek tarifi öner:\n"
        for ingredient in ingredients["ingredients"]:
            prompt += f"- {ingredient}\n"
        prompt += """\nTarifi bu formatta olustur. : {"name": "yemek ismi", "ingredients": ["1 bardak sut", "1 çorba kaşığı un"], "instructions" : " ornek ornek"} \n"""
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system",
                       "content":
                       """Bir aşçı gibi davran. Sana verdiğim malzeme listesinden bana bir yemek tarifi oluştur. Verdiğim listeye sadık kalmaya çalış. Malzemelerin hepsini kullanmak zorunda değilsin. Her evde bulunabilecek malzemeleri de var kabul edebilirsin.Bir aşçı gibi davran. Sana verdiğim malzeme listesinden bana bir yemek tarifi oluştur. Verdiğim listeye sadık kalmaya çalış. Malzemelerin hepsini kullanmak zorunda değilsin. Her evde bulunabilecek malzemeleri de var kabul edebilirsin. Yemeğin adı, içeriği ve yapılışını aşşağıdaki JSON formatinda ver bunun dışında bir şey yazma"""},
                      {"role": "user", "content": prompt}, ])
        response_text = json.loads(response["choices"][0]["message"]["content"])
        dh = DallEHelper(os.getenv("OPENAI_API_KEY"))
        image_path = dh.create_image(response_text["name"])
        print(response_text, image_path)
        return {"recipe": response_text, "image": image_path, "detected_objects": ingredients["ingredients"]}


recipe_controller = RecipeController()
