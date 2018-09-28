from src import app
from src.settings import get_host_port

if __name__ == '__main__':
    app.run(**get_host_port())
