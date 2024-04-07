# Routes

This folder contains Flask routes that handle incoming HTTP requests and define the application's endpoints.

## Usage
1. Create a new Python file for each route in this folder.
2. Use a meaningful naming convention for your routes. For example, use snake_case and suffix the file name with "_route.py".
   Example: `user_route.py`, `product_route.py`
3. Define the routes using Flask's Blueprint class.
4. Create route functions for each endpoint, implementing the functionality for that endpoint. 
5. Register that route with the Flask application in the `app.py` file.

## Example
```python
from flask import Blueprint

user_bp = Blueprint('user', __name__)

@user_bp.route('/users')
def get_users():
    return 'List of users'

@user_bp.route('/users/<int:user_id>')
def get_user(user_id):
    return f`User {user_id}`
```