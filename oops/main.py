from oops.ParrotModel import Parrot

p1 = Parrot("Amar", 28)
p2 = Parrot("Uday", 34)

print("class level variable", p1.__class__.species, p1.name)
print("object level variable", p2.name, p2.age)
