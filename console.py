#!/usr/bin/python3
"""A command line interpreter for AirBnb"""
import cmd
import shlex
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Command line interpreter class """

    prompt = '(hbnb) '
    __exist_classes = [
        "BaseModel",
        "User",
        "Amenity",
        "City",
        "State",
        "Place",
        "Review"
    ]

    def postloop(self):
        """ after cmdloop """
        storage.save()

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
        from models.base_model import BaseModel
        from models.user import User
        if not arg:
            print("** class name missing **")
        elif arg not in self.__exist_classes:
            print("** class doesn't exist **")
        else:
            match arg:
                case "BaseModel":
                    inst = BaseModel()
                case "User":
                    inst = User()
                case "Amenity":
                    from models.amenity import Amenity
                    inst = Amenity()
                case "City":
                    from models.city import City
                    inst = City()
                case "State":
                    from models.state import State
                    inst = State()
                case "Place":
                    from models.place import Place
                    inst = Place()
                case "Review":
                    from models.review import Review
                    inst = Review()
            print(inst.id)

    def help_create(self):
        """ help doc for create """
        print("Creates a new instance of the BaseModel ")
        print("Syntax: create BaseModel")

    def __validate(self, arg, args):
        """ validate args of an operation """
        if not arg:
            print("** class name missing **")
            return False
        elif args[0] not in self.__exist_classes:
            print("** class doesn't exist **")
            return False
        elif len(args) < 2:
            print("** instance id missing **")
            return False
        return True

    def do_show(self, arg):
        """ Prints the string representation of an instance"""
        args = shlex.split(arg)
        if not self.__validate(arg, args):
            return False
        else:
            all_insts = storage.all()
            inst = list(filter(
                lambda i: i.split('.')[1] == args[1]
                and i.split('.')[0] == args[0],
                all_insts.keys()
            ))
            if not len(inst):
                print("** no instance found **")
            else:
                print(str(all_insts[inst[0]]))

    def help_show(self):
        """ help doc for show command """
        print("Shows an existent instance of the BaseModel ")
        print("Syntax: show BaseModel 'id'")

    def do_destroy(self, arg):
        """ destroy BaseModel inst """
        args = shlex.split(arg)
        if not self.__validate(arg, args):
            return False
        else:
            # TODO: make it return copy and remove "store"
            all_insts = storage.all()
            inst = list(filter(
                lambda i: i.split('.')[1] == args[1]
                and i.split('.')[0] == args[0],
                all_insts.keys()
            ))
            if not len(inst):
                print("** no instance found **")
            else:
                del all_insts[inst[0]]
                storage.save(store=all_insts)

    def help_destroy(self):
        """ help doc for destroy """
        print("Deletes an instance based on the class name and id")
        print("Syntax: destroy 'Class' 'id'")

    def do_all(self, arg):
        """ Prints all string representation of all instances """
        if arg and arg not in self.__exist_classes:
            print("** class doesn't exist **")
        else:
            all_insts = storage.all()
            if arg:
                inst = list(map(lambda o: str(all_insts[o]), filter(
                    lambda i:  i.split('.')[0] == arg,
                    all_insts.keys()
                )))
                print(inst)
            else:
                print([str(obj) for obj in all_insts.values()])

    def help_all(self):
        """ help doc for all command """
        print("Prints all string representation of all instances")
        print("Syntax: all [class]")

    def do_update(self, arg):
        """ Updates an instance based on the class name and id """
        args = shlex.split(arg)
        if not self.__validate(arg, args):
            return False
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            all_insts = storage.all()
            inst = filter(
                lambda i: i.split('.')[1] == args[1]
                and i.split('.')[0] == args[0],
                all_insts.keys()
            )
            inst = next(inst, None)
            if not inst:
                print("** no instance found **")
            else:
                key = args[2]
                val = args[3]
                found_val = all_insts[inst].to_dict().get(key, None)
                if not found_val or type(found_val) is type(val):
                    setattr(all_insts[inst], key, val)
                elif isinstance(found_val, int):
                    setattr(all_insts[inst], key, int(val))
                elif isinstance(found_val, float):
                    setattr(all_insts[inst], key, float(val))

    def help_update(self):
        """ help doc for update """
        print("Updates an instance based on the class name and id")
        print("Syntax: update <class name> <id>\
              <attribute name> '<attribute value>'")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
