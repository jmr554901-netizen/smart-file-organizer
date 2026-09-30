import os
import shutil

from categories import CATEGORIES
from utils import get_file_extension, is_valid_folder


def get_category(file_name):
    """Find the category of a file from its extension."""
    extension = get_file_extension(file_name)

    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def create_category_folders(folder_path):
    """Create folders for the different file categories."""
    category_names = list(CATEGORIES.keys()) + ["Others"]

    for category in category_names:
        category_path = os.path.join(folder_path, category)
        os.makedirs(category_path, exist_ok=True)


def organize_files(folder_path):
    """Move files into their correct category folders."""
    if not is_valid_folder(folder_path):
        return False, "Please select a valid folder."

    create_category_folders(folder_path)

    moved_files = 0

    for file_name in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file_name)

        # Ignore folders because only files need to be organized.
        if not os.path.isfile(full_path):
            continue

        category = get_category(file_name)
        destination_folder = os.path.join(folder_path, category)
        destination = os.path.join(destination_folder, file_name)

        # If a file with the same name already exists, don't overwrite it.
        if os.path.exists(destination):
            continue

        try:
            shutil.move(full_path, destination)
            moved_files += 1
        except OSError:
            continue

    return True, f"{moved_files} file(s) organized successfully."
