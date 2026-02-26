import os
from utils import get_file_hash

def get_all_files(folder_path):
    all_files = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            full_path = os.path.join(root, file)
            all_files.append(full_path)

    return all_files

def find_duplicates(files):
    hashes = {}
    
    for file in files:
        file_hash = get_file_hash(file)

        if file_hash is None:
            continue

        if file_hash in hashes:
            hashes[file_hash].append(file)

        else:
            hashes[file_hash] = [file]
        
    duplicates = {hash: file_list for hash, file_list in hashes.items() if len(file_list)>1}

    return duplicates

def remove_file(file_path):
    confirm = input(f"Are you sure you want to delete {file_path}? (y/n):")
    if confirm.lower() == 'y':
        try:
            os.remove(file_path)
            print(f"Deleted {file_path}")
        except Exception as e:
            print(f"Error deleting file: {e}")
    else:
        print(f"Skipped {file_path}")
