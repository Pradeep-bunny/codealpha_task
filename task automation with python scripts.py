import os
import shutil

# Set the directory you want to organize
directory_to_organize = r'C:\Users\YourUsername\Downloads'  # Change this to your path

def organize_files_by_type(directory):
    if not os.path.exists(directory):
        print("Directory does not exist.")
        return

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get file extension (without dot and in lowercase)
        file_extension = os.path.splitext(filename)[1][1:].lower()

        if file_extension == "":
            target_folder = "Others"
        else:
            target_folder = file_extension.upper()

        # Full path to the new folder
        folder_path = os.path.join(directory, target_folder)

        # Create folder if it doesn't exist
        os.makedirs(folder_path, exist_ok=True)

        # Move file
        shutil.move(file_path, os.path.join(folder_path, filename))
        print(f"Moved: {filename} → {target_folder}/")

    print("File organization complete.")

# Run the function
organize_files_by_type(directory_to_organize)
