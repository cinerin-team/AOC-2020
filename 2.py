import re


def read_to_array_string(array, file):
    fo = open(file, "r")
    line = fo.readline()
    while line:
        if line[len(line) - 1] == '\n':
            line = line[:-1]
        array.append(line)
        line = fo.readline()


arr = []
read_to_array_string(arr, "src_files/2.txt")

counter = 0
for element in arr:
    mo = re.match(r"(\d+)-(\d+)\W(\w):\W(\w+)", element)
    if mo and (int(mo.group(1)) <= mo.group(4).count(mo.group(3)) <= int(mo.group(2))):
        counter += 1

print("válasz 2/1: " + str(counter))

counter = 0
for element in arr:
    mo = re.match(r"(\d+)-(\d+)\W(\w):\W(\w+)", element)
    if mo and ((mo.group(4)[int(mo.group(1))-1] == mo.group(3)) ^ (mo.group(4)[int(mo.group(2))-1] == mo.group(3))):
        counter += 1

print("válasz 2/2: " + str(counter))
