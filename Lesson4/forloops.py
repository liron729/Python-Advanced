names=["Liron","Egzon","Sara"]

for name in names:
    print(names)



sentence="hello world"

for character in sentence:
    if character.isalpha():
            print(character)


for number in range(1,9):
    print(number)


numbers = [12,45,72,21,8,94,67]

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num
        print("the biggest number in this list is: ",maximum)
