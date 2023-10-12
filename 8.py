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
read_to_array_string(arr, "src_files/8test.txt")

acc = 0
poz = 0
used_instructions = set()

while True:
    if poz in used_instructions:
        break

    used_instructions.add(poz)
    mo = re.search(r'(\w{3})\W(\+|-)(\d+)', arr[poz])
    if mo.group(1) == "nop":
        poz += 1
        continue

    if mo.group(1) == "acc":
        if mo.group(2) == '+':
            acc += int (mo.group(3))
        else:
            acc -= int (mo.group(3))
        poz += 1
        continue

    if mo.group(1) == "jmp":
        if mo.group(2) == '+':
            poz += int (mo.group(3))
        else:
            poz -= int (mo.group(3))

print (acc)

