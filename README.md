
# SPORTS EQUIPMENT MANAGER


This is a simple command-line program written in Python to manage a sports equipment inventory. It allows users to track which equipment is available and which items are currently borrowed.

# How to Run the Program

1.  **Save the Code:** Ensure all the Python code provided (the lists, functions, and the main execution block) is saved in a single file named `equipment_manager.py` (or any `.py` file name).
2.  **Run from Terminal:** Open your terminal or command prompt, navigate to the directory where you saved the file, and execute the program using the Python interpreter:

    ```bash
    python equipment_manager.py
    ```

#Features

The program provides a simple menu-driven interface with the following options:

* **1. Add New Equipment:** Allows the user to add a new item to the main **Equipment** inventory list. The name will be capitalized (Title Case) automatically.
* **2. View Available Equipment:** Displays a numbered list of all items currently in stock (**Equipment** list).
* **3. Borrow Equipment:** Prompts the user to select an item number from the available **Equipment** list. The selected item is removed from **Equipment** and added to the **borrowed\_items** list.
* **4. Return Equipment:** Prompts the user to select an item number from the **borrowed\_items** list. The selected item is removed from **borrowed\_items** and returned to the main **Equipment** list.
* **5. View Borrowed Items:** Displays a numbered list of all items currently checked out (**borrowed\_items** list).
* **6. Exit:** Closes the program.

#Technical Details

* **Data Structures:** The inventory uses two global Python lists:
    * `Equipment`: Stores items currently available for borrowing.
    * `borrowed_items`: Stores items currently checked out.
* **Item Management:** The `list()` function handles displaying the numbered list. Borrowing and returning are managed using the `.pop()` method to remove an item by index (after user selection) and the `.append()` method to add it to the other list, ensuring items are tracked correctly.
* **Input Handling:** Includes basic error handling for invalid (non-numeric) input when selecting item numbers.

---
**Initial Inventory:**
* Cricket Bat
* Volleyball
* Tennis Ball
* Rugby ball
* Badminton Racket
* Wickets
* Basketball
* Skipping Rope



