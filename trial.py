detail = "1 OLUWAFEMI SULE FELLOW"

detail = detail.split()

if len(detail) == 5:
    print('a fellow')
else:
    print('Staff')

import random
d = {'r1': ['steve'], 'r2': ['doug'], 'r3': ['angi'], 'r4': ['mbug'], 'r5': ['kanyi']}

def rellocate(full_name, new_room):
    for room, name in d.items():
        if full_name in name:
            d[room].remove(full_name)
            d[new_room].append(full_name)

            break
        else:
            print('No person with that name')

rellocate('kanyi', 'r2')
print(d)
