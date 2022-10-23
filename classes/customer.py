
class Customer():
    all_customers = [] # class variable to store all customers

    def __init__(self, **kwargs):
        self.customer_id = kwargs['id']
        self.account_type = kwargs['account_type']
        self.first_name = kwargs['first_name']
        self.last_name = kwargs['last_name']
        self.current_video_rentals = kwargs['current_video_rentals']

    @classmethod
    def display_customers(self):
        print('{i:^20}|{j:^20}'.format(i = "NAME",j = 'ID'))
        for people in self.all_customers:
            name = people.first_name + ' ' + people.last_name
            print(f'{name:<20}|{people.customer_id:^20}')

    @classmethod
    def find_customer_by_id(self, id):
        for customer_obj in self.all_customers:
            if id == customer_obj.customer_id:
                return customer_obj
        return None # this will catch invalid customer id entries in our methods and return a no match

    @classmethod
    def view_customers_rented_videos(self, customer_object):
        if customer_object == None:
            print('Invalid customer id')
            return
        movie_list = customer_object.current_video_rentals.split('/')
        print(f'\n{customer_object.first_name} {customer_object.last_name}\n' + '-' * 20)
        for movie in movie_list:
            print(movie)

    @classmethod
    def add_new_customer(self, new_customer):
         Customer.all_customers.append(Customer(**dict(new_customer.items())))