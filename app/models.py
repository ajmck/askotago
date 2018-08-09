from app import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(250), index=True)

    def __repr__(self):
        return '<{}: {}>'.format(self.id, self.body)
