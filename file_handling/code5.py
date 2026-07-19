#CRUD operations on File

from pathlib import Path
import os

def show_all_existing_file_folder():
    path = Path('') #empty space means i will get the path of the current file
    items = list(path.rglob('*'))   #recursive glob function, recursively reads all the files and folders name in the folder
    for i, items in enumerate(items): #to save items and list separately we use i(index) and enumerate(values)
        print(f"{i+1}, {items}")

def createfile():
    try:
        show_all_existing_file_folder()
        name = input("please enter the name of the file you want to create: ")
        p = Path(name) #include the name in path
        if not p.exists():
            with open(p,"w") as fs:
                data = input("what do you want to write: ")
                fs.write(data)
            print("FILE CREATED SUCCESSFULLY")
        else:
            print("File already exists")
     

    except Exception as err:
        print(f"an error occured: {err}")


def readfile():
    try:
        show_all_existing_file_folder()
        name = input("name the file you want to read: ")
        p = Path(name) #if file exists then the path will be stored in p else a path will be created that will be stored in p
        if p.exists() and p.is_file():
            read = open(p,'r')
            print(read.read())
            print("FILE READ SUCCESSFULLY")
        else:
            print("file does not exists, cant read")

    except Exception as err:
        print(f"an error occured: {err}")

def updatefile():
    try:
        show_all_existing_file_folder()
        name = input("Enter the file name: ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("1. change overwriting the data \n2.appending the content\n 3.changing th file name ")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                file = open(p,'w')
                data = input("write: ")
                file.write(data)
                print("ADDED SUCCCESSFULLY")
                file.close()

            elif choice == 2:
                file = open(p,"a")
                data = input("append: ")
                file.write("\n"+data)
                print("ADDED SUCCCESSFULLY")
                file.close()

            elif choice == 3:
                name2= input("give new name: ")
                p2 = Path(name2)
                p.rename(p2)

            else:
                print("incorrect choice")

    except Exception as err:
        print(f"an error occured: {err}")

def deletefile():
    try:
        show_all_existing_file_folder()
        name = input("enter the file name: ")
        p = Path(name)

        if p.exists() and p.is_file():
            os.remove(p)
            print("file removed successfully")

        else:
            print("no such file exists")
    
    except Exception as err:
        print("An error occured: {err}")


print("enter 1 to create a file")
print("enter 2 to read a file")
print("enter 3 to update a file")
print("enter 4 to delete a file")

a = int(input("enter your choice: "))

if a == 1:
    createfile()

elif a == 2:
    readfile()

elif a == 3:
    updatefile()

elif a == 4:
    deletefile()

else:
    print("incorrect choice")