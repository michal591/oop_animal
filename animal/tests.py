from models import Animal, Dog, Cat, Street_cat

dog = Animal("rexi", "8")
print(dog)

dog2 = Dog("rexi", "5")
print(dog2)
dog2.make_sound()
dog2.is_pure(False)

cat = Cat("Mizi", "2")
print(cat)
cat.make_sound()
cat.is_ear_cat(False)

cat2 = Street_cat("Pizi", "3")
print(cat2)
cat2.make_sound()
