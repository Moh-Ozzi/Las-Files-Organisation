import os
import shutil
import lasio

# Path to the folder containing LAS files
folder_path = "path_to_folder_X"

# Create a dictionary to map well names to file paths
well_files = {}

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".las"):  # Process only LAS files
        file_path = os.path.join(folder_path, filename)
        try:
            las = lasio.read(file_path)
            well_name = las.well.WELL.value.strip()  # Get and clean the well name
            if well_name not in well_files:
                well_files[well_name] = []
            well_files[well_name].append(file_path)
        except Exception as e:
            print(f"Error processing file {filename}: {e}")

# Create subdirectories for each well and move the files
for well_name, files in well_files.items():
    if well_name:  # Ensure the well name is not empty
        well_dir = os.path.join(folder_path, well_name)
        os.makedirs(well_dir, exist_ok=True)  # Create subdirectory for the well
        for file_path in files:
            shutil.move(file_path, os.path.join(well_dir, os.path.basename(file_path)))

print("Files organized into subdirectories based on well names.")