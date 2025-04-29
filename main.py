import os
from tqdm import tqdm

# Select Language
language = input("Select Language / 選擇語言:\n1. English\n2. 中文\nEnter 1 or 2: ").strip()

# Show Language
if language == "2":
    prompt_path = "請輸入資料夾路徑："
    prompt_num = "請輸入要更改的 class ID 數量："
    prompt_old = "第 {i} 個要更改的原 class ID："
    prompt_new = "第 {i} 個要更改成的新 class ID："
    prompt_table = "\n以下為將執行的 class ID 替換對照表："
    prompt_processing = "\n開始處理...\n"
    prompt_done = "\n✅ 所有檔案已處理完成！"
    progress_desc = "處理中"
else:
    prompt_path = "Enter the folder path: "
    prompt_num = "Enter the number of class IDs to modify: "
    prompt_old = "Original class ID #{i}: "
    prompt_new = "New class ID for #{i}: "
    prompt_table = "\nThe following class ID mappings will be applied:"
    prompt_processing = "\nProcessing files...\n"
    prompt_done = "\n✅ All files have been processed!"
    progress_desc = "Processing"

# Input folder Path
folder_path = input(prompt_path).strip()

class_id_mapping = {}
num_mappings = int(input(prompt_num))

for i in range(num_mappings):
    old_id = input(prompt_old.format(i=i+1)).strip()
    new_id = input(prompt_new.format(i=i+1)).strip()
    class_id_mapping[old_id] = new_id

# Show the Prompt Table
print(prompt_table)
for k, v in class_id_mapping.items():
    print(f"  {k} → {v}")

print(prompt_processing)

# Process the .txt files
txt_files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]

for file_name in tqdm(txt_files, desc=progress_desc, ncols=80):
    file_path = os.path.join(folder_path, file_name)

    with open(file_path, "r") as file:
        lines = file.readlines()

    updated_lines = []
    for line in lines:
        parts = line.strip().split()
        if len(parts) > 0 and parts[0] in class_id_mapping:
            parts[0] = class_id_mapping[parts[0]]
        updated_lines.append(" ".join(parts))

    with open(file_path, "w") as file:
        file.write("\n".join(updated_lines))

print(prompt_done)
