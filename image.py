from PIL import Image

# path to .png file
image = Image.open(".png")
# convert to RGB
# https://pillow.readthedocs.io/en/latest/reference/Image.html#PIL.Image.Image.convert
rgb_image = image.convert('RGB')
# save file as jpg
rgb_image.save('NEW_FILE.jpg')