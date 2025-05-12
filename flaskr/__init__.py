import os

from flask import Flask

# create and configure the app
app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass
    
from . import click_commands
click_commands.init_app(app)

from . import auth
from . import blog

app.register_blueprint(auth.bp)
app.register_blueprint(blog.bp)

app.add_url_rule('/', endpoint='index')