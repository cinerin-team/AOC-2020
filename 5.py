def read_to_array_string(array, file):
    fo = open(file, "r")
    line = fo.readline()
    while line:
        if line[len(line) - 1] == '\n':
            line = line[:-1]
        array.append(line)
        line = fo.readline()


def f_char(rowMin, rowMax):
    return int((rowMax - rowMin) / 2)


def b_char(rowMin, rowMax):
    return rowMax - int((rowMax - rowMin) / 2)


def r_char(columnMin, columnMax):
    return columnMax - int((columnMax - columnMin) / 2)


def l_char(columnMin, columnMax):
    return int((columnMax - columnMin) / 2)


arr = []
rowMin, rowMax = 0, 127
columnMin, columnMax = 0, 7
selectedRow, selectedColumn = 0, 0
boardingPasses = []
missing = []
for i in range(128):
    for j in range(8):
        missing.append(i * 8 + j)

read_to_array_string(arr, "src_files/5.txt")

for boardingpass in arr:
    coord = 0
    rowMin, rowMax = 0, 127
    columnMin, columnMax = 0, 7
    selectedRow, selectedColumn = 0, 0
    for letter in boardingpass:
        if coord == 6:
            if letter == 'F':
                selectedRow = rowMin
            else:
                selectedRow = rowMax
            coord += 1
        if coord == 10:
            if letter == 'R':
                selectedColumn = columnMax
            else:
                selectedColumn = columnMin
            # coord += 1
        if letter == 'F':
            rowMax = rowMax - f_char(rowMin, rowMax) - 1
            coord += 1
        if letter == 'B':
            rowMin = b_char(rowMin, rowMax)
            coord += 1
        if letter == 'R':
            columnMin = r_char(columnMin, columnMax)
            coord += 1
        if letter == 'L':
            columnMax = columnMax - l_char(columnMin, columnMax) - 1
            coord += 1
    boardingPasses.append(selectedRow * 8 + selectedColumn)
    missing.remove(selectedRow * 8 + selectedColumn)
maxBoardingPass = max(boardingPasses)

print(maxBoardingPass)
print(missing)
