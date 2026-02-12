from numpy.array_api import empty

word = ("spam", "eggs", "mouse")

print(word[0])

empty_tuple = ()
print(empty_tuple)


person = ("Liron", 17, "billionaire")

name, age, profession = person

print(name,"'s", "profession is" , profession, "and she is", age, "years old")