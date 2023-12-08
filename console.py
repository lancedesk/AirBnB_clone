#!/usr/bin/python3
"""
Interactive shell for AirBnB project.
"""

import cmd


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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
