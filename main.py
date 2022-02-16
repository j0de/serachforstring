filename = input("Please enter the filename: ")
string1 = input("Please enter your string:  ")
file1 = open(filename, "r")
instances = []


flag = 0
index = 0

for line in file1:
    index += 1

    if string1 in line:
        flag = 1
        instances.append(index)

if flag == 0:
    print('String', string1, 'Not Found')
else:
    print('String', string1, 'Found In Lines', instances)

file1.close()
