import os

def get_file_extension(file_name):
    """Return the extension of a file in lowercase."""
    return os.path.splitext(file_name)[1].lower()


def is_valid_folder(folder_path):
    """Check whether the selected path is a folder."""
    return os.path.isdir(folder_path)


def get_file_statistics(folder_path):
    """Count files according to their category."""
    from categories import CATEGORIES

    stats = {
        "Images": 0,
        "Documents": 0,
        "Videos": 0,
        "Music": 0,
        "Others": 0
    }

    if not is_valid_folder(folder_path):
        return stats

    for file_name in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file_name)

        if not os.path.isfile(full_path):
            continue

        extension = get_file_extension(file_name)
        found = False

        for category, extensions in CATEGORIES.items():
            if extension in extensions:
                stats[category] += 1
                found = True
                break

        if not found:
            stats["Others"] += 1

    return stats
