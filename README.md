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
   ```bash
   set MYSQL_PASSWORD=<your_password>              # CMD
   $env:MYSQL_PASSWORD = '<your_password>'         # PowerShell
   export MYSQL_PASSWORD=<your_password>           # Linux/macOS
   python run.py
   ```

The API runs at `http://localhost:5000`.

### Environment variables
Credentials are read from the environment, so they are never stored in the code.

| Variable | Default |
|----------|---------|
| `MYSQL_HOST` | `localhost` |
| `MYSQL_USER` | `superuser` |
| `MYSQL_PASSWORD` | *(empty)* |
| `MYSQL_DB` | `super` |
| `FLASK_DEBUG` | *(off; set to `1` to enable debug mode)* |

## Endpoints

| Method | Route | Description | Responses |
|--------|-------|-------------|-----------|
| GET | `/products` | List all products | 200 |
| GET | `/products/<codigo>` | Get a single product | 200, 404 |
| POST | `/products` | Create a product | 201, 400, 409 |
| PUT | `/products/<codigo>` | Update a product | 200, 400, 404 |
| DELETE | `/products/<codigo>` | Delete a product | 200, 404 |

### Status codes
- **200**: request succeeded.
- **201**: product created.
- **400**: missing field or invalid value in the request body.
- **404**: the product does not exist.
- **409**: a product with that `codigo` already exists.

### Request body
POST (for PUT, send the same body without `codigo`):
```json
{
  "codigo": 1,
  "descrip": "Milk",
  "stock": 10,
  "precio": 1500.50,
  "sector": "Dairy",
  "marca": "Brand",
  "foto": "milk.jpg"
}
```

### Example error response
```json
{ "message": "ERROR. Missing field: stock" }
```

## Technical notes
- All SQL queries are parameterized (`%s` placeholders), never built by
  string concatenation.
- Each endpoint checks whether the product exists before updating or
  deleting it, and the cursor is always closed before returning.
- `precio` is stored as `DECIMAL(10,2)`, so the JSON response returns it as
  a string to avoid losing precision.

## Project structure
```
app/
  __init__.py    # Flask app and MySQL configuration
  routes.py      # Endpoints
run.py           # Entry point
schema.sql       # Database and table definition
requirements.txt
```
