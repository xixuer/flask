from flask import Flask
from controller.index import index
import os

app = Flask(__name__,template_folder="template")
app.config['SECRET_KEY'] = os.urandom(24)
app.register_blueprint(index)

if __name__ == "__main__":
    app.run()

