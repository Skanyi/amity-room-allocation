from .person import *
from .room import *

class Amity(object):
    office_rooms = defaultdict(list)
    ls_rooms = defaultdict(list)
    all_rooms  = []
    staffs = []
    fellows = []
    all_people = {}

    @staticmethod
    def create_room(room_name, room_type):
        '''
        Creates a room in Amity
        '''
        

    @staticmethod
    def add_person(person_id, firstname, lastname, position):
        '''
        Add person details to the system
        '''
        pass

    @staticmethod
    def load_people(filename):
        '''
        Loads people to the system from a text file.
        '''
        pass

    @staticmethod
    def allocate_office(room_name):
        '''
        Allocates office to the people once they are added to the list
        at random. Allocates offices that are not full yet.
        '''
        pass

    @staticmethod
    def allocate_living_space(room_name, want_accomodation = 'N'):
        '''
        Allocates the fellows a living space if they want one.
        Have a default value of No.
        '''
        pass

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
