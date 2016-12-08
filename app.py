from app.amity import Amity

def start():
    print('Welcome to the my app')
    print('select \n 1 : to create a room \n 2 : to add a person')

    choice = int(input('What do you want to do? >>'))
    if choice == 1:
        Amity.create_room()
    elif choice == 2:
        Amity.add_person()
    else:
        start()

start()
