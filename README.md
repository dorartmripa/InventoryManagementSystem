
# Inventory Management System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A small, console-based Python inventory script designed for learning, demonstrations, and lightweight use-cases.

This repository contains [Inventory Management System.py](Inventory Management System.py), a single-file script that provides basic inventory operations such as adding items, updating quantities, and removing items. The script is intentionally simple so it can be adapted to use CSV/JSON/SQLite storage or repackaged as a CLI.

**Project goals**

- Provide a minimal, easy-to-read example of inventory logic in Python
- Be a starting point for adding persistence, tests, and automation
- Demonstrate common inventory operations and simple data models

## Features

- Add new inventory items (SKU/ID, name, quantity, optional price/notes)
- Update item quantities (increase/decrease)
- Remove items from inventory
- Simple console menu for interactive usage

## Requirements

- Python 3.8 or newer

## Quickstart

1. Clone the repository and change into the folder:

```powershell
git clone <your-repo-url>
cd InventoryManagementSystem
```

2. (Optional) create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. Run the script:

```powershell
python "Inventory Management System.py"
```

The script will run in the console and present a menu. Follow on-screen prompts to add, edit, or remove items.

## Example usage

Add an item (example interaction):

- Choose `Add item`
- Enter SKU: `ABC-001`
- Enter name: `Widget`
- Enter quantity: `10`
- Enter price: `9.99` (optional)

Update quantity:

- Choose `Update item`
- Enter SKU: `ABC-001`
- Enter quantity change: `-2` (to reduce stock)

Remove an item:

- Choose `Remove item`
- Enter SKU: `ABC-001`

If you'd like, I can add a non-interactive mode that accepts command-line arguments for scripting.

## Data / Storage suggestions

The script may store data in memory only. Recommended persistence options:

- JSON file — easy to inspect and portable
- CSV file — simple tabular export/import
- SQLite — recommended when you need reliable, multi-session storage

Example JSON record:

```json
{
  "sku": "ABC-001",
  "name": "Widget",
  "quantity": 12,
  "price": 9.99,
  "notes": "Top seller"
}
```

CSV example header:

```
sku,name,quantity,price,notes
ABC-001,Widget,12,9.99,Top seller
```

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