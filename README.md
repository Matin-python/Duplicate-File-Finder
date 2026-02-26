# Duplicate File Finder

A Python tool to scan a folder and find duplicate files based on their MD5 hash values. It recursively scans through all subdirectories and identifies files that are duplicates.

## Features 

- Recursive Folder Scanning: Scans the provided folder and its subdirectories for files.
- MD5 Hashing: Uses MD5 hashing to identify duplicate files.
- Safe Deletion: Option to delete duplicate files after user confirmation.
- User-Friendly: Command-line interface that allows users to interact easily with the tool.

## Requirements

- Python 3.x
- No additional libraries required (uses the built-in hashlib and os modules).

## How to Run

1. Clone or download this repository.
2. Open a terminal or command prompt.
3. Navigate to the folder where you saved the repository.
4. Run the script:
   
bash
    python main.py
    
5. Enter the path of the folder you want to scan.
6. The tool will display any duplicate files found.
7. You will be prompted if you want to delete the duplicate files.

## Example Usage

      `bash
      Enter folder path: /path/to/your/folder
      Scanning for duplicates...

      Duplicate files found:
      ----------
      /path/to/your/folder/file1.txt
      /path/to/your/folder/file1 (1).txt
      Do you want to delete the duplicate files? (y/n): y
      Are you sure you want to delete /path/to/your/folder/file1 (1).txt? (y/n): y
      Deleted /path/to/your/folder/file1 (1).txt

      Scan completed.


