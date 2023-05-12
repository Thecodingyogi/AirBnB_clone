#!/usr/bin/python3
"""Program that contains the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Contains the entry point of the command interpreter."""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Exits the program by typing Ctrl-D."""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def emptyline(self):
        """Do nothing when an empty line is passed."""
        pass

    def help_quit(self):
        print('\n'.join(['Quit command to exit the program.']))
        print()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
