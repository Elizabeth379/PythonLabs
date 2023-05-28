import sys

from container import Container

if __name__ == '__main__':
    print("Hello! Welcome to our container of unique elements!!!")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

    username = input("Enter your username: ")
    storage = Container(username)

    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

    while True:
        command = input("Enter command: ")

        if not command:
            continue

        arguments = command.split()
        if arguments[0] == "add":
            if len(arguments) != 2:
                print("Invalid arguments for add command")
            else:
                storage.add(arguments[1])

        elif arguments[0] == "remove":
            if len(arguments) != 2:
                print("Invalid arguments for remove command")
            else:
                storage.remove(arguments[1])

        elif arguments[0] == "find":
            if len(arguments) < 2:
                print("Invalid arguments for find command")
            else:
                storage.find(*arguments[1:])

        elif arguments[0] == "list":
            storage.list()

        elif arguments[0] == "grep":
            if len(arguments) != 2:
                print("Invalid arguments for grep command")
            else:
                storage.grep(arguments[1])

        elif arguments[0] == "save":
            storage.save()
        elif arguments[0] == "load":
            storage.load()
        elif arguments[0] == "switch":
            if len(arguments) != 2:
                print("Invalid arguments for switch command")
            else:
                storage.switch(arguments[1])
        elif arguments[0] == "q":
            sys.exit(0)

        else:
            print("Invalid command")



