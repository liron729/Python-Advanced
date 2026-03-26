


with open('example.txt', 'r') as file:
    for line in file:
        cleaned_line = line.strip()
        print(cleaned_line)

with open('example.txt', 'r') as file:
    for line in file:
        words = line.strip().split()
        print(words)

name = "Liron"
age = 18

with open("output.txt", "w") as file:
    file.write("Name: " + name + "\n")
    file.write("age: " + age + "\n")

with open("output.txt", "w") as file:
    file.write(f"Name:  + {name}\n")
    file.write(f"age:  + {age} \n")

with open('example.txt', 'r') as infile, open('output.txt' , 'r'):
    for line in infile:
        cleaned_line = line.strip()
        modified_line = cleaned_line.replace("line 1", "Line X")
        outfile.write(modified_line + "\n")