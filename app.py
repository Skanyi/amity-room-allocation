'''
Usage:
    add_person <person_id> <first_name> <last_name> <F|S> [wants_accomodation=N]
    create_room <room_type> <room_name>...
    reallocate_person <person_id> <new_room_name>
    load_people <filename>
    print_allocations [--o=filename]
    print_unallocated [--o=filename]
    print_room <room_name>
    save_state [--db=sqlite_database]
    load_state [--db=sqlite_database]
    quit
Options:
    -h, --help  Show this screen and exit
'''

from app.amity import Amity
import sys
import cmd
from docopt import docopt, DocoptExit


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

class AmityApplication(cmd.Cmd):
    prompt = "Amity -->"

    @docopt_cmd
    def do_create_room(self, arg):
        r_name = arg["<room_name>"]
        r_type = arg["<room_type>"]
        Amity.create_room(r_name.upper(), r_type.upper())


if __name__ == '__main__':
    AmityApplication().cmdloop()
