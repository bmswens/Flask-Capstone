# 3rd party
from flask import Flask


# app factory
def create_app():
    app = Flask(
        __name__,
        static_folder="static"
    )

    return app
