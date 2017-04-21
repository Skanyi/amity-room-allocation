import sqlite3
detail = "1 OLUWAFEMI SULE FELLOW"

detail = detail.split()

if len(detail) == 5:
    print('a fellow')
else:
    print('Staff')

import random
d = {'r1': ['steve', 'chela'], 'r2': ['doug'], 'r3': ['angi'], 'r4': ['mbug'], 'r5': ['kanyi']}
print(d)

if 'r2' in d:
    print('chela found')
else:
    print('Chela not found')

def save_state(database = None):
    if not database:
        pass



def rellocate(full_name, new_room):
    for room, name in d.items():
        if full_name in name:
            d[room].remove(full_name)
            d[new_room].append(full_name)

            break
        else:
            print('No person with that name')

rellocate('chela', 'r3')
print(d)
def print_allocations(filename):
    if rn in d:
        print(d[rn])
    else:
        print('room not found')


filename = ""
if filename:
    print('yes')
else:
    print('no')


dl = {'n1': [1,5,7], 'n2': [2,6,8]}

num = [n for n in dl.values()]
print(num)
if 6 in num:
    print('found')

else:
    print('not found')


'''def introduction():
    print (border)
    print "WELCOME TO AMITY SPACE ALLOCATION!".center(70)
    print (spacer)
    print (spacer)
    print "ROOM ALLOCATION COMMANDS:".center(70)
    print spacer
    print "1. create_room (Living|Office) <room_name>...".center(70)
    print "2. add_person " \
        "< first_name> <last_name> (Fellow|Staff) " \
        "[<wants_space>]".center(70)
    print "3. reallocate_person <employee_id> <new_room_name>".center(70)
    print "4. load_people <filename>".center(70)
    print "5. print_allocations [--o=filename.txt]".center(70)
    print "6. print_unallocated [--o=filename.txt]".center(70)
    print "7. print_room <room_name>".center(70)
    print "8. save_state [--db=sqlite_database]".center(70)
    print "9. load_state <sqlite_database>".center(70)
    print spacer
    print "OTHER COMMANDS:".center(70)
    print spacer
    print "1. help".center(70)
    print "2. quit".center(70)
    print spacer
    print border
intro = introduction()
'''
