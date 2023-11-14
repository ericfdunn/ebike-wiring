#!/usr/bin/env python
from PIL import Image
import os

def image_props(folder_path):
    # Get a list of all files in the folder
    file_list = [f for f in os.listdir(folder_path) if f.lower().endswith('.jpg')]

    # Loop through the image files
    for filename in file_list:
        image_path = os.path.join(folder_path, filename)
        
        # Open the image using PIL
        with Image.open(image_path) as img:
            # Get the dimensions (width and height) of the image
            width, height = img.size
            
            # Calculate the aspect ratio
            aspect_ratio = width / height
            
            # Print the results
            print(f'File: {filename}')
            print(f'Dimensions: {width}x{height}')
            print(f'Aspect Ratio: {aspect_ratio:.2f}')
            print('-' * 30)

def crop_and_resize_image(input_path, output_path, target_width, target_height):
    with Image.open(input_path) as img:
        # Calculate the aspect ratio of the original image
        original_width, original_height = img.size
        original_aspect_ratio = original_width / original_height

        # Calculate the aspect ratio of the target dimensions
        target_aspect_ratio = target_width / target_height

        # Calculate the new dimensions and offsets for cropping
        if original_aspect_ratio > target_aspect_ratio:
            # Original image is wider, crop the sides
            new_width = int(original_height * target_aspect_ratio)
            new_height = original_height
            left_offset = (original_width - new_width) // 2
            top_offset = 0
        else:
            # Original image is taller, crop the top and bottom
            new_width = original_width
            new_height = int(original_width / target_aspect_ratio)
            left_offset = 0
            top_offset = (original_height - new_height) // 4

        # Crop and resize the image
        cropped_resized_img = img.crop((left_offset, top_offset, left_offset + new_width, top_offset + new_height))
        cropped_resized_img = cropped_resized_img.resize((target_width, target_height), Image.ANTIALIAS)

        # Save the edited image with the "-banner" suffix
        cropped_resized_img.save(output_path)

def process_images(folder_path, target_width, target_height):
    # Get a list of all files in the folder
    file_list = [f for f in os.listdir(folder_path) if f.lower().endswith('.jpg')]

    # Loop through the image files
    for filename in file_list:
        image_path = os.path.join(folder_path, filename)
        
        # Determine the output filename with the "-banner" suffix
        output_filename = "d-" + filename
        output_path = os.path.join(folder_path, output_filename)
        
        # Crop and resize the image and save it with the new name
        crop_and_resize_image(image_path, output_path, target_width, target_height)
        
        # Print the results
        print(f'Processed: {filename} -> {output_filename}')

       
if __name__ == "__main__":
    current_directory = os.getcwd()
    # image_props(current_directory)
    process_images(current_directory, 600, 800)


