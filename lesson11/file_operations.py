# file_path = "example.txt"
# file = open(file_path, "r")
#
# content = file.read()
# print(content)
#
# file.close()

import os
from turtledemo.clock import datum

file = open('example.txt')
file.close()


with open('example.txt', 'r') as file:
    content = file.read()


with open('example.txt', 'r') as file:
    content = file.read()
    line = file.readline()
    lines = file.readlines()


with open('example.txt', 'w') as file:
    file.write("hello world")

lines = ['hello world\n', 'welcome to py\n']
with open('example.txt', 'w') as file:
    file.writelines(lines)



with open('example.txt', 'r') as file:
    file.seek(0)
    data = file.read()
    print(data)

    if os.path.exists('example.txt'):
        print('file exists')


with open('example.txt', 'a') as file:
    file.write("new data appended")


data = b'this is sum binary stuff'
with open('example.bin', 'wb') as file:
    file.write(data)