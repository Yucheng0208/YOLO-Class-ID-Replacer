import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tqdm import tqdm

# Language options (can expand to more languages)
LANG = {
    "zh": {
        "title": "Class ID 批次替換工具",
        "select_folder": "選擇資料夾",
        "add_mapping": "新增對應",
        "run": "執行",
        "exit": "離開",
        "msg_done": "✅ 所有檔案處理完成！",
        "msg_no_folder": "請先選擇資料夾！",
        "msg_no_mapping": "請至少輸入一個對應項！",
        "label_folder": "選擇標註資料夾：",
        "label_mappings": "Class ID 對應表：",
    },
    "en": {
        "title": "Class ID Batch Replacer",
        "select_folder": "Select Folder",
        "add_mapping": "Add Mapping",
        "run": "Run",
        "exit": "Exit",
        "msg_done": "✅ All files have been processed!",
        "msg_no_folder": "Please select a folder first!",
        "msg_no_mapping": "Please add at least one mapping!",
        "label_folder": "Label folder path:",
        "label_mappings": "Class ID Mappings:",
    }
}

# Default language is Traditional Chinese
current_lang = "zh"


class IDMapperGUI:
    def __init__(self, root):
        self.root = root
        self.root.title(LANG[current_lang]["title"])
        self.folder_path = ""

        # Label and entry for folder path
        self.label_path = tk.Label(root, text=LANG[current_lang]["label_folder"])
        self.label_path.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.entry_path = tk.Entry(root, width=50)
        self.entry_path.grid(row=0, column=1, padx=5)
        self.btn_browse = tk.Button(root, text=LANG[current_lang]["select_folder"], command=self.browse_folder)
        self.btn_browse.grid(row=0, column=2, padx=5)

        # Label and frame for mappings
        self.label_map = tk.Label(root, text=LANG[current_lang]["label_mappings"])
        self.label_map.grid(row=1, column=0, sticky="nw", padx=10)
        self.frame_mapping = tk.Frame(root)
        self.frame_mapping.grid(row=1, column=1, columnspan=2, sticky="w")
        self.mapping_entries = []

        self.add_mapping_row()  # Start with one row by default
        self.btn_add = tk.Button(root, text=LANG[current_lang]["add_mapping"], command=self.add_mapping_row)
        self.btn_add.grid(row=2, column=1, sticky="w", padx=10, pady=5)

        # Run and Exit buttons
        self.btn_run = tk.Button(root, text=LANG[current_lang]["run"], command=self.run_processing)
        self.btn_run.grid(row=3, column=1, pady=10, sticky="e")
        self.btn_exit = tk.Button(root, text=LANG[current_lang]["exit"], command=root.quit)
        self.btn_exit.grid(row=3, column=2, pady=10, sticky="w")

    def browse_folder(self):
        # Open folder selection dialog
        path = filedialog.askdirectory()
        if path:
            self.folder_path = path
            self.entry_path.delete(0, tk.END)
            self.entry_path.insert(0, path)

    def add_mapping_row(self):
        # Add a new row for class ID mapping
        row_frame = tk.Frame(self.frame_mapping)
        row_frame.pack(pady=2, anchor="w")
        entry_from = tk.Entry(row_frame, width=10)
        entry_to = tk.Entry(row_frame, width=10)
        entry_from.pack(side="left")
        tk.Label(row_frame, text="→").pack(side="left", padx=5)
        entry_to.pack(side="left")
        self.mapping_entries.append((entry_from, entry_to))

    def run_processing(self):
        folder = self.entry_path.get()
        if not folder:
            messagebox.showerror("Error", LANG[current_lang]["msg_no_folder"])
            return

        # Read all mappings from GUI entries
        mapping = {}
        for entry_from, entry_to in self.mapping_entries:
            k = entry_from.get().strip()
            v = entry_to.get().strip()
            if k and v:
                mapping[k] = v

        if not mapping:
            messagebox.showerror("Error", LANG[current_lang]["msg_no_mapping"])
            return

        # Get all .txt files in folder
        txt_files = [f for f in os.listdir(folder) if f.endswith(".txt")]

        # Process each file with tqdm progress bar
        for file_name in tqdm(txt_files, desc="Processing", ncols=80):
            file_path = os.path.join(folder, file_name)
            with open(file_path, "r") as file:
                lines = file.readlines()

            updated_lines = []
            for line in lines:
                parts = line.strip().split()
                if len(parts) > 0 and parts[0] in mapping:
                    parts[0] = mapping[parts[0]]
                updated_lines.append(" ".join(parts))

            with open(file_path, "w") as file:
                file.write("\n".join(updated_lines))

        # Show completion dialog
        messagebox.showinfo("Done", LANG[current_lang]["msg_done"])


if __name__ == "__main__":
    # Launch GUI
    root = tk.Tk()
    app = IDMapperGUI(root)
    root.mainloop()
