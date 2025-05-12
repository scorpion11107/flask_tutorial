import click
from waitress import serve

from . import db
from . import app

@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    db.init_db()
    click.echo('Initialized the database.')

@click.command('run-app')
def run_app_command():
    """Run flaskr"""
    click.echo('Starting server...')
    serve(app, host='0.0.0.0', port=8080)

def init_app(app):
    app.teardown_appcontext(db.close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(run_app_command)