from multiprocessing.sharedctypes import Value
import re
from classes.inventory import Inventory
from classes.customer import Customer
import csv

# try to do something to not repeat this code
with open ('./data/customers.csv', newline='') as csvfile:
    people = csv.DictReader(csvfile, delimiter=',', skipinitialspace=True)
    for row in people:
        Customer.all_customers.append(Customer(**dict(row)))

with open ('./data/inventory.csv', newline='') as csvfile:
    movies = csv.DictReader(csvfile, delimiter=',', skipinitialspace=True)
    for row in movies:
        Inventory.inventory.append(Inventory(**dict(row)))

def main_menu():
    print('== Welcome to Code Platoon Video! ==\n'
    '1. View store video inventory\n'
    '2. View store customers\n'
    '3. View customer rented videos\n'
    '4. Add new customer\n'
    '5. Rent video\n'
    '6. Return video\n'
    '7. Exit')
    user_choice = input('> ')

    match user_choice:
        case '1':
            Inventory.display_inventory()
            input("Press enter to return to menu...")
            print()
        case '2':
            Customer.display_customers()
            input("Press enter to return to menu...")
            print()
        case '3':
            id = input("Enter customer id: ")
            Customer.view_customers_rented_videos(Customer.find_customer_by_id(id))
            input("Press enter to return to menu...")
            print()
        case '4':
            new_customer = {'id' : str(int(Customer.all_customers[-1].customer_id) + 1), 'current_video_rentals' : ''}
            new_customer['first_name'] = input("Enter new users first name: ")
            new_customer['last_name'] = input("Enter new users last name: ")
            new_customer['account_type'] = input("Enter new users account type: ").lower()
            # quick catch for invalid account type entry
            while re.search("\As|\Ap" and "f$|x$", new_customer['account_type']) == None or len(new_customer['account_type']) != 2:
                print("Invalid account type\n")
                new_customer['account_type'] = input("Enter new users account type: ").lower()
            # pass the new customer into our class method 
            Customer.add_new_customer(new_customer)
            print(f"{new_customer['first_name']} has been added.")
            input("Press enter to return to menu...")
            print()
        case '5':
            id = input("Enter customer id: ")
            video = input("Enter video title: ")
            Inventory.rent_a_video(Customer.find_customer_by_id(id), Inventory.find_video_by_title(video))
            input("Press enter to return to menu...")
            print()
        case '6':
            id = input("Enter customer id: ")
            video = input("Enter video title: ")
            Inventory.return_a_video(Customer.find_customer_by_id(id), Inventory.find_video_by_title(video))
            input("Press enter to return to menu...")
            print()
        case '7':
            print("Goodbye!")
        case other:
            print("Invalid menu selection\n")

    return user_choice

while main_menu() != '7':
    continue