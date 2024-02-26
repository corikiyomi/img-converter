# takes two args from user input 
    # first arg is current image folder
    # second arg is the new image folder that gets created
    # if you run script: python3 JPGtoPNGconverter.py Pokedex/ new/

import sys
import os
from PIL import Image

# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

print(image_folder, output_folder)

# check if new/ exists, if not create
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    
# loop through Pokedex
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done!')

# convert images to png
# save to the new folder
