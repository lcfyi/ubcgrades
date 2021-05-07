from flask_frozen import Freezer
from config import Config
from app import create_app


if __name__ == "__main__":
    Config.FREEZER_DESTINATION = "../build"
    Config.FREEZER_BASE_URL = "https://lcfyi.github.io/ubcgrades/"
    app, _ = create_app(Config)
    freezer = Freezer(app)
    freezer.freeze()
