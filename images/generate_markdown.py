#!/usr/bin/env python
import os

# List of image file extensions to search for
image_extensions = ['.jpg', '.png', '.gif', '.jpeg']

def generate_markdown_image_links(folder_path, markdown_file):
    # Get a list of all files in the folder with image extensions
    image_files = [f for f in os.listdir(folder_path) if any(f.lower().endswith(ext) for ext in image_extensions)]

    # Open the markdown file for writing
    with open(markdown_file, 'w') as md_file:
        # Loop through the image files and generate markdown image links
        for image_file in image_files:
            # Create a markdown image link
            markdown_link = f"![{image_file}]({image_file})"
            
            # Write the markdown image link to the markdown file
            md_file.write(markdown_link + '\n')

def print_markdown_image_links(folder_path):
    # Get a list of all files in the folder with image extensions
    image_files = [f for f in os.listdir(folder_path) if any(f.lower().endswith(ext) for ext in image_extensions)]

    # Sort items alphabetically
    image_files.sort()

    # Loop through the image files and generate markdown image links
    for image_file in image_files:
        # Create a markdown image link
        print(f"![{image_file}](</images/{image_file}>)")
        
       
if __name__ == "__main__":
    current_directory = os.getcwd()
#    markdown_file_name = "image_links.md"  # Change this to your desired markdown file name
#    generate_markdown_image_links(current_directory, markdown_file_name)
    print_markdown_image_links(current_directory)
