from classes.customer import Customer
from re import search

class Inventory():

    inventory = []

    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.title = kwargs['title']
        self.rating = kwargs['rating']
        self.release_year = kwargs['release_year']
        self.copies_available = kwargs['copies_available']
    
    @classmethod
    def display_inventory(self):
        print('{i:^20}|{j:^20}'.format(i = "TITLE",j = 'COPIES AVAILABLE'))
        for items in self.inventory:
            print(f'{items.title:<20}|{items.copies_available:^20}')
    
    @classmethod
    def find_video_by_title(self, video_title):
        for item_object in self.inventory:
            if item_object.title == video_title:
                return item_object
        return None
        
    @classmethod
    def rent_a_video(self, customer_object, video_object):
        number_of_rented_videos = 0
        if customer_object.current_video_rentals != '':
            number_of_rented_videos = len(customer_object.current_video_rentals.split('/'))
        # perform some qucik checks to see if data is valid before continuing
        if customer_object == None:
            print('Invalid customer id')
            return
        if video_object == None:
            print('Invalid video title')
            return
        if video_object.copies_available == '0':
            print("There are no copies available to rent for this title")
            return
        # now perform some checks to see if they can rent a video base on account type
        if search("\As", customer_object.account_type) and number_of_rented_videos == 1:
            print("This customer has reached their maximum account limit for rented videos\n")
            return
        elif search("\Ap", customer_object.account_type) and number_of_rented_videos == 3:
            print("This customer has reached their maximum account limit for rented videos\n")
            return
        elif search("f$", customer_object.account_type) and video_object.rating == 'R':
            print("This account is restricted from renting 'R' rated movies\n")
            return
        # done with checks, execute the renting feature
        video_object.copies_available = str(int(video_object.copies_available) - 1)
        if number_of_rented_videos > 0:
            customer_object.current_video_rentals += f'/{video_object.title}'
        else:
            customer_object.current_video_rentals += video_object.title
        print(f"The video has been checked out of inventory and added to user account.")
    
    @classmethod
    def return_a_video(self, customer_object, video_object):
        number_of_rented_videos = 0
        # repeat quick check for valid data
        if customer_object == None:
            print('Invalid customer id')
            return
        if video_object == None:
            print('Invalid video title')
            return
        if customer_object.current_video_rentals != '':
            number_of_rented_videos = len(customer_object.current_video_rentals.split('/'))
        if number_of_rented_videos == 0:
            print("This customer has no videos checked out.")
            return
        if video_object.title not in customer_object.current_video_rentals.split('/'):
            print("This customer does not have that video checked out")
            return
        # no other checks needed, execute return
        video_object.copies_available = str(int(video_object.copies_available) + 1)
        if number_of_rented_videos > 0:
            customer_object.current_video_rentals = customer_object.current_video_rentals.split('/')
            customer_object.current_video_rentals.remove(video_object.title)
            customer_object.current_video_rentals = '/'.join(customer_object.current_video_rentals)
            print(f"The video has been removed from account and placed back in inventory.")
            return
        print(f"The video has been removed from account and placed back in inventory.")
        customer_object.current_video_rentals = ''
