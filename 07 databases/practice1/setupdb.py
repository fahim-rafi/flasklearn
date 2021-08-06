from practice import db,Puppy

db.create_all()

kallu = Puppy("Kallu",5)
tyson = Puppy("Tyson",1)

db.session.add_all([kallu,tyson])

db.session.commit()

print(kallu.id)
print(tyson.id)
