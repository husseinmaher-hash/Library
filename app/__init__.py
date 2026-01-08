from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import AppConfig

database = SQLAlchemy()
migration = Migrate()
def createApp():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = AppConfig.secretKey
    app.config["SQLALCHEMY_DATABASE_URI"] = AppConfig.databaseUrl
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = AppConfig.sqlalchemyTrackModifications

    database.init_app(app)
    
    #to ensure registered with SQLAlchemy before migration
    from .module.library import Library
    from .module.books import Book

    migration.init_app(app, database)

    from .routes.library_routes import libraryBP
    from .routes.book_routes import bookBP
    app.register_blueprint(libraryBP)
    app.register_blueprint(bookBP)

    @app.route("/")
    def indexRoute():
        return {"status": "ok"}

    return app
