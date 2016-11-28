import abc
from amity import Amity

class Room(Amity):
    full_room  = {} # name of the room as the key and names of the occupants as the kvalues
    not_full_room = {}
    '''
    Models all the information of the rooms that the office and Living space will
    inherit from
    '''
    def __init__(self, room_name, room_type):
        self.room_name = room_name
        self.room_type = room_type

    @abc.abstractmethod
    def set_room_max_occupants(self):
        pass

    def create_room(self):
        '''
        Creates a room in Amity
        '''
        pass

    def validate_room_type(self):
        '''
        Validates that the room is either #Office or #LivingSpace
        '''
        pass

    def validate_wing(self, wing):
        '''
        if it is a living space, then validates that it is either
        male_wing or female_wing
        '''
        self.wing = wing
        pass

class Office(Room):

    def room_max_occupants(self):
        '''
        set maximum occupants of one office to 6 people
        '''
        self.max_occupants = 6
        return self.max_occupants

class LivingSpace(Room):

    def room_max_occupants(self):
        '''
        set maximum occupants of one living space to 4 people
        '''
        self.max_occupants = 4
        return self.max_occupants
