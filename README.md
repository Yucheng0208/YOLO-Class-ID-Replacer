## Introduction
Class ID Replacer is a simple Python script designed to update `class_id` values in `.txt` files and overwrite the original files. It is particularly useful for tasks like modifying object detection labels or preparing datasets for machine learning.

## Features
- Replace `class_id` values based on a user-defined mapping.
- Automatically process all `.txt` files in a specified folder.
- Overwrite the original files to save storage space.
- Simple and lightweight.

## Requirements
- Python 3.6 or later

## Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/your_username/class-id-replacer.git
   cd class-id-replacer
   ```
2. Modify the `folder_path` variable in the script to point to your `.txt` files directory:
  ```python
  folder_path = "path_to_your_folder"
  ```
3. Adjust the `class_id_mapping` dictionary to define your custom mappings:
  ```python
  class_id_mapping = {
      "0": "10",  # Change class_id 0 to 10
      "1": "20",  # Change class_id 1 to 20
      "2": "30"   # Change class_id 2 to 30
  }
  ```
4. Run the script:
   ```bash
   python replace_class_id.py
   ```
5. The script will automatically process and overwrite the .txt files in the specified folder.

## Example
### Before
   ```txt
      0 0.13203125 0.42890625 0.2125 0.67578125
      1 0.14140625 0.1609375 0.09296875 0.0984375
      2 0.37890625 0.4875 0.19296875 0.6171875
   ```
### After
   ```txt
   10 0.13203125 0.42890625 0.2125 0.67578125
   20 0.14140625 0.1609375 0.09296875 0.0984375
   30 0.37890625 0.4875 0.19296875 0.6171875
   ```
# License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

# Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue if you encounter any problems or have suggestions for improvement.
