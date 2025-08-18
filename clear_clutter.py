# rename or save files as in sequential format:
# Example (as comment): bcz here no files module is there.
'''
import os

# Path to your folder
folder_path = r"C:\Users\YourName\Pictures\Clutter"

# Get all files in the folder
files = os.listdir(folder_path)

# Allowed image extensions
image_extensions = (".png", ".jpg", ".jpeg")

# Filter only image files
image_files = [f for f in files if f.lower().endswith(image_extensions)]

# Rename each file sequentially
for idx, filename in enumerate(image_files, start=1):
    ext = os.path.splitext(filename)[1]  # Extract the file extension
    old_path = os.path.join(folder_path, filename)
    new_filename = f"{idx:03}{ext}"  # e.g., 001.jpg
    new_path = os.path.join(folder_path, new_filename)
    os.rename(old_path, new_path)
    print(f"Renamed: {filename} -> {new_filename}")

print("Files renamed successfully!")
'''
