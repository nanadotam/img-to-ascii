import sys
from PIL import Image

def asciiConvert(image, type, saveas, scale):
    scale = int(scale)

    # open the image and get size
    img = Image.open(image)
    w, h = img.size

    # resize the image (downscale)
    img.resize((w//scale, h//scale)).save("resized.%s" % type)

    #open new image
    img = Image.open("resized.%s" % type)
    w, h = img.size

    #list with correct length and height
    grid = []
    for i in range(h):
        grid.append([" "] * w)  # Initialize with spaces instead of "X"

    pix = img.load()

    for y in range(h):
        for x in range(w):
            pixel_sum = sum(pix[x,y])
            # Inverted logic - now darker pixels get characters
            if pixel_sum < 100:
                grid[y][x] = "X"
            elif pixel_sum < 200:
                grid[y][x] = "%"
            elif pixel_sum < 300:
                grid[y][x] = "&"
            elif pixel_sum < 400:
                grid[y][x] = "+"
            elif pixel_sum < 500:
                grid[y][x] = "/"
            elif pixel_sum < 600:
                grid[y][x] = "()"
            else:
                grid[y][x] = " "  # Lighter pixels become spaces

    art = open(saveas, "w") 
        
    for row in grid:
        art.write("".join(row)+"\n")
            
    art.close()

# run from command line with image details
if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: python program_name.py <image_path> <image_type> <output_file> <scale>")
        sys.exit(1)
    
    image_path = sys.argv[1]
    image_type = sys.argv[2]
    output_file = sys.argv[3]
    scale = sys.argv[4]
    
    asciiConvert(image_path, image_type, output_file, scale)
