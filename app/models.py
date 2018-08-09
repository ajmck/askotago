from app import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(250), index=True)
    votes = db.Column(db.Integer)
    posttime = db.Column(db.DateTime)

    comments = db.relationship('Comment', backref='parent', lazy='dynamic')

    def __repr__(self):
        return '<{}: {}>'.format(self.id, self.body)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(250), index=True)
    votes = db.Column(db.Integer)
    posttime = db.Column(db.DateTime)

    parent_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    def __repr__(self):
        return '<{}: {}>'.format(self.id, self.body)
