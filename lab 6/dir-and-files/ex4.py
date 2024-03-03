def count_lines(file_path):
    with open(file_path, "r") as file:
        print(f"Number of lines: {len(file.readlines())}.")

path = r"C:\Users\Temirlan\Desktop\second sem\pp2\labs\lab 6\dir-and-files\ex4.txt"
count_lines(path)