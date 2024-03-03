import os

def get_list_dir_files(path):
    all_items = os.listdir(path)
    dirs = [item for item in all_items if os.path.isdir(item)]
    files = [item for item in all_items if os.path.isfile(item)]
    print(f"Details of path: {path}")
    print(f"Directories: {dirs}")
    print(f"Files: {files}")
    print(f"All Items: {all_items}")

path = os.getcwd()
get_list_dir_files(path)
