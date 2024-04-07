from flask import Blueprint, jsonify
from models.hello_model import (
    HelloResponse,
)  # Import the HelloResponse model from the models package

# Create a Flask Blueprint for the hello route
hello_bp = Blueprint("hello", __name__)


# Define the route for the /hello endpoint
@hello_bp.route("/hello")
def hello():
    # Create a HelloResponse instance with the message "Hello from Flask!"
    response_model = HelloResponse(message="Hello from Flask!")
    # Return the JSON representation of the response model
    return jsonify(response_model.model_dump())
