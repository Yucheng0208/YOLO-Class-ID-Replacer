import os

# Specify the folder path
folder_path = f"path_to_your_folder"  # Replace this with the path to your folder

# Define the mapping of class_id to new values
class_id_mapping = {
    "0": "10",  # Change class_id 0 to 10
    "1": "20",  # Change class_id 1 to 20
    "2": "30"   # Change class_id 2 to 30
}

# Iterate through all .txt files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith(".txt"):
        file_path = os.path.join(folder_path, file_name)
        
        # Read the content of the file
        with open(file_path, "r") as file:
            lines = file.readlines()
        
        # Process each line and replace class_id
        updated_lines = []
        for line in lines:
            parts = line.strip().split()
            if parts[0] in class_id_mapping:
                parts[0] = class_id_mapping[parts[0]]  # Replace class_id
            updated_lines.append(" ".join(parts))
        
        # Overwrite the original file
        with open(file_path, "w") as file:
            file.write("\n".join(updated_lines))
        
        print(f"Updated file: {file_name}")

print("All files have been processed!")
