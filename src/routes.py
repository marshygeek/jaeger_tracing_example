from flask import request

from src import app
from src import controller


@app.route('/v1/log', methods=['POST'])
def log():
    return controller.log(request.json)


@app.route('/v1/log/finish', methods=['POST'])
def finish_logging():
    return controller.finish_logging(request.json)
