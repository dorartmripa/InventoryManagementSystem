# Inventory Management System

A Python-based inventory management application designed to simplify stock tracking, product management, and restocking operations for small businesses or warehouses.

## Features

### Product Management

- Add new products with details (name, quantity, supplier, last restock date)
- Update product information or stock levels
- Remove products from the inventory
- Search and retrieve product records
- Track low-stock items for timely restocking

### Stock Tracking

- Monitor inventory levels in real-time
- Set alerts for products below a specified threshold
- Maintain historical data of restock dates
- Track suppliers for each product

## Database Structure

The system uses SQLite with the following core table:

**inventory** - Stores product details, quantities, suppliers, and restock dates

```sql
CREATE TABLE IF NOT EXISTS inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    quantity INTEGER,
    supplier TEXT,
    last_restock TEXT
)
```

Foreign key constraints are not needed as this is a single-table system, keeping it simple and lightweight.

## User Roles & Access Control

**Admin/Staff:** Full access to add, update, remove, and check stock levels

## Getting Started

### Requirements

- Python 3.7+
- SQLite3 (included with Python)

### Installation

```bash
git clone https://github.com/yourusername/inventory-management-system.git
cd inventory-management-system
```

### Running the Application

```bash
python "Inventory Management System.py"
```

The application will:

- Initialize the SQLite database (inventory.db) on first run
- Create the inventory table if it doesn't exist
- Display a menu-driven interface for inventory operations

## Usage

The application provides an interactive menu for:

- **Add Products** - Enter new products with details
- **Update Products** - Modify stock levels, supplier info, or product details
- **Remove Products** - Delete products from inventory
- **Check Low Stocks** - Identify products that need restocking

## Key Features

- ✅ Data Validation - Ensures correct input for quantities and dates
- ✅ Low Stock Alerts - Quickly identify products that need restocking
- ✅ Historical Tracking - Maintains last restock date for reference
- ✅ Interactive Menu - Easy-to-use command-line interface

## Technical Stack

- **Language:** Python 3
- **Database:** SQLite3
- **Architecture:** Console-based application with modular functions
- **Interface:** Interactive command-line menu system

## Future Enhancements

Potential future features:

- Web or GUI interface for easier management
- Automatic low-stock notifications
- Multi-user access with permissions
- Reports on stock trends and supplier performance
- Integration with barcode scanners

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Feel free to submit a Pull Request with improvements, bug fixes, or new features.

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

**Developed by Dorart**

## Extending this project

Ideas you may want implemented:

- Persist inventory to `inventory.json` or `inventory.db` (SQLite)
- Add unit tests using `pytest`
- Add a non-interactive CLI mode with `argparse` or `click`
- Package as an installable module with `setup.cfg`/`pyproject.toml` and a `console_scripts` entry point

If you want any of these, I can implement them and include tests and CI.

## Development

- Run tests: `pytest` (add tests first)
- Format code: use `black` or `ruff` as desired

## Contributing

- Open an issue to propose features or report bugs
- Send pull requests with clear descriptions and tests for new behavior

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## Contact

If you want help implementing persistence, tests, packaging, or CI, reply with which item to do next (for example: `A` — add `LICENSE`, `B` — add example `inventory.json`, `C` — persist to SQLite, `D` — add CLI mode). I will implement the chosen item and update the repository.

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

Developed by Dorart
