def main():
    user_name = input("Please enter your FULL name and CUSTOMER NUMBER IF AVAILABLE: ")
    print(f"Hello {user_name}!")

    while True:
        menu = """
Choose an option from the following:

1. List items from warehouse 1
2. List items from warehouse 2
3. Search and order item
4. Quit
"""

        user_choice = int(input(menu))

        if user_choice == 1:
            list_items(warehouse1)
        elif user_choice == 2:
            list_items(warehouse2)
        elif user_choice == 3:
            search_and_order()
        elif user_choice == 4:
            print("Goodbye! Thank you for visiting Jonathan's Warehouse Company.")
            break  # Exit this loop
        else:
            print("NOT ALLOWED!!! Please enter a valid choice from the MENU.")

        another_choice = input("Do you want to choose another option? TYPE yes or no: ")
        if another_choice.lower() != 'yes':
            print("Goodbye! Thank you for shopping with Jonathan's Warehouse Company.")
            break  # Exit the loop and end the program

def list_items(warehouse):
    for item in warehouse:
        print(item)

def search_and_order():
    search_item = input("Enter the item you want to search and order: ")
    if search_item in warehouse1:
        print(f"Item found in warehouse 1: {search_item}.  Great news....Placing order...")
        process_order(warehouse1, search_item)
    elif search_item in warehouse2:
        print(f"Item found in warehouse 2: {search_item}.  Great news...Placing order...")
        process_order(warehouse2, search_item)
    else:
        print(f"Item not found in either warehouse. Goods are not available. so sorry but please choose another item")

def process_order(warehouse, item):
    warehouse.remove(item)  # For simplicity, remove the item from list of things
    print("Thanks for your order! It will be processed and available as soon as possible in your home")

def initialize_warehouses():
    # Declare warehouse1 and warehouse2 as variables as a global 
    global warehouse1
    global warehouse2

    warehouse1 = [
        "Brand new laptop", "Exceptional monitor", "Cheap tablet"
    ]

    warehouse2 = [
        "High quality tablet", "Second hand headphones", "Second hand laptop"
    ]

if __name__ == "__main__":
    initialize_warehouses()
    main()
