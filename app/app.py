import os
import logging
from flask import Flask

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

@app.route('/')
def hello_world():
    logging.info("Received request for / endpoint")
    name = os.environ.get('NAME', 'World')
    message = f'Hello {name}!\n'
    logging.info(f"Responding with: {message.strip()}")
    return message

if __name__ == "__main__":
    logging.info("Starting Flask application")
    app.run(debug=True, host='0.0.0.0', port=8080)
