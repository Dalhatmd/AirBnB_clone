#!/usr/bin/python3
"""A command line interpreter for AirBnb"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Command line interpreter class """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Exit program"""
        return True

    def help_quit(self):
        """ help doc for quit """
        print("Quit command to exit the program\n")

    def do_EOF(self, arg):
        """Exit program"""
        print()
        return True

    def help_EOF(self):
        """ help doc for EOF """
        print("EOF or Ctrl+D command to exit the program\n")

    def emptyline(self):
        """ Do nothing on emptyline """
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel """
        available = ["BaseModel"]
        if not arg:
            print("** class name missing **")
        elif arg not in available:
            print("** class doesn't exist **")
        else:
            inst = BaseModel()
            print(inst.id)

    def help_create(self):
        """ help doc for create """
        print(" Creates a new instance of the BaseModel ")
        print("Syntax: create BaseModel")

    def postloop(self):
        """ after loop """
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
