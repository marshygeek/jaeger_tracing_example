from flask import Flask

app = Flask(__name__)

from src import routes
import threading
from time import sleep

logger = threading.current_thread().logger

logger.log()
logger.finish_scenario()
