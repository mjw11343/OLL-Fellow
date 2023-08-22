import os
import re

def replace_whitespace_with_dash(root_dir):
    for folder_name, subdirs, files in os.walk(root_dir):
        for file_name in files:
            file_path = os.path.join(folder_name, file_name)
            new_file_name = re.sub(r'\s+', '-', file_name)
            new_file_path = os.path.join(folder_name, new_file_name)
            
            if file_name != new_file_name:
                os.rename(file_path, new_file_path)
                print(f"Renamed '{file_name}' to '{new_file_name}' in '{folder_name}'")

if __name__ == "__main__":
    current_directory = 'C:/Users/Slewe/oll/library-prod/badriver-nsn/law-docs/us/nsn/badriver/council/resolutions'
    replace_whitespace_with_dash(current_directory)