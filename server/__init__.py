import os
from flask import Flask, jsonify, send_from_directory, session, request, send_file
from flask_cors import CORS
from server.views import landing

def create_app():
    app = Flask(__name__, template_folder='templates')
    if os.getenv("FLASK_ENV", 'dev') == 'production':
        DB_URL = 'sqlite:///dev.sqlite'

    app.config['SECRET_KEY'] = os.urandom(24)
    app.register_blueprint(landing)
    CORS(app,
        origins=["http://localhost:3000"],
        headers=['Content-Type'],
        expose_headers=['Access-Control-Allow-Origin'],
        supports_credentials=True
    )
    return app
