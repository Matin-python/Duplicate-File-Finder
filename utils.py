import hashlib

def get_file_hash(file_path):
    hasher = hashlib.md5()

    try:
        with open(file_path, 'rb') as file:
            while chunk:= file.read(4096):
                hasher.update(chunk)
        return hasher.hexdigest()
    
    except Exception as e:
        print(f"Error reading{file_path}: {e}")
        return None