#!/usr/bin/python3
"""
This is module define the Cmd class for command line in python
"""

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """
        Class  HBNBCommand
        command line for A&B project
    """

    prompt = '(hbnb) '

    def emptyline(self):
        """ Empty line """
        pass

    def do_quit(self, arg):
        """
            do quit command
        """
        return True

    def do_EOF(self, arg):
        """
            command to end of file
        """
        print("^D")
        return True

    def do_create(self, arg):
        """
            create a new intance of base model and 
            saves it in the file.json
        """
        if arg and  arg == "BaseModel":
            cl_name = eval(arg + '()')
            cl_name.save()
        elif not arg:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")


    def help_create(self):
        print("-- Sintax: create class_name")
        print("creat a and save instance for BaseModel")

    def help_EOF(self):
        """
            help command to  end of file
        """
        print("End of File")

    def help_quit(self):
        """
            help command quit
        """
        print("Quit command to exit the program")
        print()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
