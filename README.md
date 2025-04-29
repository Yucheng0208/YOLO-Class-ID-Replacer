# Class ID Replacer

A dual-interface Python tool (CLI + GUI) to batch replace `class_id` values in `.txt` label files. This is particularly useful for modifying YOLO-style object detection annotations or preparing datasets for machine learning.

## 🔧 Features

- Replace `class_id` values based on user-defined mappings.
- Supports Command-Line Interface (CLI) and Graphical User Interface (GUI).
- Automatically processes all `.txt` files in a folder.
- Overwrites original files to save storage.
- Multilingual support (English and Traditional Chinese).
- Progress bar using `tqdm`.

---

## 📦 Requirements

- Python 3.6 or above
- Required Python packages:
  ```bash
  pip install tqdm
  ```
## 🚀 Usage
### Option 1: Command-Line Interface (CLI)
**Run the script**
```bash
python CLI.py
```
**Steps:**
1. Choose language: `1` for English or `2` for 中文.
2. Input the path to your `.txt` annotation folder.
3. Input the number of `class_id` pairs to replace.
4. Enter each original ID and its corresponding new ID.
5. The script will display the mapping table and begin processing.

**Example**
- Before
```txt
0 0.132 0.428 0.212 0.675
1 0.141 0.160 0.092 0.098
2 0.378 0.487 0.192 0.617
```
- After
```txt
10 0.132 0.428 0.212 0.675
20 0.141 0.160 0.092 0.098
30 0.378 0.487 0.192 0.617
```

### Option 2: Graphical User Interface (GUI)
**Run the script**
```bash
python GUI.py
```
**Steps:**
1. Select the folder containing your label files.
2. Add one or more mapping pairs (e.g., `0 → 10`).
3. Click Run to start processing.
4. A popup message will confirm successful completion.

## 🌐 Language Support
- English (`en`)
- Traditional Chinese (`zh`)

## 📄 License
This project is licensed under the [MIT License](LICENSE). See the [LICENSE](LICENSE) file for complete details.

