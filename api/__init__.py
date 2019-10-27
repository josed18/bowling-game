from flask import Flask
from flask_caching import Cache

app = Flask(__name__)

app.config.from_pyfile('../settings.cfg')
app.cache = Cache(app)
