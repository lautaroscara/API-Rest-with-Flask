# Products REST API with Flask and MySQL

A CRUD REST API for managing supermarket products, built with Flask and MySQL.
It uses parameterized queries to prevent SQL injection, validates input, and
returns meaningful HTTP status codes for each case.

## Requirements
- Python 3.10+
- MySQL or MariaDB

## Setup
1. Create the database and table by running `schema.sql`.
2. Create a dedicated database user for the app:
   ```sql
   CREATE USER 'superuser'@'localhost' IDENTIFIED BY '<your_password>';
   GRANT ALL PRIVILEGES ON super.* TO 'superuser'@'localhost';
   ```
3. Install the dependencies:
   ```bash
   python -m venv venv
   venv\Scripts\activate        # Linux/macOS: source venv/bin/activate
   pip install -r requirements.txt
   ```
4. Set the database password and start the app:
