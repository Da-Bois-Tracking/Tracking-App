from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from routes.hello_route import hello_bp

app = Flask(__name__)

SWAGGER_URL = "/api/docs"
API_URL = "/static/swagger.yml"

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "Tracking App API"}
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
app.register_blueprint(hello_bp)


@app.route("/")
def index():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)
