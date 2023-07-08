from PIL import Image, ImageDraw, ImageFont

font = "./templates/fonts/TTNorms-Bold.otf"

img = Image.open("templates/1.png", mode='r')
image_width = img.width
image_height = img.height
draw = ImageDraw.Draw(img)
text = "Muzlu Peynirli Mini Kekler"

font = ImageFont.truetype(font, size=100)

text_width, _ = draw.textsize(text, font=font)
percent_width, _ = draw.textsize("%", font=font)
text_y_position = (image_height - text_width) / 2
draw.text(( (image_width - text_width-200) / 2, text_y_position ), "%", fill=(0, 0, 0), stroke_width=2, font=font)
draw.text( ( (image_width - text_width) / 2, text_y_position ), text, fill=(0, 0, 0), stroke_width=2, font=font)

img.show()