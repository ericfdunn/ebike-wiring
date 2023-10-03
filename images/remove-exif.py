#!/usr/bin/env python3

# Remove exif data for privacy protection from all photos in current directory

import os
from PIL import Image

def remove_exif(directory):
    
    for index, filename in enumerate(sorted(os.listdir(directory)), start=1):
        if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg'):
            filepath = os.path.join(directory, filename)
            
            # Open the image using PIL
            image = Image.open(filepath)
            
            # Check if EXIF data is present
            exif_data = image._getexif()
            if not exif_data or len(exif_data) == 0:
                print(f"Skipped {filename} (No EXIF data found)")
                continue
            
            # Remove EXIF data by not copying it over
            data = list(image.getdata())
            image_without_exif = Image.new(image.mode, image.size)
            image_without_exif.putdata(data)
            
            # Construct the new filename
            new_filename = f"image{index:03}.jpg"
            new_filepath = os.path.join(directory, new_filename)
            
            # Save the new image with new filename
            image_without_exif.save(new_filepath)
            
            # Delete the original image (if the new filename isn't the same as the original)
        #    if filepath != new_filepath:
        #        os.remove(filepath)

            print(f"Processed {filename} -> {new_filename}")
            
# directory_path = input("Enter the path to the directory containing JPEGs: ")
remove_exif(os.getcwd())

