from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from routes.hello_route import (
    hello_bp,
)  # Import the hello_bp Blueprint from the routes package

# Create the Flask application
app = Flask(__name__)

# Define the URL paths for Swagger UI and the Swagger Yaml file
SWAGGER_URL = "/api/docs"
API_URL = "/static/swagger.yml"

# Create a Swagger UI blueprint with the specified URLs and configuration
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "Tracking App API"}
)

# Register the Swagger UI blueprint with the Flask application
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
app.register_blueprint(hello_bp)


# Define a route for the root URL
@app.route("/")
def index():
    return "Hello, World!"


# Start the Flask application if this script is executed
if __name__ == "__main__":
    app.run(debug=True)
