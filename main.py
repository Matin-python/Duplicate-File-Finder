from finder import get_all_files, find_duplicates, remove_file

def main():

    folder_path = input("Enter your file path: ")

    files = get_all_files(folder_path)

    print ("\nScanning for duplicates...\n")
    duplicates = find_duplicates(files)
    
    if not duplicates:
        print("No duplicated files found")
    else:
        print("Duplicated files")
        for file_hash, file_list in duplicates.items():
            print("---------") 
            for file in file_list:
                print(file)

        delete_choice = input("Do you want to delete the duplicate files? (y/n):")
        if delete_choice.lower() == 'y':
            for file_hash, file_list in duplicates.items():
                for file in file_list:
                    remove_file(file)

    print("End")



if __name__ == "__main__":
    main()