from utility import read_to_array_int

arr = []
read_to_array_int(arr, "src_files/1.txt")

x = 0
y = 0
found = False

while x < len(arr) and not found:
    y = x
    while y < len(arr) and not found:
        found = arr[x] + arr[y] == 2020
        y += 1
    x += 1

print("válasz 1/1: " + str(arr[x - 1] * arr[y - 1]))

x = 0
y = 0
z = 0
found = False

while x < len(arr) and not found:
    y = x
    while y < len(arr) and not found:
        z = y
        while z < len(arr) and not found:
            found = arr[x] + arr[y] + arr[z] == 2020
            z += 1
        y += 1
    x += 1

print("válasz 1/2: " + str(arr[x - 1] * arr[y - 1] * arr[z - 1]))
