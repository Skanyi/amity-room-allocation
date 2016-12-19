from .person import *
from .room import *
import random
from db.migration import (Base, Person, Room, DatabaseCreator, UnAllocated,
                          OfficeAllocations, LivingSpaceAllocations)


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
        if room_name in Amity.all_rooms:
            return 'Room already exists'
        elif room_type == 'O':
            Amity.all_rooms.append(room_name.upper())
            Amity.office_rooms[room_name.upper()]
            current_room = Office()
            print('%s created succesfully' % room_name)

        elif room_type == 'L':
            Amity.all_rooms.append(room_name.upper())
            Amity.ls_rooms[room_name.upper()]
            current_room = LivingSpace()
            print('%s created succesfully' % room_name)
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

        elif position.upper() == 'F' and wants_accomodation.upper() == 'N':
            Amity.all_people[person_id] = full_name.upper()
            Amity.fellows.append(full_name.upper())
            fellow = Fellow(person_id, firstname, lastname)
            random_office = Amity.generate_random_office()
            Amity.office_rooms[random_office].append(full_name.upper())
            print("Added: " + full_name + " and allocated them to: " + random_office)
            Amity.unallocated_person.append(full_name.upper())
            print(full_name + " does not need a living space, added to unallocated")

        elif position.upper() == 'F' and wants_accomodation.upper() == 'Y':
            Amity.all_people[person_id] = full_name.upper()
            Amity.fellows.append(full_name.upper())
            fellow = Fellow(person_id, firstname, lastname)
            random_office = Amity.generate_random_office()
            Amity.office_rooms[random_office].append(full_name.upper())
            print("Added: " + full_name + " and allocated them to: " + random_office)
            random_ls = Amity.generate_random_living_space()
            Amity.ls_rooms[random_ls].append(full_name.upper())
            print("Added: " + full_name + " and allocated them to: " + random_ls)

        elif position.upper() == 'S' and wants_accomodation.upper() == 'N':
            Amity.all_people[person_id] = full_name.upper()
            Amity.staffs.append(full_name.upper())
            staff = Staff(person_id, firstname, lastname)
            random_office = Amity.generate_random_office()
            Amity.office_rooms[random_office].append(full_name.upper())
            print("Added: " + full_name + " and allocated them to: " + random_office)

        elif position.upper() == 'S' and wants_accomodation.upper() == 'Y':
            Amity.all_people[person_id] = full_name.upper()
            Amity.staffs.append(full_name)
            staff = Staff(person_id, firstname, lastname)
            random_office = Amity.generate_random_office()
            Amity.office_rooms[random_office].append(full_name.upper())
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
                for line in people_file:
                    people_details = line.split()
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
                print('Selected %s is full' % random_room_name)
                return
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
                print('Selected %s is full' % random_room_name)
                return
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
        if full_name in Amity.all_people.values():
            for room, name in list(Amity.office_rooms.items()):
                print(name)
                if full_name in name:
                    Amity.office_rooms[room].remove(full_name)
                    Amity.office_rooms[new_room_name].append(full_name)
                    print('%s has been reallocated to %s ' % (full_name, new_room_name))
                    break
                else:
                    print('%s does not have an office room' % full_name)
        else:
            print('No person called %s in offices' % full_name)

    @staticmethod
    def reallocate_person_from_ls(full_name, new_room_name):
        '''
        use the person full name to remove the person from one livingspace
        to another, should not reallocate to the same room or a room that is full
        '''
        if full_name in Amity.all_people.values():
            for room, name in list(Amity.ls_rooms.items()):
                if full_name in name:
                    Amity.ls_rooms[room].remove(full_name)
                    Amity.ls_rooms[new_room_name].append(full_name)
                    print('%s has been reallocated to %s ' % (full_name, new_room_name))
                    break
                else:
                    print('%s does not have a living space room' % full_name)
        else:
            print('No person called %s in living space' % full_name )


    @staticmethod
    def print_room(room_name):
        '''
        prints a room and all the people allocated to that room
        '''

        if room_name.upper() in Amity.office_rooms.keys():
            print(room_name.upper())
            print('-' * 50)
            print(', '.join(Amity.office_rooms[room_name.upper()]))

        if room_name.upper() in Amity.ls_rooms.keys():
            print(room_name.upper())
            print('-' * 50)
            print(' ,'.join(Amity.ls_rooms[room_name.upper()]))


    @staticmethod
    def print_allocations(filename=''):
        '''
        prints a list of all the people that have been allocated a room
        '''

        if filename:
            with open(filename, 'w') as allocation:
                print("\nWriting to the file .., \n")
                allocation.write('People in offices \n')
                for room, name in Amity.office_rooms.items():
                    allocation.write(room + '\n')
                    allocation.write('-' * 50 + '\n')
                    allocation.write(', '.join(name) + '\n')
                allocation.write('=' * 75 + '\n')

                allocation.write('People in living space \n')
                for room, name in Amity.ls_rooms.items():
                    allocation.write(room + '\n')
                    allocation.write('-' * 50 + '\n')
                    allocation.write(', '.join(name) + '\n')
        else:
            print('People in office')
            for room, name in Amity.office_rooms.items():
                print(room)
                print('-' * 50)
                print(', '.join(name))
                print('=' * 50)

            print('People in Living space rooms')
            for room, name in Amity.ls_rooms.items():
                print(room)
                print('-' * 50)
                print(', '.join(name))
                print('=' * 50)

    @staticmethod
    def print_unallocated(filename=''):
        '''
        prints a list of people that have not been allocated to a room yet
        '''
        if filename:
            with open(filename, 'w') as unallocated:
                print("\nWriting to the file .., \n")
                unallocated.write('People who are not allocated a living space \n')
                unallocated.write('-' * 50 + '\n')
                unallocated.write(', '.join(Amity.unallocated_person))
        else:
            print('People not in an room')
            print(', '.join(Amity.unallocated_person))

    @staticmethod
    def load_state():
        '''
        loads the data from database to the app
        '''
        pass

    @staticmethod
    def save_state(db_name=None):
        '''
        Saves the data in the app to the database
        '''
        if db_name:
            db = DatabaseCreator(db_name)
        else:
            db = DatabaseCreator('default_db')

        Base.metadata.bind = db.engine
        db_session = db.session()

        for person in Amity.all_people:
            person_to_save = Person(
                name = person.full_name,
                position = person.position
            )
            db_session.merge(person_to_save)

        for room in Amity.all_rooms:
            room_to_save = Room(
                name = room.name,
                room_type = room.room_type,
                max_occupants = room.max_occupants
            )
            db_session.merge(person_to_save)


Amity.create_room('PHP', 'L')
Amity.create_room('Narnia', 'O')
Amity.create_room('GO', 'L')
Amity.create_room('Carmel', 'O')
Amity.create_room('JAVA', 'L')
Amity.create_room('Hogwarts', 'O')
Amity.add_person(8, 'steve', 'WAWERU', 'F')
Amity.add_person(15, 'Joseph', 'Njogu', 'F', 'Y')
Amity.add_person(3, 'douglas', 'mbugua', 'S')
Amity.add_person(4, 'Joshua', 'Mwaniki', 'S', 'Y')
Amity.add_person(5, 'Angie', 'Mugo', 'F')
Amity.add_person(6, 'Anthony', 'Yayo', 'F', 'Y')
