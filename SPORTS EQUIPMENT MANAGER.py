Equipment = [
    "Cricket Bat", "Volleyball", "Tennis Ball","Rugby ball",
    "Badminton Racket", "Wickets", "Basketball", "Skipping Rope"
]

borrowed_items = []

def list(item_list, header):
    if not item_list:
        print("Empty")
        return False
    count=1
    for item in item_list:
        print(f"{count}.{item}")
        count += 1
    return True
def add_equipment():
    print("\n Add New Equipment")
    name = input("Enter equipment name:")

    if not name:
        print("Equipment name cannot be empty.\n")
        return
    Equipment.append(name.title())
    print(f" added successfully to the inventory!\n")
def check_stock():
    list(Equipment, "Available Sports Equipment")
def borrow_item():
    if not list(Equipment, "Select Item to Borrow"):
        print("No equipment is available to borrow.\n")
        return
    try:
        selection = int(input("Select item number to borrow: "))
    except:
        print("Invalid input. Please enter a number.\n")
        return

    equipment_index = selection - 1
    if 0 <= equipment_index < len(Equipment):
        item_to_borrow = Equipment.pop(equipment_index)
        
        borrowed_items.append(item_to_borrow)
        print("Item successfully borrowed.\n")
    else:
        print("That item number does not match any available equipment.\n")

def return_item():
    if not list(borrowed_items, "Select Borrowed Item to Return"):
        print("No items are currently borrowed.\n")
        return
    try:
        selection = int(input("Select item number to return: "))
    except:
        print("Invalid input. Please enter a number.\n")
        return

    borrowed_index = selection - 1

    if 0 <= borrowed_index < len(borrowed_items):
        item_to_return = borrowed_items.pop(borrowed_index)

        Equipment.append(item_to_return)
        print(f"Returned successfully to the inventory.\n")
    else:
        print("Invalid item number.\n")
def main():
    while True:
        print(" SPORTS EQUIPMENT MANAGER")
        print("1. Add New Equipment")
        print("2. View Available Equipment")
        print("3. Borrow Equipment")
        print("4. Return Equipment")
        print("5. View Borrowed Items")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_equipment()
        elif choice == "2":
            check_stock()
        elif choice == "3":
            borrow_item()
        elif choice == "4":
            return_item()
        elif choice == "5":
            list(borrowed_items, "Items Currently Borrowed")
        elif choice == "6":
            print("\nThank you!.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()