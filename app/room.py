from collections import defaultdict

class Room(object):

    '''
    Models all the information of the rooms that the office and Living space will
    inherit from
    '''
    office_rooms = defaultdict(list)
    ls_rooms = defaultdict(list)
    rooms  = ['Go']

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
        print('Steve, Kevin')


class Office(Room):

    def __init__(self, *args, **kwargs):
        super(Office, self).__init__(*args, **kwargs)


class LivingSpace(Room):

    def __init__(self, *args, **kwargs):
        super(LivingSpace, self).__init__(*args, **kwargs)
