class Amity(object):

    def load_people(self):
        '''
        Loads people to the system from a file.
        '''
        pass


    def reallocate_person(self, person_id, room_name):
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
