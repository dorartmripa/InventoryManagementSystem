import sqlite3

database = sqlite3.connect("inventory.db")
cursor = database.cursor()

def sql_database():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        quantity INTEGER,
        supplier TEXT,
        last_restock TEXT
    )
    """)

    database.commit()

def add():
    print("\nWhat would you like to add to your inventory?")
    print("Enter the following: ")
    name = input("Name of the product: ")
    quantity = int(input("Quantity of the product: "))
    supplier = input("Name of the supplier: ")
    last_restock = input("Date of the last restock DD/MM/YYYY: ")
    
    cursor.execute("""
    INSERT INTO inventory (name, quantity, supplier, last_restock)
    VALUES (?, ?, ?, ?)
    """, (name, quantity, supplier, last_restock))
    
    database.commit()
    print("\nItem added successfully!\n")

def update():
    while True:
        while True:
            try:
                print("\nWhat would you like to update in your inventory?")
                id = int(input("What is the ID of the item you would like to update: "))
                break
            except ValueError:
                print("\nOops! Please enter a number. Try again.")

        cursor.execute("""
        SELECT 1 from inventory WHERE id = ? LIMIT 1
        """, (id,))
        exists = cursor.fetchone()

        if not exists:
            print("\nOops! That item does not exist. Try again.\n")
            continue

        while True:
            item_update = input("What would you like to update [quantity, name, supplier, last restock]: ")

            if item_update.lower().strip() == "quantity":
                item = input("Enter the new *quantity* for this item: ")
                item = int(item)
                cursor.execute("""
                UPDATE inventory SET quantity = ? WHERE id = ?
                """, (item, id))
            elif item_update.lower().strip() == "name":
                item = input("Enter the new *name* for this item: ")
                cursor.execute("""
                UPDATE inventory SET name = ? WHERE id = ?
                """, (item, id))
            elif item_update.lower().strip() == "supplier":
                item = input("Enter the new *supplier name* for this item: ")
                cursor.execute("""
                UPDATE inventory SET supplier = ? WHERE id = ?
                """, (item, id))
            elif item_update.lower().strip() == "last restock":
                item = input("Enter the new *last restock date* (DD/MM/YYYY): ")
                cursor.execute("""
                UPDATE inventory SET last_restock = ? WHERE id = ?
                """, (item, id))
            else:
                print("\nOops! That's not a valid option. Try again.\n")
                continue
            
            break

        database.commit()
        print("\nItem updated successfully!\n")
        break

def remove():
    while True:
        while True:
            try:
                print("\nWhat would you like to remove in your inventory?")
                id = int(input("What is the ID of the item you would like to remove: "))
                break
            except ValueError:
                print("\nOops! Please enter a number. Try again.")

        cursor.execute("""
        SELECT 1 from inventory WHERE id = ? LIMIT 1
        """, (id,))
        exists = cursor.fetchone()

        if not exists:
            print("\nOops! That item does not exist. Try again.\n")
            continue

        cursor.execute("""
        DELETE FROM inventory WHERE id = ?
        """, (id,))
        database.commit()
        print("\nItem removed successfully!\n")

        break

def search():
    while True:
        print("\nWhat would you like to search for in your inventory?")
        name = input("Enter the name of the item(s) you want to search for: ").strip()

        cursor.execute("""
        SELECT * FROM inventory 
        WHERE name LIKE ?
        """, (f"%{name}%",))

        results = cursor.fetchall()

        if not results:
            print("\nOops! That item does not exist. Try again.\n")
            continue

        print(f"\nItems in your inventory that match '{name}':")

        cursor.execute("SELECT * FROM inventory")
        columns = [description[0] for description in cursor.description]
        print(f"\n{columns}")

        for result in results:
            print(result)
        
        break

def low_stock():
    while True:
        try:
            low_stock = int(input("\nCheck for items with quantity lower than: "))
            break
        except ValueError:
            print("\nOops! Please enter a number. Try again.")

    cursor.execute("""
    SELECT * FROM inventory WHERE quantity < ?
    """, (low_stock,))

    print(f"\nItems in your inventory that are less than {low_stock}")
    results = cursor.fetchall()
    for result in results:
            print(result)



def main():
    choices = ['add', 'update', 'remove', 'search', 'low stock']
    sql_database()

    print("\n--- WELCOME TO INVENTORY MANAGEMENT SYSTEM ---\n")

    while True:
        print("To make a change to your inventory, type one of the following options:")
        print("- Add")
        print("- Update")
        print("- Remove")
        print("- Search")
        print("- Low Stock\n")

        action = input("Enter your choice: ").strip().lower()

        if action not in choices:
            while True:
                print("\nOops! That's not a valid option. Try again.\n")
                print("Enter one of the following options: ")
                print("- Add")
                print("- Update")
                print("- Remove")
                print("- Search")
                print("- Low Stock\n")

                action = input("Enter your choice: ").strip().lower()

                if action in choices:
                    break
    
        if action == choices[0]:
            add()
        elif action == choices[1]:
            update()
        elif action == choices[2]:
            remove()
        elif action == choices[3]:
            search()
        else:
            low_stock()
        
        yes_or_no = input("Do you want to perform another inventory action? (yes/no): ").strip().lower()

        if yes_or_no == "no":
            print("\nThank you for using Inventory Management System!\n")
            database.close()
            break


if __name__ == "__main__":
    main()

