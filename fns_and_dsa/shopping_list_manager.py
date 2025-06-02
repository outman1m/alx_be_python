def display_menu():
    """Display the main menu of the shopping list manager"""
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """Main function to manage the shopping list"""
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to your shopping list.")
            else:
                print("Item name cannot be empty!")
        
        elif choice == '2':
            if not shopping_list:
                print("Your shopping list is empty!")
                continue
                
            print("Current items in your list:")
            for index, item in enumerate(shopping_list, 1):
                print(f"{index}. {item}")
                
            try:
                item_num = int(input("Enter the number of item to remove: "))
                if 1 <= item_num <= len(shopping_list):
                    removed_item = shopping_list.pop(item_num - 1)
                    print(f"'{removed_item}' has been removed from your list.")
                else:
                    print("Invalid item number!")
            except ValueError:
                print("Please enter a valid number!")
        
        elif choice == '3':
            if not shopping_list:
                print("Your shopping list is empty!")
            else:
                print("\nYour Shopping List:")
                for index, item in enumerate(shopping_list, 1):
                    print(f"{index}. {item}")
        
        elif choice == '4':
            print("Goodbye! Your final shopping list:")
            if shopping_list:
                for index, item in enumerate(shopping_list, 1):
                    print(f"{index}. {item}")
            else:
                print("(Empty)")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
