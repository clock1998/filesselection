import os
import configparser
import subprocess


def config():
    config = configparser.ConfigParser()
    config.read("config.ini")
    directory_to_watch = config.get("general", "directory_to_watch")
    if directory_to_watch == "":
        p = subprocess.run(["echo", "%userprofile%"], shell=True, text=True, capture_output=True)
        directory_to_watch = p.stdout.replace("\n", "")
        directory_to_watch = directory_to_watch + "\Downloads"
        print(directory_to_watch)
        while not os.path.isdir(directory_to_watch):
            print("Invalid directory!")
            directory_to_watch = input("Enter your path: ")
        config.set("general", "directory_to_watch", directory_to_watch)
    else:
        while not os.path.isdir(directory_to_watch):
            print("Invalid directory!")
            directory_to_watch = input("Enter your path: ")
        config.set("general", "directory_to_watch", directory_to_watch)
    # categories = config.get("general", "categories")
    # print("Use default categories (%s)?" % categories)
    # default = input("(Press Enter to use defaults. Press N to enter your own.)")
    # while default.lower() != "n" and default.lower() != "":
    #     print("Invalid Input")
    #     default = input("(Press Enter to use defaults. Press N to enter your own.)")
    #
    # if default == "":
    #     with open('config.ini', 'w') as configfile:
    #         config.write(configfile)
    #     return
    # elif default.lower() == "n" or default.lower() == "no":
    #     print("Enter your categories, separated by comma without space:")
    #     print("Example:video,image,document")
    #     raw_input = input()
    #     # raw_input = raw_input.split(",")
    #     # categories = []
    #     # for i in raw_input:
    #     #     categories.append(i.strip())
    #
    # print("Please verify:")
    # print(raw_input)
    # change = input("Press Enter to continue. Press M to change.")
    # while change.lower() != "m" and change.lower() != "":
    #     print("Invalid Input")
    #     change = input("Press Enter to continue. Press M to change.")
    # if change == "":
    #     config.set("general", "categories", raw_input)
    #     with open('config.ini', 'w') as configfile:
    #         config.write(configfile)
    # elif change.lower() == "m":
    #     print("Enter your categories, separated by comma without space:")
    #     print("Example:video,image,document")
    #     raw_input = input()
    #     config.set("general", "categories", raw_input)
    with open('config.ini', 'w') as configfile:
        config.write(configfile)


config()
