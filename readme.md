# Data Acquisition System Scripts

This project includes two Python scripts for reading and writing data in an SQLite database.

## Scripts

### `write_data.py`
- **Purpose**: Generates mock data and writes it to `data_acquisition.db`.
- **How to Use**: Run the script:
    ```bash
    python write_data.py
    ```

### `read_data.py`
- **Purpose**: Reads and prints data from `data_acquisition.db` with formatted output.
- **How to Use**: Run the script:
    ```bash
    python read_data.py
    ```

## Requirements
- Python 3.x (no external dependencies).

## Notes
- Ensure `write_data.py` is run before `read_data.py` to populate the database.