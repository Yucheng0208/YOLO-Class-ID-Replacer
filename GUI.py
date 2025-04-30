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
        "msg_done": "所有檔案處理完成！",
        "msg_no_folder": "請先選擇資料夾！",
        "msg_no_mapping": "請至少輸入一個對應項！",
        "label_folder": "選擇標註資料夾：",
        "label_mappings": "Class ID 對應表：",
        "label_add_count": "新增筆數：",
        "error_input": "請輸入正整數"
    },
    "en": {
        "title": "Class ID Batch Replacer",
        "select_folder": "Select Folder",
        "add_mapping": "Add Mapping",
        "run": "Run",
        "exit": "Exit",
        "msg_done": "All files have been processed!",
        "msg_no_folder": "Please select a folder first!",
        "msg_no_mapping": "Please add at least one mapping!",
        "label_folder": "Label folder path:",
        "label_mappings": "Class ID Mappings:",
        "label_add_count": "Number to Add:",
        "error_input": "Please enter a positive integer."
    }
}

# Default language
current_lang = "zh"  # 切換為 "en" 可顯示英文 GUI


class IDMapperGUI:
    def __init__(self, root):
        self.root = root
        self.root.title(LANG[current_lang]["title"])
        self.folder_path = ""

        # 資料夾路徑選擇
        self.label_path = tk.Label(root, text=LANG[current_lang]["label_folder"])
        self.label_path.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.entry_path = tk.Entry(root, width=50)
        self.entry_path.grid(row=0, column=1, padx=5)
        self.btn_browse = tk.Button(root, text=LANG[current_lang]["select_folder"], command=self.browse_folder)
        self.btn_browse.grid(row=0, column=2, padx=5)

        # 對應表標題
        self.label_map = tk.Label(root, text=LANG[current_lang]["label_mappings"])
        self.label_map.grid(row=1, column=0, sticky="nw", padx=10)
        self.frame_mapping = tk.Frame(root)
        self.frame_mapping.grid(row=1, column=1, columnspan=2, sticky="w")
        self.mapping_entries = []

        # 新增筆數輸入與按鈕
        self.label_count = tk.Label(root, text=LANG[current_lang]["label_add_count"])
        self.label_count.grid(row=2, column=0, sticky="e", padx=10)
        self.add_count_var = tk.StringVar(value="1")
        self.entry_count = tk.Entry(root, textvariable=self.add_count_var, width=5)
        self.entry_count.grid(row=2, column=1, sticky="w", padx=0)
        self.btn_add = tk.Button(root, text=LANG[current_lang]["add_mapping"], command=self.add_multiple_mappings)
        self.btn_add.grid(row=2, column=1, padx=60, sticky="w")

        self.add_mapping_row()  # 預設一筆

        # 執行與離開按鈕
        self.btn_run = tk.Button(root, text=LANG[current_lang]["run"], command=self.run_processing)
        self.btn_run.grid(row=3, column=1, pady=10, sticky="e")
        self.btn_exit = tk.Button(root, text=LANG[current_lang]["exit"], command=root.quit)
        self.btn_exit.grid(row=3, column=2, pady=10, sticky="w")

    def browse_folder(self):
        path = filedialog.askdirectory()
        if path:
            self.folder_path = path
            self.entry_path.delete(0, tk.END)
            self.entry_path.insert(0, path)

    def add_mapping_row(self):
        row_frame = tk.Frame(self.frame_mapping)
        row_frame.pack(pady=2, anchor="w")
        entry_from = tk.Entry(row_frame, width=10)
        entry_to = tk.Entry(row_frame, width=10)
        entry_from.pack(side="left")
        tk.Label(row_frame, text="→").pack(side="left", padx=5)
        entry_to.pack(side="left")
        self.mapping_entries.append((entry_from, entry_to))

    def add_multiple_mappings(self):
        try:
            count = int(self.add_count_var.get())
            if count <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", LANG[current_lang]["error_input"])
            return

        for _ in range(count):
            self.add_mapping_row()

    def run_processing(self):
        folder = self.entry_path.get()
        if not folder:
            messagebox.showerror("Error", LANG[current_lang]["msg_no_folder"])
            return

        mapping = {}
        for entry_from, entry_to in self.mapping_entries:
            k = entry_from.get().strip()
            v = entry_to.get().strip()
            if k and v:
                mapping[k] = v

        if not mapping:
            messagebox.showerror("Error", LANG[current_lang]["msg_no_mapping"])
            return

        txt_files = [f for f in os.listdir(folder) if f.endswith(".txt")]

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

        messagebox.showinfo("Done", LANG[current_lang]["msg_done"])


if __name__ == "__main__":
    root = tk.Tk()
    app = IDMapperGUI(root)
    root.mainloop()
