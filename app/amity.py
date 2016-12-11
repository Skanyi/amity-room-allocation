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
    unallocated_person = {}
    full_name = ""


    @staticmethod
    def create_room(room_name, room_type):
        '''
        Check that the room does not exist and determine what type of room it is
        '''
        if room_name in Amity.all_rooms:
            return 'Room already exists, Create another room with another name'
        elif room_type.upper() == 'O':
            Amity.all_rooms.append(room_name.upper())
            Amity.office_rooms[room_name.upper()]
            current_room = LivingSpace()
        elif room_type.upper() == 'L':
            Amity.all_rooms.append(room_name.upper())
            Amity.ls_rooms[room_name.upper()]
            current_room = Office()
        else:
            return '%s is an invalid room type' % room_type

    @staticmethod
    def add_person(person_id, firstname, lastname, position):
        '''
        Add person details to the system
        '''
        if person_id in Amity.all_people.keys():
            return 'Person with %d id already exist.' % person_id
        elif position.upper() == 'F':
            Amity.full_name = firstname + " " + lastname
            Amity.all_people[person_id] = Amity.full_name
            Amity.fellows.append(Amity.full_name)
            fellow = Fellow(person_id, firstname, lastname)

        elif position.upper() == 'S':
            Amity.full_name = firstname + " " + lastname
            Amity.all_people[person_id] = Amity.full_name
            Amity.staffs.append(Amity.full_name)
            staff = Staff(person_id, firstname, lastname)
            Amity.full_name = firstname + " " + lastname
        else:
            return '%s is not a valid position.' % position
    @staticmethod
    def load_people(filename):
        '''
        Loads people to the sstem from a text file.
        '''
        pass

    @staticmethod
    def allocate_office(room_name):
        '''
        Allocates office to the people once they are added to the list
        at random. Allocates offices that are not full yet.
        '''
        room_name = random.randint(0, len(Amity.office_rooms) - 1)
        if len(Amity.office_rooms[list(Amity.office_rooms)[room_name]]) >= 6:
            return 'Selected %s is full' % room_name
        else:
            Amity.office_rooms[list(Amity.office_rooms)[room_name]].append(Amity.full_name)
            print('person Added succesfully')

    @staticmethod
    def allocate_living_space(room_name, wants_accomodation = 'N'):
        '''
        Allocates the fellows a living space if they want one.
        Have a default value of No.
        '''
        room_name = random.randint(0, len(Amity.ls_rooms) - 1)
        if wants_accomodation == 'N':
            return 'Thanks but the fellow does not want accomodation'
        else:
            if len(Amity.ls_rooms[list(Amity.ls_rooms)[room_name]]) >= 4:
                return 'Selected %s is full' % room_name
            else:
                Amity.ls_rooms[list(Amity.ls_rooms)[room_name]].append(Amity.full_name)
                print('Person added succesfully')


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
