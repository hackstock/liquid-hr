import os
from flask_migrate import Migrate
from app import create_app, db
from app.models import User, Profile

app = create_app(os.getenv("APP_CONFIG") or "default")
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Profile = Profile)

@app.cli.command()
def test():
    """Runs unit tests"""
    import unittest
    tests = unittest.TestLoader().discover("test")
    unittest.TextTestRunner(verbosity=2).run(tests)