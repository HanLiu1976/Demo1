import os

file_count = 0
for dirpath, dirnames, filenames in os.walk('C://temp//RACE//'):
    for file in filenames:
        file_count = file_count + 1
        print(file)

print(file_count)