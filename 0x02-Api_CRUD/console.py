#!/usr/bin/env python3
"""Management console for the Friendly Gadget project"""
import cmd
import shlex
from models.user import User
from models import storage


class HGNX(cmd.Cmd):
    """FgConsole Module"""

    __clx = {"User": User}

    def __init__(self):
        """The constructor for HBNBCommand class."""
        super().__init__()
        self.prompt = "[HGNX]: "

    def do_EOF(self, arg):
        """Exits console"""
        print("\nExiting....\nDone")
        return True

    def help_EOF(self):
        """EOF documenataion"""
        print("Syntax: Ctrl + D")
        print("Terminates the program")

    def emptyline(self):
        """overwriting the emptyline method"""
        return False

    def help_emptyline(self):
        """emptyline doucmentation"""
        print("Ignores empty lines")

    def do_quit(self, arg):
        """Quit command to exit the program"""
        print("Quiting console...")
        return True

    def help_quit(self):
        """quit documentation"""
        print("Syntax: quit")
        print("Terminates and exit the program")
        return

    """Important Management functions"""
    def do_create(self, argz):
        """Creates a new instance of a class"""
        usage = "Usage: create <obj_class> <obj_name>"
        # check if argumments is empty
        if argz is None or argz == "":
            print("Error: Class cannot be empty\n{}".format(usage))
            return
        # check if a list was passed as argument
        data = argz.split(" ")
        if len(data) == 1:
            print("Error: Class name cannot be empty\n{}".format(usage))
            return
        # check if class name is valid
        clx = argz.split(" ", 1)[0].strip("'\"")
        data = argz.split(" ",1)[1].strip("'\"")
        if clx not in self.__clx:
            print("Error: Invalid class name\n{}".format(usage))
            return
        # create new instance
        obj = storage.new(self.__clx[clx], data)
        storage.save()
        print(obj.to_dict())
        return

    
    def do_show(self, argz):
        """
        Prints the string representation of an instance
        show <class> <id>
        """
        usage = "Usage: show <class> <id>"
        tokens = shlex.split(argz)
        if len(tokens) == 0:
            print("Error: Missing class name\n{}".format(usage))
            return
        if len(tokens) == 1:
            print("Error: Missing object id\n{}".format(usage))
            return
        if len(tokens) > 2:
            print("Error: Too many arguments\n{}".format(usage))
            return
        clx = tokens[0]
        id = tokens[1]
        # validate class name
        if clx not in HGNX.__clx:
            print("Error: Invalid class name")
            return
        # validate id
        if storage.get(HGNX.__clx[clx], id) is None:
            print("Error: Invalid id")
            return
        obj = storage.get(HGNX.__clx[clx], id)
        print(obj.to_dict())


    def help_show(self):
        """
        This will print out the dictionary of the all the attributes
        of a given class and it's id
        show documentation
        """
        usage = "show Brand f0ca205f-31dc-40e4-ac82-09a83d75bcaa"
        print("show <class> <id>")
        print("id is the id of the obj\nExample: {}".format(usage))
        return

    def do_delete(self, argz):
        """Delete content from the database"""
        usage = "Usage: delete <class> <id>"
        tokens = shlex.split(argz)
        if len(tokens) == 0:
            print("Error: Missing class name\n{}".format(usage))
            return
        if len(tokens) == 1:
            print("Error: Missing object id\n{}".format(usage))
            return
        if len(tokens) > 2:
            print("Error: Too many arguments\n{}".format(usage))
            return
        clx = tokens[0]
        id = tokens[1]
        # validate class name
        if clx not in HGNX.__clx:
            print("Error: Invalid class name")
            return
        # validate id
        if storage.get(HGNX.__clx[clx], id) is None:
            print("Error: Invalid id")
            return
        # get the object
        obj = storage.get(HGNX.__clx[clx], id)
        storage.delete(obj)
        storage.save()
        print("Object deleted successfully")
        return

    def do_all(self, argz):
        """Prints all string representation of all instances"""
        usage = "Usage: all <class>"
        tokens = shlex.split(argz)
        obj_list = []
        if len(tokens) == 0:
            print("Error: Missing class name\n{}".format(usage))
            return
        if len(tokens) > 1:
            print("Error: Too many arguments\n{}".format(usage))
            return
        clx = tokens[0]
        # validate class name
        if clx not in HGNX.__clx:
            print("Error: Invalid class name")
            return
        # get the objects
        objs = storage.all(HGNX.__clx[clx])
        if len(objs) == 0:
            print("No objects found")
            return
        for obj in objs.values():
            obj_list.append(obj.to_dict())
        for disp in obj_list:
            print(disp)
            print()
        return

    def do_update(self, argz):
        """Update a given object"""
        usage = "Usage: update <class=Aaaaa> <id> <attribute> <value>"
        tokens = shlex.split(argz)
        if len(tokens) == 0:
            print("Error: Missing class name\n{}".format(usage))
            return
        if len(tokens) == 1:
            print("Error: Missing object id\n{}".format(usage))
            return
        if len(tokens) == 2:
            print("Error: Missing attribute\n{}".format(usage))
            return
        if len(tokens) == 3:
            print("Error: Missing value\n{}".format(usage))
            return

        clx = tokens[0]
        id = tokens[1]
        attr = tokens[2]
        val = tokens[3]
        # validate class name
        if clx not in HGNX.__clx:
            print("Error: Invalid class name")
            return
        # validate id
        if storage.get(HGNX.__clx[clx], id) is None:
            print("Error: Invalid id")
            return
        if clx == "User":
            if attr == "user_name":
                setattr(HGNX.__clx[clx], attr, val)
                storage.save()
                print("{} Object updated successfully".format(clx))
                return
            else:
                print("Error: Invalid attribute\n{}".format(usage))
                return


if __name__ == "__main__":
    HGNX().cmdloop()
