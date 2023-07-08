
from PIL import Image, ImageDraw, ImageFont
import csv
import random
import json

template_json = open("./templates/templates.json")
template_json = json.load(template_json)


def trans_paste(fg_img,bg_img,alpha=1.0,box=(0,0)):
    fg_img_trans = Image.new("RGBA",fg_img.size)
    fg_img_trans = Image.blend(fg_img_trans,fg_img,alpha)
    bg_img.paste(fg_img_trans,box,fg_img_trans)
    return bg_img

def generate_story(name, ingridients, instructions, image_path):

    temp_nu = random.randint(0, 0)    
    story_temp = "./templates/"+str(temp_nu)+".png"
    specs = template_json[str(temp_nu)]
    font_path = "templates/fonts/"

    img = Image.open(story_temp, mode='r')
    image_width = img.width
    image_height = img.height
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path+specs["title_font"], size=specs["title_font_size"])
    text_width, _ = draw.textsize(name, font=font)
    
    food_img = Image.open(image_path, mode='r')
    food_img = food_img.resize((specs['food_img_width'], specs['food_img_height']))
    food_img.show()
    draw.text( ( specs['title_x'], specs['title_y'] ), name, fill=tuple(specs['font_color']), stroke_width=1, font=font)
    
    img = trans_paste(food_img,img,1,(specs['food_img_x'],specs['food_img_y']))
    print(font_path+specs["ingredients_font"])
    font = ImageFont.truetype(font_path+specs["ingredients_font"], size=specs["ingredients_font_size"])
    # draw.text( ( specs['ingredients_x'], specs['ingredients_y'] ), ingredients, fill=tuple(specs['font_color']), stroke_width=1, font=font)        
    draw.text( ( specs['ingredients_x'], specs['ingredients_y'] ), "\n".join(ingridients), fill=tuple(specs['font_color']), stroke_width=1, font=font)
    img.show()



# Driver Code
if __name__ == "__main__":

    name = "Muzlu Peynirli Mini Kekler"
    ingredients = ["1 su bardağı un", "1 su bardağı toz şeker", "1 su bardağı süt", "1 su bardağı sıvı yağ", "3 adet yumurta", "1 paket kabartma tozu", "1 paket vanilya", "1 adet muz", "1 su bardağı rendelenmiş kaşar peyniri"]
    instructions = "- 2 adet olgun muz\n- 1 su bardağı un\n- 1/2 su bardağı şeker\n- 1/2 su bardağı süt\n- 4 yemek kaşığı tereyağı (eritilmiş)\n- 100 gram rendelenmiş beyaz peynir\n\nYapılışı:\n1. Fırını önceden 180 derecede ısıtın ve mini kek kalıplarını yağlayın veya muffin kağıtları yerleştirin.\n\n2. Olgun muzları ezerek püre haline getirin ve bir kaseye alın.\n\n3. Ayrı bir kapta un, şeker ve rendelenmiş beyaz peyniri karıştırın.\n\n4. Muz püresine eritilmiş tereyağı ve sütü ekleyin ve iyice karıştırın.\n\n5. Muzlu karışımı unlu karışıma ekleyin ve spatula yardımıyla hafifçe karıştırın. Homojen bir karışım elde edene kadar karıştırmaya devam edin.\n\n6. Kek karışımını yağladığınız mini kek kalıplarına eşit olarak paylaştırın veya muffin kağıtlarına dökün.\n\n7. Önceden ısıtılmış fırında yaklaşık 20-25 dakika kadar pişirin. Kürdan testi yaparak keklerin piştiğinden emin olun. (Kürdan temiz çıkmalıdır)\n\n8. Fırından çıkan muzlu peynirli mini kekleri oda sıcaklığında bir süre bekletip servis yapın.\n\nAfiyet olsun! "

    generate_story(name, ingredients, instructions, "images/1.png")


