from collections import defaultdict

class Amity(object):

    full_rooms  = defaultdict(list) # name of the room as the key and names of the occupants as the kvalues
    not_full_rooms = defaultdict(list)
    rooms = []
    staffs = []
    male_fellows = []
    female_fellows = []
    room_name = ''
    room_type = ''

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

    def add_person(self):
        '''
        Add person details to the system
        '''

        pass

    def validate_position(self):
        '''
        Validate that the person being added on the system is either
        a fellow or Staff
        '''
        pass

    def validate_gender(self):
        '''
        For living space alloction for the fellows, we use gender to group them
        '''
        pass


    def load_people(self):
        '''
        Loads people to the system from a file.
        '''
        pass



    def allocate_office(self):
        '''
        Allocates office to the people once they are added to the list
        at random. Allocates offices that are not full yet.
        '''
        pass

    def allocate_living_space(self):
        '''
        Allocates the fellows a living space if they want one.
        Have a default value of No.
        Allocates guys to the male wing and ladies to the female wing
        '''
        pass

    def reallocate_person(self, person_id):
        '''
        reallocates a person with specific id to another room that is not full
        '''
        self.person_id = person_id
        pass

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

    def print_room(self):
        '''
        prints a room and all the people allocated to that room
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
