from api.config import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titles = db.Column(db.String(50))
    content = db.Column(db.String(255))

    def __repr__(self):
        return '<Post %s>' % self.title


class Register(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String)
    password=db.Column(db.String)
    first_name=db.Column(db.String(50))
    last_name=db.Column(db.String(50))

