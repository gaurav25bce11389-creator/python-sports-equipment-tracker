Sports Equipment Manager

Welcome to the Sports Equipment Manager!
This is a simple Python program that lets you keep track of sports equipment—what’s available, what’s borrowed, and what’s been returned. It runs in the terminal and is perfect for small clubs, schools, or anyone who wants a basic inventory tool.

# What This Program Does
This tool helps you:
* Add new sports equipment to your inventory
* See what equipment is currently available
* Borrow an item and mark it as taken
* Return borrowed items
* View everything that’s currently checked out

Everything happens through an easy menu system where you just type the number of your choice.

# How the Program Works
The program starts with a small list of equipment like cricket bats, volleyballs, and skipping ropes. You can add more at any time.
Two lists keep track of everything:
* Equipment → items available to borrow
* Borrowed_items → items currently borrowed

Whenever you borrow something, it moves from one list to the other. Simple and clean.

# How to Run It

1. Make sure you have **Python 3** installed.
2. Save the code as something like `equipment_manager.py`.
3. Open a terminal or command prompt.
4. Run:

```bash
python equipment_manager.py
```

You’ll then see a menu like this:

```
SPORTS EQUIPMENT MANAGER
1. Add New Equipment
2. View Available Equipment
3. Borrow Equipment
4. Return Equipment
5. View Borrowed Items
6. Exit
```

Just type the number of the option you want to use.

---

## A Quick Example

**Borrowing an item:**

```
Select Item to Borrow:
1. Cricket Bat
2. Volleyball
3. Tennis Ball
...
Select item number to borrow: 2
Item successfully borrowed.
```

Now the Volleyball is moved to the borrowed list.

**Returning an item:**

```
Select Borrowed Item to Return:
1. Volleyball
Select item number to return: 1
Returned successfully to the inventory.
```

## **License**

This project is free to use, modify, learn from, or improve however you like. Have fun with it! 
