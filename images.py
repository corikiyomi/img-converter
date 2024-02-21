from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')

# filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img = img.convert('L')
# crooked = filtered_img.rotate(90)
resize = filtered_img.resize((300, 300))
resize.save("grey.png", 'png')
# filtered_img.show() # opens a Preview window with image

