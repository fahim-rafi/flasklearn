from practice import db, Puppy

# add_puppy = Puppy("Kukur",3)
# db.session.add(add_puppy)
# db.session.commit()

# read_puppies = Puppy.query.all()
# print(read_puppies)

# select_puppy = Puppy.query.get(1)
# print(select_puppy)
# print(select_puppy.name)

# filter_puppy = Puppy.query.filter_by(age=3)
# print(filter_puppy)
# print(filter_puppy.all())

# update_puppy = Puppy.query.get(1)
# update_puppy.age = 4
# db.session.add(update_puppy)
# db.session.commit()

# delete_puppy = Puppy.query.get(2)
# db.session.delete(delete_puppy)
# db.session.commit()

# all_puppies = Puppy.query.all()
# print(all_puppies)

add_puppy_breed = Puppy.query.get(1)
add_puppy_breed.breed = "labrador"
db.session.add(add_puppy_breed)
db.session.commit()
print(Puppy.query.get(1).breed)