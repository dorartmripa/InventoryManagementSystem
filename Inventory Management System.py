import sqlite3

database = sqlite3.connect("inventory.db") #Connects to the database
cursor = database.cursor() #Creates a cursor to execute SQL commands

def sql_database(): #Creates database table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        quantity INTEGER,
        supplier TEXT,
        last_restock TEXT
    )
    """) #Creates table if it doesn't exist

    database.commit() #Save changes

def add(): #Adds new item to the database
    print("\nWhat would you like to add to your inventory?")
    print("Enter the following: ")
    name = input("Name of the product: ")

    while True: #loops until a number is entered
        try:
            quantity = int(input("Quantity of the product: "))
            break #breaks out of loop if a number was entered
        except ValueError: #Catches error if user didn't eneter a number
            print("\nOops! Please enter a number. Try again.")

    supplier = input("Name of the supplier: ")
    last_restock = input("Date of the last restock DD/MM/YYYY: ")
    
    cursor.execute("""
    INSERT INTO inventory (name, quantity, supplier, last_restock)
    VALUES (?, ?, ?, ?)
    """, (name, quantity, supplier, last_restock)) #Adds the new item to the database
    
    database.commit() #Save changes
    print("\nItem added successfully!\n")

def update(): #Updates item by id 
    while True: #loops until a item is updated
        try:
            print("\nWhat would you like to update in your inventory?")
            id = int(input("What is the ID of the item you would like to update: "))
        except ValueError: #Catches error if user didn't eneter a number
                print("\nOops! Please enter a number. Try again.")
                continue #Restart the loop to ask for input again

        cursor.execute("""
        SELECT 1 from inventory WHERE id = ? LIMIT 1
        """, (id,)) #Finds the first item with the id number entered by user
        exists = cursor.fetchone() #Gets the matching result

        if not exists: #Checks if no matching items were found
            print("\nOops! That item does not exist. Try again.\n")
            continue #Restart the loop to ask for input again

        while True: #loops until a valid option is enetered
            item_update = input("What would you like to update [quantity, name, supplier, last restock]: ")

            if item_update.lower().strip() == "quantity": #Checks if user entered quantity
                item = input("Enter the new *quantity* for this item: ")
                item = int(item)
                cursor.execute("""
                UPDATE inventory SET quantity = ? WHERE id = ?
                """, (item, id)) #Updates the quantity of the item
            elif item_update.lower().strip() == "name": #Checks if user entered name
                item = input("Enter the new *name* for this item: ")
                cursor.execute("""
                UPDATE inventory SET name = ? WHERE id = ?
                """, (item, id)) #Updates the name of the item
            elif item_update.lower().strip() == "supplier": #Checks if user entered supplier
                item = input("Enter the new *supplier name* for this item: ")
                cursor.execute("""
                UPDATE inventory SET supplier = ? WHERE id = ?
                """, (item, id)) #Updates the supplier of the item
            elif item_update.lower().strip() == "last restock": #Checks if user entered last restock
                item = input("Enter the new *last restock date* (DD/MM/YYYY): ")
                cursor.execute("""
                UPDATE inventory SET last_restock = ? WHERE id = ?
                """, (item, id)) #Updates the last restock date of the item
            else:
                print("\nOops! That's not a valid option. Try again.\n")
                continue #Restart the loop to ask for input again
            
            break #breaks out of loop if a valid option was entered

        database.commit() #Save changes
        print("\nItem updated successfully!\n")
        break #Exit the loop after updating the item

def remove(): #Removes item by id 
    while True: #loops until a valid item is entered
        try:
            print("\nWhat would you like to remove in your inventory?")
            id = int(input("What is the ID of the item you would like to remove: "))
        except ValueError: #Catches error if user didn't eneter a number
            print("\nOops! Please enter a number. Try again.")
            continue #Restart the loop to ask for input again

        cursor.execute("""
        SELECT 1 from inventory WHERE id = ? LIMIT 1
        """, (id,)) #Finds the first item with the id number entered by user
        exists = cursor.fetchone() #Gets the matching result

        if not exists: #Checks if no matching items were found
            print("\nOops! That item does not exist. Try again.\n")
            continue #Restart the loop to ask for input again

        cursor.execute("""
        DELETE FROM inventory WHERE id = ?
        """, (id,)) #Deletes the item with the id number entered
        database.commit() #Saves changes
        print("\nItem removed successfully!\n")

        break #Exit the loop after deleting the item

def search(): #Search for items by name and display the results
    while True: #loops until a valid item is entered
        print("\nWhat would you like to search for in your inventory?")
        name = input("Enter the name of the item(s) you want to search for: ").strip()

        cursor.execute("""
        SELECT * FROM inventory 
        WHERE name LIKE ?
        """, (f"%{name}%",)) #Search for items that contains name in the database

        results = cursor.fetchall() #Gets all the matching results

        if not results: #Checks if no matching items were found
            print("\nOops! That item does not exist. Try again.\n")
            continue #Restart the loop to ask for input again

        print(f"\nItems in your inventory that match '{name}':")

        cursor.execute("SELECT * FROM inventory") #Gets all the items in the inventory database
        columns = [description[0] for description in cursor.description] #Gets the column names of the database
        print(f"\n{columns}")

        for result in results: #Goes through each row in results and prints it out
            print(result)
        
        break #Exit the loop after showing the results

def low_stock(): #Prints items in the database with quantity lower than the number the user entered
    while True: #loops until a number is entered
        try:
            low_stock = int(input("\nCheck for items with quantity lower than: "))
            break #breaks out of loop if a number was entered
        except ValueError: #Catches error if user didn't eneter a number
            print("\nOops! Please enter a number. Try again.")

    cursor.execute("""
    SELECT * FROM inventory WHERE quantity < ?
    """, (low_stock,)) #Search for items that has less than the quantity number entered

    results = cursor.fetchall() #Gets all the matching results

    print(f"\nItems in your inventory that are less than {low_stock}")

    cursor.execute("SELECT * FROM inventory") #Gets all the items in the inventory database
    columns = [description[0] for description in cursor.description] #Gets the column names of the database
    print(f"\n{columns}")

    for result in results:
            print(result)

def main():
    choices = ['add', 'update', 'remove', 'search', 'low stock']
    sql_database() #creates the sqlite database if not created already

    print("\n--- WELCOME TO INVENTORY MANAGEMENT SYSTEM ---\n")

    while True: #loops until user doesn't want to make any more changes to the database
        print("To make a change to your inventory, type one of the following options:")
        print("- Add")
        print("- Update")
        print("- Remove")
        print("- Search")
        print("- Low Stock\n")

        action = input("Enter your choice: ").strip().lower()

        if action not in choices: #checks if user entered a valid option
            while True:
                print("\nOops! That's not a valid option. Try again.\n")
                print("Enter one of the following options: ")
                print("- Add")
                print("- Update")
                print("- Remove")
                print("- Search")
                print("- Low Stock\n")

                action = input("Enter your choice: ").strip().lower()

                if action in choices: #breaks out of the loop if a valid option was entered
                    break
        
        if action == choices[0]: #Calls add() if user entered add
            add()
        elif action == choices[1]: #Calls update() if user entered update
            update()
        elif action == choices[2]: #Calls remove() if user entered remove
            remove()
        elif action == choices[3]: #Calls search() if user entered search
            search()
        else: #Calls low_stock() by default since code makes sure it user enters a valid option
            low_stock()

        while True: #Loops until user entered yer or no
            yes_or_no = input("Do you want to perform another inventory action? (yes/no): ").strip().lower()

            if yes_or_no in ["yes", "no"]:
                break #Exits loop if user entered a valid option

        if yes_or_no == "no": #Ends code if user entered no
            print("\nThank you for using Inventory Management System!\n")
            database.close() #Closes connection to the database
            break #Exits the loop to end the program

if __name__ == "__main__": #Run only when the file is executed directly.
    main()

