def read_to_array_string(array, file):
    fo = open(file, "r")
    line = fo.readline()
    while line:
        if line[len(line) - 1] == '\n':
            line = line[:-1]
        array.append(line)
        line = fo.readline()


arr = []

read_to_array_string(arr, "src_files/3.txt")

x = 0
y = 0
hossz = len(arr[0])
counter = 0

# jobbra 3 le 1
while y < len(arr):
    if (arr[y][x] == "#"):
        counter += 1
    x += 3
    y += 1
    if x >= hossz:
        x -= hossz

print("válasz 3/1: " + str(counter))

hossz = len(arr[0])
counter = 0
local_counter = 0

# jobbra 1 le 1
x = 0
y = 0
while y < len(arr):
    if (arr[y][x] == "#"):
        counter += 1
    x += 1
    y += 1
    if x >= hossz:
        x -= hossz
print(counter)

# jobbra 3 le 1
x = 0
y = 0
local_counter = 0

while y < len(arr):
    if (arr[y][x] == "#"):
        local_counter += 1
    x += 3
    y += 1
    if x >= hossz:
        x -= hossz
print(local_counter)

counter *= local_counter
# jobbra 5 le 1
x = 0
y = 0
local_counter = 0

while y < len(arr):
    if (arr[y][x] == "#"):
        local_counter += 1
    x += 5
    y += 1
    if x >= hossz:
        x -= hossz
print(local_counter)

counter *= local_counter

# jobbra 7 le 1
x = 0
y = 0
local_counter = 0

while y < len(arr):
    if (arr[y][x] == "#"):
        local_counter += 1
    x += 7
    y += 1
    if x >= hossz:
        x -= hossz
print(local_counter)

counter *= local_counter

# jobbra 1 le 2
x = 0
y = 0
local_counter = 0

while y < len(arr):
    if (arr[y][x] == "#"):
        local_counter += 1
    x += 1
    y += 2
    if x >= hossz:
        x -= hossz
print(local_counter)


counter *= local_counter

print("válasz 3/2: " + str(counter))
