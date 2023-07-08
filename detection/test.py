from roboflow import Roboflow
rf = Roboflow(api_key="cXvQYarU4cip5KQ73rfJ")

project = rf.workspace().project("aicook-lcv4d")
model = project.version(3).model

predictions = model.predict("dolap_1.jpeg", confidence=25, overlap=30).json()
dictionary = {'apple': 'elma', 'banana': 'muz', 'beef': 'biftek', 'blueberries': 'yaban mersini', 'bread': 'ekmek', 'butter': 'tereyağı', 'carrot': 'havuç', 'cheese': 'peynir', 'chicken': 'tavuk', 'chicken_breast': 'tavuk göğsü', 'chocolate': 'çikolata', 'corn': 'Mısır', 'eggs': 'yumurtalar', 'flour': 'un', 'goat_cheese': 'Keçi peyniri', 'green_beans': 'taze fasulye', 'ground_beef': 'dana kıyma', 'ham': 'jambon', 'heavy_cream': 'yoğun krema', 'lime': 'kireç', 'milk': 'süt', 'mushrooms': 'mantarlar', 'onion': 'soğan', 'potato': 'patates', 'shrimp': 'karides', 'spinach': 'ıspanak', 'strawberries': 'çilekler', 'sugar': 'şeker', 'sweet_potato': 'tatlı patates', 'tomato': 'domates'}
ingredients = list(set([dictionary[p['class']] for p in predictions['predictions']]))
print(ingredients)