import sqlite3
database = sqlite3.connect("inventory.db")
cursor = database.cursor()

def sql_database():
   #database = sqlite3.connect("inventory.db")
    #cursor = database.cursor()

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
    print("What would you like to add to your inventory?")
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


def update():
    print("What would you like to update in your inventory?")
    id = int(input("What is the ID of the item you would like to update: "))
    item_update = input("What would you like to update [quantity, name, supplier]: ")
    item = input("Enter the new update of the item: ")

    if item_update.lower().strip() == "quantity":
        item = int(item)
        cursor.execute("""
        UPDATE inventory SET quantity = ? WHERE id = ?
        """, (item, id))
    elif item_update.lower().strip() == "name":
        cursor.execute("""
        UPDATE inventory SET name = ? WHERE id = ?
        """, (item, id))
    else:
        cursor.execute("""
        UPDATE inventory SET supplier = ? WHERE id = ?
        """, (item, id))
    
    database.commit()
    
def remove():
    print("What would you like to remove in your inventory?")
    id = int(input("What is the ID of the item you would like to remove: "))

    cursor.execute("""
    DELETE FROM inventory WHERE id = ?
    """, (id,))

    database.commit()


def main():
    choices = ['add', 'update', 'remove', 'search', 'low stock']
    sql_database()

    print("\n--- WELCOME TO INVENTORY MANAGEMENT SYSTEM ---\n")

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


if __name__ == "__main__":
    main()

