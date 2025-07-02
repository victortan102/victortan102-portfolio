from flask import Flask

from routes.home import home_bp
from routes.software import software_bp
from routes.hardware import hardware_bp


app = Flask(__name__, template_folder="pages", static_folder="assets")


# Register blueprints
app.register_blueprint(home_bp, url_prefix="/")
app.register_blueprint(software_bp, url_prefix="/software")
app.register_blueprint(hardware_bp, url_prefix="/hardware")


if __name__ == "__main__":
    app.run()
