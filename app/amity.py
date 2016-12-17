from .person import *
from .room import *
import random

class Amity(object):
    office_rooms = defaultdict(list)
    ls_rooms = defaultdict(list)
    all_rooms  = []
    staffs = []
    fellows = []
    all_people = {}
    unallocated_person = []


    @staticmethod
    def create_room(room_name, room_type):
        '''
        Check that the room does not exist and determine what type of room it is
        '''
        if room_name.upper() in Amity.all_rooms:
            print('Room already exists')
            return 'Room already exists'
        elif room_type.upper() == 'O':
            Amity.all_rooms.append(room_name.upper())
            Amity.office_rooms[room_name.upper()]
            current_room = Office()
        elif room_type.upper() == 'L':
            Amity.all_rooms.append(room_name.upper())
            Amity.ls_rooms[room_name.upper()]
            current_room = LivingSpace()
        else:
            print('%s is an invalid room type' % room_type)

    @staticmethod
    def add_person(person_id, firstname, lastname, position, wants_accomodation = 'N'):
        '''
        Add person details to the system
        '''
        full_name = firstname + " " + lastname
        if person_id in Amity.all_people.keys():
            print ('Person with %s id already exist.' % person_id)

        elif position.upper() == 'F' and wants_accomodation == 'N':
            Amity.all_people[person_id] = full_name
            Amity.fellows.append(full_name)
            fellow = Fellow(person_id, firstname, lastname)
            random_office = Amity.generate_random_office()
            Amity.office_rooms[random_office].append(full_name)
            print("Added: " + full_name + " and allocated them to: " + random_office)
            Amity.unallocated_person.append(full_name)
            print(full_name + " does not need a living space, added to unallocated")

        elif position.upper() == 'F' and wants_accomodation == 'Y':
            Amity.all_people[person_id] = full_name
            Amity.fellows.append(full_name)
            fellow = Fellow(person_id, firstname, lastname)
            random_office = Amity.generate_random_office()
            Amity.office_rooms[random_office].append(full_name)
            print("Added: " + full_name + " and allocated them to: " + random_office)
            random_ls = Amity.generate_random_living_space()
            Amity.ls_rooms[random_ls].append(full_name)
            print("Added: " + full_name + " and allocated them to: " + random_ls)

        elif position.upper() == 'S' and wants_accomodation == 'N':
            Amity.all_people[person_id] = full_name
            Amity.staffs.append(full_name)
            staff = Staff(person_id, firstname, lastname)
            random_office = Amity.generate_random_office()
            Amity.office_rooms[random_office].append(full_name)
            print("Added: " + full_name + " and allocated them to: " + random_office)

        elif position.upper() == 'S' and wants_accomodation == 'Y':
            Amity.all_people[person_id] = full_name
            Amity.staffs.append(full_name)
            staff = Staff(person_id, firstname, lastname)
            random_office = Amity.generate_random_office()
            Amity.office_rooms[random_office].append(full_name)
            print("Added: " + full_name + " and allocated them to: " + random_office)
            print('Staff cannot be llocated a living space')

        else:
            print('%s is not a valid position.' % position)

    @staticmethod
    def load_people(filename):
        '''
        Loads people to the system from a text file.
        '''
        if filename:
            with open(filename) as people_file:
                people_details = people_file.readlines()
                people_details = people_details.split()
                if len(people_details) == 5:
                    Amity.add_person(person_id=people_details[0], firstname=people_details[1], lastname=people_details[2],
                    position=people_details[3], wants_accomodation=people_details[4])
                elif len(people_details) == 4:
                    Amity.add_person(person_id=people_details[0], firstname=people_details[1], lastname=people_details[2],
                    position=people_details[3], wants_accomodation='N')
                else:
                    print('Cannot process the data provided')
        else:
            print('Provide a file, please')


    @staticmethod
    def generate_random_office():
        '''
        Generates a random office that is not full
        '''
        if len(Amity.office_rooms) > 0:
            random_room_name = random.choice(list(Amity.office_rooms))
            if len(Amity.office_rooms[random_room_name]) >= 6:
                return 'Selected %s is full' % random_room_name
            else:
                return random_room_name
        else:
            return 'There are no office rooms available'

    @staticmethod
    def generate_random_living_space():
        '''
        Generate a random living space that is not fulloccupied
        '''
        if len(Amity.ls_rooms)> 0:

            random_room_name = random.choice(list(Amity.ls_rooms))
            if len(Amity.ls_rooms[random_room_name]) >= 4:
                return 'Selected %s is full' % random_room_name
            else:
                return random_room_name
        else:
            return 'There are no living space available'

    @staticmethod
    def reallocate_person_from_office(full_name, new_room_name):
        '''
        use the person full name to remove the person from one office
        to another
        '''
        for room, name in Amity.office_rooms.items():
            if full_name in name:
                Amity.office_rooms[room].remove(full_name)
                Amity.office_rooms[new_room_name].append(full_name)
                break
            else:
                print('No person with that name')

    @staticmethod
    def reallocate_person_from_ls(full_name, new_room_name):
        '''
        use the person full name to remove the person from one livingspace
        to another
        '''
        for room, name in Amity.ls_rooms.items():
            if full_name in name:
                Amity.ls_rooms[room].remove(full_name)
                Amity.ls_rooms[new_room_name].append(full_name)
                break
            else:
                print('No person with that name')


    @staticmethod
    def print_room(room_name):
        '''
        prints a room and all the people allocated to that room
        '''
        print('People in php')
        if room_name in Amity.office_rooms.keys():
            print(room_name)
            print('------------------------------------')
            print(', '.join(Amity.office_rooms[room_name]))

        if room_name in Amity.ls_rooms.keys():
            print(room_name)
            print('------------------------------------')
            print(' ,'.join(Amity.ls_rooms[room_name]))


    @staticmethod
    def print_allocation():
        '''
        prints a list of all the people that have been allocated a room
        '''
        print('People in offices')
        for room, name, in Amity.office_rooms.items():
            print(room)
            print('.................................\n')
            print(', '.join(name))

        print('People in Living space rooms')
        for room, name, in Amity.ls_rooms.items():
            print(room)
            print('.................................\n')
            print(', '.join(name))

    @staticmethod
    def print_unallocated():
        '''
        prints a list of people that have not been allocated to a room yet
        '''
        print('People not in an room')
        for name in Amity.unallocated_person:
            print(name)


    def load_state(self):
        '''
        loads the data from database to the app
        '''
        pass

    def save_state(self):
        '''
        Saves the data in the app to the database
        '''
        pass


Amity.create_room('PHP', 'l')
Amity.create_room('Narnia', 'o')
Amity.add_person(1, 'steve', 'kanyi', 'f')
Amity.add_person(2, 'Joseph', 'Njogu', 'f', 'Y')
print(Amity.office_rooms)
print(Amity.ls_rooms)
Amity.print_allocation()
Amity.print_unallocated()
Amity.print_room('PHP')
