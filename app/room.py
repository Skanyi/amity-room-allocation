from collections import defaultdict

class Room(object):

    '''
    Models all the information of the rooms that the office and Living space will
    inherit from
    '''
    office_rooms = []
    ls_rooms = []
    rooms  = []
    full_rooms  = defaultdict(list) # name of the room as the key and names of the occupants as the kvalues
    not_full_rooms = defaultdict(list)

    def __init__(self, room_name='', room_type='', max_occupants=0):
        self.room_name = room_name
        self.room_type = room_type
        self.max_occupants = max_occupants


    @staticmethod
    def create_room(room_name, room_type):
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

    def __init__(self, room_name):
        super(Office, self).__init__(room_name) #max_occupants = 6)


class LivingSpace(Room):

    def __init__(self, room_name):
        super(LivingSpace, self).__init__(room_name) #max_occupants=4)
