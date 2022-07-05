import os
import shutil

original_path = r'-----------------------------------'
new_path = r'------------------------------------------'

# try:
#     os.mkdir(new_path)
# except FileExistsError as e:
#     print(f'Folder {new_path} already exist.')

for root, dirs, files in os.walk(new_path):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(new_path, file)
        # if '.docx' in file:
        #     shutil.move(old_file_path, new_file_path)
        #     shutil.copy(old_file_path, new_file_path)
        #     print(f'File {file} moved sucessfully')
        if '.docx' in file:
            os.remove(new_file_path)


