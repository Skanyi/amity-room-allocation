detail = "1 OLUWAFEMI SULE FELLOW"

detail = detail.split()

if len(detail) == 5:
    print('a fellow')
else:
    print('Staff')

import random
d = {'r1': ['steve', 'kanyi'], 'r2': ['doug'], 'r3': ['angi'], 'r4': ['mbug'], 'r5': ['kanyi']}

for r, v in d.items():
    print(r)
    print('...............................................\n')
    print(', '.join(v))
