import os
import pathlib
import pyperclip
from os.path import exists



def main():

    preview = True
    debug = False


    # folder path
    dir_path = str(pathlib.Path(__file__).parent.absolute()) + "/texts"
    count = 0
    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
    yourfile = os.listdir(dir_path)
    if exists(dir_path + "/../config.dat"):
        with open(dir_path + "/../config.dat",'r', errors="ignore", encoding='utf8') as f:
            lines = f.readlines()
            f.close()
        if lines[0] == "preview: False\n":
            preview = False 
        if lines[1] == "debug: True\n":
            debug = True 



    if debug:
        print("--- Debug data ---")
        print('File count:', count)
        print (yourfile)
        print("--- End ---")

    print("Welcome!")
    print("Copies: ")
    print ("")
    for i in range(count):
        if ".txt" in yourfile[i]:
            print(" - " + yourfile[i].replace(".txt",""))
            
            with open(dir_path + "/" + yourfile[i],'r', errors="ignore", encoding='utf8') as f:
                lines = f.readlines()
                f.close()
                if preview:
                    if len(lines) > 5:
                        for j in range(5):
                            print(lines[j], end="")
                        print("...")
                    else:
                        for j in range(len(lines)):
                            print(lines[j], end="")
                    print()

    print()
    print("Please insert the name of the thing you want to copy")
    selected = input()
    goesright = False
    for i in range(count):
        if ".txt" in yourfile[i]:
            if selected == yourfile[i].replace(".txt",""):
                with open(dir_path + "/" + yourfile[i],'r', errors="ignore", encoding='utf8') as f:
                    lines = f.read()
                    f.close()
                pyperclip.copy(lines)
                print("copied")
                goesright = True
    if goesright == False:
        print("your file doesn't exist")
    input()

while True:
    main()
    os.system('cls')
