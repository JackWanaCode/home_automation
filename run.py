from api import app
import logging

if __name__ == "__main__":
    logging.basicConfig(filename='flask.log', level=logging.DEBUG)
    app.run(debug=True)
