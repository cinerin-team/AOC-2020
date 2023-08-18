def read_to_array_int(file):
    array = []
    fo = open(file, "r")
    line = fo.readline()
    while line:
        if line[len(line) - 1] == '\n':
            line = line[:-1]
        array.append(int(line))
        line = fo.readline()
    fo.close()
    return array


def part1(arr_local):
    x = 0
    y = 0
    found = False

    while x < len(arr_local) and not found:
        y = x
        while y < len(arr_local) and not found:
            found = arr_local[x] + arr_local[y] == 2020
            y += 1
        x += 1

    return arr_local[x - 1] * arr_local[y - 1]


def part2(arr_local):
    x = 0
    y = 0
    z = 0
    found = False

    while x < len(arr_local) and not found:
        y = x
        while y < len(arr_local) and not found:
            z = y
            while z < len(arr_local) and not found:
                found = arr_local[x] + arr_local[y] + arr_local[z] == 2020
                z += 1
            y += 1
        x += 1
    return arr_local[x - 1] * arr_local[y - 1] * arr_local[z - 1]


if __name__ == '__main__':
    arr = read_to_array_int("src_files/1.txt")

    print("válasz 1/1: " + str(part1(arr)))
    print("válasz 1/2: " + str(part2(arr)))

