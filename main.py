import os
from datetime import datetime
import re

def get_date_prefix(file_path):
    """
    Get the file's last modification date in 'yymmdd' format.
    """
    timestamp = os.path.getmtime(file_path)
    date = datetime.fromtimestamp(timestamp)
    return date.strftime("%y%m%d")

def extract_base_filename(filename):
    """
    Remove ALL existing yymmdd prefixes from the filename.
    """
    # Remove all leading yymmdd_ prefixes
    base_name = re.sub(r"^(\d{6}_)+", "", filename)
    return base_name

def get_latest_date_from_multiple_prefixes(filename):
    """
    Extract the latest date from multiple leading yymmdd prefixes.
    Returns None if no valid prefixes found.
    """
    parts = filename.split('_')
    prefixes = []
    for part in parts:
        # Check if part is a valid 6-digit date
        if len(part) == 6 and part.isdigit():
            prefixes.append(part)
        else:
            break  # Stop at first non-date component
    return max(prefixes) if prefixes else None

def generate_new_name(original_name, date_prefix, folder_path):
    """
    Generate a clean filename with the new/latest date prefix.
    """
    base_name = extract_base_filename(original_name)
    return f"{date_prefix}_{base_name}"

def rename_file(entry, folder_path):
    # Get current modification date prefix
    new_prefix = get_date_prefix(entry.path)
    
    # Check for existing prefixes in filename
    existing_prefix = get_latest_date_from_multiple_prefixes(entry.name)
    
    # Use latest prefix if available
    final_prefix = existing_prefix or new_prefix
    
    # Generate new name
    new_name = generate_new_name(entry.name, final_prefix, folder_path)
    
    # Perform rename
    os.rename(entry.path, os.path.join(folder_path, new_name))
    print(f"Renamed: {entry.name} -> {new_name}")

def main():
    folder_path = "filebatch-prefixer/master_folder"
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        return

    for entry in os.scandir(folder_path):
        if entry.is_file():
            rename_file(entry, folder_path)

    print("All files renamed successfully.")

if __name__ == "__main__":
    main()