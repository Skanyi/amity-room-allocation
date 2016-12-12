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
            return '%s is an invalid room type' % room_type

    @staticmethod
    def add_person(person_id, firstname, lastname, position, wants_accomodation = 'N'):
        '''
        Add person details to the system
        '''
        full_name = firstname + " " + lastname
        if person_id in Amity.all_people.keys():
            return 'Person with %d id already exist.' % person_id

        elif position.upper() == 'fellow' and wants_accomodation == 'N':
            Amity.all_people[person_id] = full_name
            Amity.fellows.append(full_name)
            fellow = Fellow(person_id, firstname, lastname)
            random_office = generate_random_office()
            Amity.office_rooms[random_office].append(full_name)
            print("Added: " + full_name + " and allocated them to: " + random_office)
            Amity.unallocated_person.append(full_name)
            print(full_name + " does not need a living space, added to unallocated")

        elif position.upper() == 'Fellow' and wants_accomodation == 'Y':
            Amity.all_people[person_id] = full_name
            Amity.fellows.append(full_name)
            fellow = Fellow(person_id, firstname, lastname)
            random_office = generate_random_office()
            Amity.office_rooms[random_office].append(full_name)
            print("Added: " + full_name + " and allocated them to: " + random_office)
            random_ls = generate_random_living_space()
            Amity.ls_rooms[random_ls].append(full_name)
            print("Added: " + full_name + " and allocated them to: " + random_ls)

        elif position.upper() == 'staff' and wants_accomodation == 'N':
            Amity.all_people[person_id] = full_name
            Amity.staffs.append(full_name)
            staff = Staff(person_id, firstname, lastname)
            random_office = generate_random_office()
            Amity.office_rooms[random_office].append(full_name)
            print("Added: " + full_name + " and allocated them to: " + random_office)

        elif position.upper() == 'staff' and wants_accomodation == 'Y':
            Amity.all_people[person_id] = full_name
            Amity.staffs.append(full_name)
            staff = Staff(person_id, firstname, lastname)
            random_office = generate_random_office()
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
                people_details = readlines(people_file)
                people_details = people_details.split()
                if len(people_details) == 5:
                    Amity.add_person(person_id=people_details[0], firstname=people_details[1], lastname=people_details[2], position=people_details[3])



    @staticmethod
    def generate_random_office():
        '''
        Generates a random office that is not full
        '''
        random_room_name = random.choice(list(Amity.office_rooms))
        if len(random_room_name) >= 6:
            return 'Selected %s is full' % room_name
        else:
            return random_room_name

    @staticmethod
    def generate_random_living_space():
        '''
        Generate a random living space that is not fulloccupied
        '''
        random_room_name = random.choice(list(Amity.ls_rooms))
        if len(random_room_name) >= 4:
            return 'Selected %s is full' % room_name
        else:
            return random_room_name

    @staticmethod
    def reallocate_person(person_id, new_room_name):
        '''
        use the person id to remove the person from one office
        to another
        '''
        pass

    @staticmethod
    def is_full(room_name, room_type):
        '''
        check the room name and room type given if
        it is full before allocation
        '''
        pass

    @staticmethod
    def print_room(room_name):
        '''
        prints a room and all the people allocated to that room
        '''
        print(room_name)

    def print_allocation(self):
        '''
        prints a list of all the people that have been allocated a room
        '''
        pass

    def print_unallocated(self):
        '''
        prints a list of people that have not been allocated to a room yet
        '''
        pass


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
