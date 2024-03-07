import os, shutil
from get_dw_folder import get_download_folder

import re

while True:
    try:
        """in case you want to make the path selectable for the user
        path = input("Enter a path: ")"""

        # 1 Get the path either to the downloads folder or the one given by the user
        path = get_download_folder()

        # 2 Assign the files inside the path to a variable
        files = os.listdir(path)
        break

    except FileNotFoundError:
        print("The path is incorrect or doesn't exist")

# 3 loop the files and:
for file in files:
    while True:
        try:
            # 4 Separate the file into his name and extension
            name, extension = file.split(".")

            # 5 Assign the path of the file to a variable
            file_path = path + "\\" + file

            # This variable contains substrings that could be find on files downloaded  from this site.
            # In my case i want to have them separated from files with the same extension
            # Change them to something you use or delete them 
            pattern = "scrnli|unsplash|z-library"
            
            #6 Check if the file is from one of the specified sources, 
            # if it exists change extension to the string found.
            special_name = re.search(pattern, name.lower())

            if special_name:
                extension = special_name.group(0)


            # 7 Create a path to a possible folder of that file
            folder = path + "\\" + extension.upper()

            # 8 Check if the folder exists and:
            if os.path.exists(folder):
                # 9 If the folder exist, move the file inside
                shutil.move(file_path, folder)
            # 10 else, create a new folder and move the file into it.
            else:
                os.mkdir(folder)
                shutil.move(file_path, folder)

            break
        except ValueError:
                # If one of the elements inside the directory doesn't have an extension
                # It raises a ValueError and goes to the next element
                break

print("Program finished")


# Stuff that could be added: 
# 1 Rename certain files like the ones that come out of scrnli to a specific name
# 2 Make it so it runs everytime you download something (Could be added but it would consume resources)
