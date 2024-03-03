import os

def generate_26_text_files(folderName):
    new_path = (f"C:\\Users\\Temirlan\\Desktop\\second sem\\pp2\\labs\\lab 6\\dir-and-files\\{folderName}")
    if (not os.access(new_path, os.F_OK)):
        os.makedirs(new_path)
    for i in range(65, 91):
        f = open(f"{new_path}\\{chr(i)}.txt", "w")
        f.write(f"This is {chr(i)}`s txt file, which situated in new folder named: {folderName}.")
        f.close()
        
name = input("Input a name for new folder: ")
generate_26_text_files(name)        
