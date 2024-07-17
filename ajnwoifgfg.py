import os
import shutil
import hashlib

def get_file_hash(file_path):
    with open(file_path, 'rb') as file:
        content = file.read()
        return hashlib.sha256(content).hexdigest()

def move_duplicate_files(source_dir, destination_dir):
    file_hashes = {}
    
    # Iterate through all files in the source directory
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = get_file_hash(file_path)
            
            # Check if the file hash already exists in the dictionary
            if file_hash in file_hashes:
                # Move the file to the destination directory
                shutil.move(file_path, destination_dir)
            else:
                # Add the file hash to the dictionary
                file_hashes[file_hash] = file_path

# Specify the source and destination directories
source_directory = 'D:/discord_ProfiPoint/LA23CLIPS'
destination_directory = 'D:/discord_ProfiPoint/duplicates'

# Call the function to move duplicate files
move_duplicate_files(source_directory, destination_directory)