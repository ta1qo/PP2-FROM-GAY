import os

def test_path_details(path, testNumber):
    print(f"# {testNumber} path: {path}")
    if os.path.exists(path):
        print("Path is exists")
        if os.path.isfile(path):
            print(f"1.The directory portion of the path: {os.path.dirname(path)}")
            print(f"2.The filename portion of this path: {os.path.basename(path)}")
        else:
            print(f"The directory of the path: {path}")
    else:
        print("The path does not exist.")

path1 = r"C:\Users\Temirlan\Desktop\second sem\pp2\labs\lab 6\dir-and-files" 
path2 = r"C:\Users\Temirlan\Desktop\second sem\pp223"
path3 = r"C:\Users\Temirlan\Desktop\second sem\pp2\labs\lab 6\dir-and-files\ex1.py"
test_path_details(path1, "test1")
test_path_details(path2, "test2")
test_path_details(path3, "test3")
