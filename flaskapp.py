from app import app, db
from app.models import Post


# to set up environment in `flask shell`
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Post': Post}
