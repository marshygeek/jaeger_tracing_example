from src import app as application
from src.settings import get_host_port

if __name__ == '__main__':
    application.run(**get_host_port())
