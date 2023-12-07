def read_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text_content = file.read()
        return text_content
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

file_path = 'input.txt'  
text_string = read_text_file(file_path)

if text_string:
    print("Text read successfully:")
    print(text_string)
    
    
else:
    print("Failed to read text from the file.")
