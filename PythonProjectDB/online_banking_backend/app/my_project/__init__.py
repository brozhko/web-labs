import os
import yaml
from flask import Flask
from .auth.domain.models import db
from .auth.route.client_routes import client_bp
from .auth.route.account_routes import account_bp
from .auth.route.payment_routes import payment_bp
from .auth.route.transaction_routes import transaction_bp
from .auth.route.reference_routes import reference_bp


def load_config():
    config_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "config",
        "app.yml"
    )
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def create_app():
    cfg = load_config()

    app = Flask(__name__)
    app.config["SECRET_KEY"] = cfg["flask"]["secret_key"]
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"mysql+pymysql://{cfg['database']['user']}:"
        f"{cfg['database']['password']}@"
        f"{cfg['database']['host']}:"
        f"{cfg['database']['port']}/"
        f"{cfg['database']['name']}"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # Реєстрація blueprints
    app.register_blueprint(client_bp, url_prefix="/api/clients")
    app.register_blueprint(account_bp, url_prefix="/api/accounts")
    app.register_blueprint(payment_bp, url_prefix="/api/payments")
    app.register_blueprint(transaction_bp, url_prefix="/api/transactions")
    app.register_blueprint(reference_bp, url_prefix="/api/ref")

    @app.route("/")
    def index():
        return {"message": "OnlineBanking API works"}

    return app
