from PIL import Image


def show(image_name):
    img = Image.open(image_name)
    img.show()


def crop(image_name):
    img = Image.open(image_name)
    img = img.convert("RGB")
    width, height = img.size
    left = 157   #150
    top = height - 497
    right = 685
    bottom = height
    new_img = img.crop((left, top, right, bottom))
    new_img.save("mainpost.jpg")
    new_img.save("mainpost.png")

