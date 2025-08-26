# rename or save files as in sequential format:
# Example (as comment): to prevent error: module not found bcz here no files or module is there.
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
# Practice Question:
'''Question 1: Resume Files Cleanup
You are given messy resume file names:

["resume(John).pdf", "resume-final.docx", "resume_v2.docx", 
"resume2024.pdf"]

Write a program to rename them as:
1.pdf, 2.docx, 3.docx, 4.pdf '''

import os

folder_path = r"C:\Users\HP\Pictures\Screenshots\Clutter"

files = os.listdir(folder_path)


file_extensions = (".pdf", ".docx")

target_files = [f for f in files if f.lower().endswith(file_extensions)]

for idx, filename in enumerate(target_files, start=1):
    ext = os.path.splitext(filename)[1]    
      
    old_path = os.path.join(folder_path, filename)
    new_path = os.path.join(folder_path, f"{idx}{ext}")
    os.rename(old_path, new_path)

print("Files renamed successfully!")

# Expected Output:
''' 1.pdf
2.docx
3.docx
4.pdf '''

