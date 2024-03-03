import os

def delete_file(path):
    if os.access(path, os.F_OK) and os.path.exists(path):
        os.remove(path)
        print("File deleted.")
    else:
        print("File does not exist or is not accessible.")

path = r"C:\Users\Temirlan\Desktop\second sem\pp2\labs\lab 6\dir-and-files\ex8.txt"
delete_file(path)