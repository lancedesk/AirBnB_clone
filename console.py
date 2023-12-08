#!/usr/bin/python3
"""
Interactive shell for AirBnB project.
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_help(self, arg):
        """Display help message"""
        print("Help message goes here.")

    def do_quit(self, arg):
        """Quit the shell"""
        return True

    def do_EOF(self, arg):
        """Exit on EOF (Ctrl-D)"""
        print("")
        return True

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        cls = storage.classes()[class_name]
        new_instance = cls()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(class_name, args[1])
        objs_dict = storage.all()
        if key in objs_dict:
            print(objs_dict[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if not arg or arg not in storage.classes():
            print("** class doesn't exist **")
        else:
            instances = storage.all().values()
            filtered_instances = [
                str(inst) for inst in instances if type(inst).__name__ == arg
            ]
            print(filtered_instances)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in storage.all():
                    print("** no instance found **")
                elif len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    instance = storage.all()[key]
                    attribute_name = args[2]
                    if hasattr(instance, attribute_name):
                        setattr(instance, attribute_name, eval(args[3]))
                        instance.save()
                    else:
                        print("** attribute doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
