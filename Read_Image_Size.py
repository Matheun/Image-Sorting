import os
from PIL import Image
import glob

# -----
# Gets locations of the folder on the device
# -----
dir_path = os.path.dirname(os.path.realpath(__file__))

# -----
# Selects all the images in the folder
# -----
folders = glob.glob(dir_path)
imagenames_list = []

# -----
# Creates the name for transporting the images
# -----
for folder in folders:
    for f in glob.glob(folder + '/*.png'):
        imagenames_list.append(f)

# -----
# Processes the images and sorts them in the correct
# folders which are selected/created
# -----
for i in range(len(imagenames_list)):

    # -----
    # Gets the information about the location and size
    # of the images
    # -----
    base = os.path.basename(imagenames_list[i])
    im = Image.open(imagenames_list[i])
    width = im.size[0]
    height = im.size[1]
    im.close()

    # -----
    # Creates the folders : Horizontal, Vertical and Square
    # If they don`t already exist
    # -----
    if not os.path.exists('Horizontal'):
        os.makedirs('Horizontal')
    if not os.path.exists('Vertical'):
        os.makedirs('Vertical')
    if not os.path.exists('Square'):
        os.makedirs('Square')

    # -----
    # Creates the destinations for the images to go into
    # -----
    source = imagenames_list[i]
    destinationHorizontal = dir_path + "\\Horizontal\\" + base
    destinationVertical = dir_path + "\\Vertical\\" + base
    destinationSquare = dir_path + "\\Square\\" + base

    # -----
    # Sorts the images in the correct folders
    # -----
    try:
        if width > height:
            os.replace(source, destinationHorizontal)
            print(source + " was moved")

        elif height > width:
            os.replace(source, destinationVertical)
            print(source + " was moved")
        elif height == width:
            os.replace(source, destinationSquare)
            print(source + " was moved")
        else:
            print(source + " was not found")

    # -----
    # If the image isn`t found it wil display an error
    # -----
    except FileNotFoundError:
        print(source + " was not found")