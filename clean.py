import json
import os

def is_valid_json_array(input_str):
    try:
        json_data = json.loads(input_str)
        if isinstance(json_data, list):
            return True
        else:
            return False
    except ValueError:
        return False

def check_json_files_in_folder(folder_path):
    invalid_files = []
    for file in os.listdir(folder_path):
        if file.endswith(".json"):
            file_path = os.path.join(folder_path, file)
            is_valid = False
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                is_valid = is_valid_json_array(content)
            if not is_valid:
                invalid_files.append(file_path)
                os.rename(file_path, file_path + ".invalid")
    return invalid_files


# 示例
folder_path = "out"
invalid_files = check_json_files_in_folder(folder_path)

if(len(invalid_files)==0):
    print("All files are valid.")
else:
    print("Invalid files: ", invalid_files)