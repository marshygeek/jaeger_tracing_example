from flask import Flask

app = Flask(__name__)

from src import routes
from src.controller import logger

logger.log()  # this case will work
logger.finish_scenario()
