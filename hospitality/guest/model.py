
class Guest(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self):
        return '<User {}'.format(self.email)
