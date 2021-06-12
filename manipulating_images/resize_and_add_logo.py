 #! python3
# resize_and_add_logo.py - Resizes all images in current working directory to fit in a 300x300 square, and adds catlogo.png to the lower-right corner

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'
logo_img = Image.open(LOGO_FILENAME)
logo_width, logo_height = logo_img.size

os.makedirs('withLogo', exist_ok=True)

# Loop over all files in the working directory
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == LOGO_FILENAME:
        continue

    img = Image.open(filename)
    width, height = img.size

    # Check if image needs to be resized
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:

        # Calculate the new width and height to resize to
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        # Resize the image
        print(f'Resizing {filename}...')
        img = img.resize((width, height))

    # Add the logo
    print(f'Adding logo to {filename}...')
    img.paste(logo_img, (width - logo_width, height - logo_height), logo_img)

    # Save changes
    img.save(os.path.join('withLogo', filename))