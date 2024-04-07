from flask import Blueprint, jsonify
from models.hello_model import HelloResponse

hello_bp = Blueprint("hello", __name__)


@hello_bp.route("/hello")
def hello():
    response_model = HelloResponse(message="Hello from Flask!")
    return jsonify(response_model.model_dump())
