import os

from flask import Flask
app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
)
app.config.from_pyfile('config.py', silent=True)

try:
    os.makedirs(app.instance_path)
except OSError:
    pass

from . import db
db.init_app(app)

from . import auth
app.register_blueprint(auth.bp)

from . import blog
app.register_blueprint(blog.bp)
app.add_url_rule('/', endpoint='index')

# a simple page that says hello
@app.route('/hello')
def hello():
    return 'Hello, World!'