from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    tags = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f"Product('{self.name}', '{self.image_url}')"

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    message = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"Log('{self.timestamp}', '{self.message}')"