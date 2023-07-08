from roboflow import Roboflow


class ObjectDetectionController():
    def __init__(self) -> None:
        base_items = ["salt", "pepper"]  # her evde bulunan malzemeleri burada toplayabiliriz
        self.roboflow = Roboflow(api_key="cXvQYarU4cip5KQ73rfJ")  # todo: api key'i env'den al
        self.dictionary = {
            'apple': 'elma', 'banana': 'muz', 'beef': 'biftek', 'blueberries': 'yaban mersini', 'bread': 'ekmek',
            'butter': 'tereyağı', 'carrot': 'havuç', 'cheese': 'peynir', 'chicken': 'tavuk',
            'chicken_breast': 'tavuk göğsü', 'chocolate': 'çikolata', 'corn': 'Mısır', 'eggs': 'yumurtalar',
            'flour': 'un', 'goat_cheese': 'Keçi peyniri', 'green_beans': 'taze fasulye', 'ground_beef': 'dana kıyma',
            'ham': 'jambon', 'heavy_cream': 'yoğun krema', 'lime': 'kireç', 'milk': 'süt', 'mushrooms': 'mantarlar',
            'onion': 'soğan', 'potato': 'patates', 'shrimp': 'karides', 'spinach': 'ıspanak',
            'strawberries': 'çilekler', 'sugar': 'şeker', 'sweet_potato': 'tatlı patates', 'tomato': 'domates'}

        self.project = self.roboflow.workspace().project("aicook-lcv4d")
        self.model = self.project.version(3).model

    def get_fridge_contents(self, image_path):
        predictions = self.model.predict(image_path, confidence=25, overlap=30).json()
        ingredients = list(set([self.dictionary[p['class']] for p in predictions['predictions']]))
        return {"ingredients": ingredients}


object_detection_controller = ObjectDetectionController()
