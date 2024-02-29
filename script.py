import os, shutil

# 1 Prompt for a path.

while True:
    try:
        path = input("Enter a path: ")
        # 2 Get the files from the path.
        files = os.listdir(path)
        break
    except FileNotFoundError:
        print("The path is incorrect or doesn't exist")

# 3 loop the files and:
for file in files:
    while True:
        try:
            #4 Create a path to the file
            file_path = path + "\\" + file

            #5 Separate the file into his name and extension
            name, extension = file.split(".")

            # 6 Create a path to a possible folder of that file
            folder = path + "\\" + extension.upper()

            # 7 Check if the folder exists and:
            if os.path.exists(folder):
                #8 If the folder exist, move the file inside
                shutil.move(file_path, folder)
            # 8 else, create a new folder and move the file into it.
            else:
                os.mkdir(folder)
                shutil.move(file_path, folder)

            break
        except ValueError:
            print(f"{file} is a folder or an invalid file")
            break

print("Program finished")


# addtional stuff:
# 1 Create a regex for the input so it doesn't allows an invalid path
# 2 Rename certain files like the ones that come out of scrnli to a specific name


# ERROR:
# FileNotFoundError: [WinError 2] The system cannot find the file specified: 'bookmarks_1_15_24.html' -> 'C:\\Users\\Administrator\\Downloads\\test/html\\bookmarks_1_15_24.html'
