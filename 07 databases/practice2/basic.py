from practice import db, Puppy,Toy,Owner

kallu = Puppy("Kallu")
tyson = Puppy("Tyson")

db.session.add_all([kallu,tyson])
db.session.commit()

tyson = Puppy.query.filter_by(name="Tyson").first()
print(tyson)

yamin = Owner("Yamin",tyson.id)

tyson_toy_1 = Toy("Haddi",tyson.id)
tyson_toy_2 = Toy("Ball",tyson.id)

db.session.add_all([yamin,tyson_toy_1,tyson_toy_2])
db.session.commit()

tyson = Puppy.query.filter_by(name="Tyson").first()
print(tyson)
tyson.report_toys()