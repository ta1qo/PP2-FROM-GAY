def write_list_to_file(file_path, list_items):
    with open(file_path, "w") as file:
        for item in list_items:
            file.write(f"{item}\n")


path = r"C:\Users\Temirlan\Desktop\second sem\pp2\labs\lab 6\dir-and-files\ex5.txt"
li = [
    "ACADEMIC POLICY",
    "Students are required:",
    "* to be respectful to the teacher and other students",
    "* to switch off mobile phones during classes;",
    "* DO NOT cheat. Plagiarized papers shall be graded with zero points!",
    "* to come to classes prepared and actively participate in classroom work; to meet the deadlines",
    "* to enter the room before the teacher starts the lesson; ",
    "* to attend all classes. No make-up tests or quiz are allowed unless there is a valid reason for missing it;",
]
# li = input().split(', ')
write_list_to_file(path, li)
