def copy_file(source_path, destination_path):
    with open(source_path, "r") as source, open(destination_path, "w") as destination:
        destination.write(source.read())
        destination.write(f"\nContents from {source_path} successfully copied to {destination_path}")

firstFile = r"C:\Users\Temirlan\Desktop\second sem\pp2\labs\lab 6\dir-and-files\ex7_from_here.txt"
secondFile = (r"C:\Users\Temirlan\Desktop\second sem\pp2\labs\lab 6\dir-and-files\ex7_to_here.txt")

copy_file(firstFile, secondFile)
