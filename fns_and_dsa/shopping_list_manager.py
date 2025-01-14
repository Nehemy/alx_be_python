def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_item = input("Enter the item to add: ")
            shopping_list.append(add_item)
            
        elif choice == '2':
            remove_item = input("Enter the name of the item to remove: ")
            if remove_item not in shopping_list:
                print("Item not in shopping list")
            else:
                shopping_list.remove(remove_item)
            
        elif choice == '3':
            for i in shopping_list:
                print(i)
            
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
