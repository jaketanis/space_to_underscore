import os

path_name = input("The path of the folder where you want filenames to be edited in: ")

# character variables
char_to_replace = ' '
char_to_add = '_'

counter = 0
print("============================================\n")

# renames the file with spaces to underscores
for file in os.listdir(path_name):
    new_file_name = ''
    file_chars = list(file)
    for char in file_chars:
        if char == char_to_replace:
            new_file_name += char_to_add
        else:
            new_file_name += char

    old_path_name = path_name + '\\' + file
    new_path_name = path_name + '\\' + new_file_name

    if old_path_name == new_path_name:
        print(f"Skipped: {file} \n")
    else:
        print(f"Changed: {file} \n")
        os.rename(old_path_name, new_path_name)
        counter += 1
print("============================================\n")
print(f"Edited {counter} files. Review the Flare project folder to see changes.")

