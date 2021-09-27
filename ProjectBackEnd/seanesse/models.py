from seanesse import db



class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(160), nullable=False)
    datet = db.Column(db.String(80),unique=True, nullable=False)
    descrip = db.Column(db.String(200),unique=True, nullable=False)
    image = db.Column(db.String(160))
    
    def __repr__(self):
        return '<User %r>' % self.title


class Prodact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(20), nullable=False)



# slayd sekil anseyfe
# carda seil()