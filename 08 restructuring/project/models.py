from project import db

## Puppies table
class Puppy(db.Model):
    __tablename__ = 'puppies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner',backref="puppy",uselist=False)
    
    def __init__(self,name):
        self.name = name
    
    def __repr__(self):
        if self.owner:
            return f"{self.name} with an ID of {self.id} has been adopted by {self.owner.name}"
        else:
            return f"{self.name} with an ID of {self.id} has not been adopted yet! :( "

## Owners table
class Owner(db.Model):
    __tablename__ = "owners"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer,db.ForeignKey("puppies.id"))

    def __init__(self,name,puppy_id):
        self.name = name
        self.puppy_id = puppy_id