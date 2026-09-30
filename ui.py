import tkinter as tk
from tkinter import filedialog, messagebox

from organizer import organize_files
from utils import get_file_statistics


class FileOrganizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart File Organizer")
        self.root.geometry("650x520")
        self.root.resizable(False, False)

        self.selected_folder = ""

        self.build_interface()

    def build_interface(self):
        title = tk.Label(
            self.root,
            text="SMART FILE ORGANIZER",
            font=("Arial", 22, "bold")
        )
        title.pack(pady=(25, 5))

        subtitle = tk.Label(
            self.root,
            text="Organize your files into simple categories",
            font=("Arial", 11)
        )
        subtitle.pack(pady=(0, 25))

        folder_frame = tk.Frame(self.root)
        folder_frame.pack(pady=5)

        self.folder_label = tk.Label(
            folder_frame,
            text="No folder selected",
            width=55,
            anchor="w",
            relief="sunken",
            padx=8
        )
        self.folder_label.pack(side="left", padx=5)

        select_button = tk.Button(
            folder_frame,
            text="Select Folder",
            command=self.select_folder,
            width=14
        )
        select_button.pack(side="left", padx=5)

        organize_button = tk.Button(
            self.root,
            text="ORGANIZE FILES",
            command=self.organize,
            width=22,
            height=2
        )
        organize_button.pack(pady=25)

        stats_title = tk.Label(
            self.root,
            text="FILE STATISTICS",
            font=("Arial", 14, "bold")
        )
        stats_title.pack(pady=(5, 10))

        self.stats_label = tk.Label(
            self.root,
            text="Select a folder to see its file statistics.",
            font=("Arial", 11),
            justify="left"
        )
        self.stats_label.pack()

        self.status_label = tk.Label(
            self.root,
            text="Status: Ready",
            font=("Arial", 10)
        )
        self.status_label.pack(side="bottom", pady=20)

    def select_folder(self):
        folder = filedialog.askdirectory(title="Select a folder")

        if folder:
            self.selected_folder = folder
            self.folder_label.config(text=folder)
            self.show_statistics()
            self.status_label.config(text="Status: Folder selected")

    def show_statistics(self):
        stats = get_file_statistics(self.selected_folder)

        text = (
            f"Images      : {stats['Images']}\n"
            f"Documents   : {stats['Documents']}\n"
            f"Videos      : {stats['Videos']}\n"
            f"Music       : {stats['Music']}\n"
            f"Others      : {stats['Others']}"
        )

        self.stats_label.config(text=text)

    def organize(self):
        if not self.selected_folder:
            messagebox.showwarning(
                "No Folder",
                "Please select a folder first."
            )
            return

        success, message = organize_files(self.selected_folder)

        if success:
            self.show_statistics()
            self.status_label.config(text="Status: Organization completed")
            messagebox.showinfo("Done", message)
        else:
            self.status_label.config(text="Status: Error")
            messagebox.showerror("Error", message)


def start_app():
    root = tk.Tk()
    FileOrganizerApp(root)
    root.mainloop()
