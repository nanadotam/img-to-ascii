from PIL import Image

def asciiConvert(image, type, saveas, scale):
    scale = int(scale)

    # open the image and get size
    img = Image.open(image)
    w, h = img.size

    # resize the image (downscale)
    img.resize((w//scale, h//scale)).save("resized.%s" % type)

    #open new image
    img = image.open("resized.%s" % type)
    w, h = img.size # get new width and height 

    