grades = {
    ("Melina", "Math"): 2,
    ("Dion", "Physics"): 3.5,
    ("festa", "biology"): 5,
    ("reina", "English"): 4,
}

melina_math = grades[("Melina", "Math")]
print("melina's grade in math is", melina_math )

grades[("Dion", "physics")] = 3
print(grades)

keys = list(grades.keys())

student, subject = keys[0]
print(student, "'s grade in ", subject, " is " , melina_math)