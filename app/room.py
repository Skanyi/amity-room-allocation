from collections import defaultdict

class Room(object):

    '''
    Models all the information of the rooms that the office and Living space will
    inherit from
    '''
    office_rooms = defaultdict(list)
    ls_rooms = defaultdict(list)
    rooms  = []

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


class Office(Room):

    def __init__(self, room_name):
        super(Office, self).__init__(room_name) #max_occupants = 6)


class LivingSpace(Room):

    def __init__(self, room_name):
        super(LivingSpace, self).__init__(room_name) #max_occupants=4)
