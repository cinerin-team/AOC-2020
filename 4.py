import re


def read_to_array_string_w_d_enter(array, file):
    fo = open(file, "r")
    whole_file = fo.read()
    whole_file = whole_file.replace("\n\n", "@")
    whole_file = whole_file.replace("\n", " ")
    whole_file = whole_file.replace("@", "\n")
    for line in whole_file.split("\n"):
        array.append(line)

    fo.close()

arr = []
array_od_dict =[]
counter = 0

read_to_array_string_w_d_enter(arr, "src_files/4.txt")

for element in arr:
    d = {}
    mo = re.findall(r"(\w+):(\w*|#[0-9a-fA-F]{6})", element)
    for item in mo:
        d[item[0]] = item[1]
    array_od_dict.append(d)

for element in array_od_dict:
    if not ("byr" in element.keys()): continue
    if not ("iyr" in element.keys()): continue
    if not ("eyr" in element.keys()): continue
    if not ("hgt" in element.keys()): continue
    if not ("hcl" in element.keys()): continue
    if not ("ecl" in element.keys()): continue
    if not ("pid" in element.keys()): continue
    counter += 1

print("válasz 4/1: " + str(counter))

array_of_dict = []
counter = 0
for element in arr:
    d = {}
    mo = re.findall(r"(\w+):(#[0-9a-fA-F]{6}|\w*)", element)
    for item in mo:
        d[item[0]] = item[1]
    array_of_dict.append(d)
for element in array_of_dict:
    if not ("byr" in element.keys() and re.match(r'\d{4}', element["byr"]) and 1920 <= int(
            re.match(r'(\d{4})', element["byr"]).group(1)) <= 2002): continue
    if not ("iyr" in element.keys() and re.match(r'\d{4}', element["iyr"]) and 2010 <= int(
            re.match(r'(\d{4})', element["iyr"]).group(1)) <= 2020): continue
    if not ("eyr" in element.keys() and re.match(r'\d{4}', element["eyr"]) and 2020 <= int(
            re.match(r'(\d{4})', element["eyr"]).group(1)) <= 2030): continue
    if not ("hgt" in element.keys() and ((re.match(r'\d+cm', element["hgt"]) and 150 <= int(
            re.match(r'(\d+)cm', element["hgt"]).group(1)) <= 193) or (
                                                 re.match(r'\d+in', element["hgt"]) and 59 <= int(
                                             re.match(r'(\d+)in', element["hgt"]).group(1)) <= 76))): continue
    if not ("hcl" in element.keys() and re.match(r'#[0-9a-fA-F]{6}', element["hcl"])): continue
    if not ("ecl" in element.keys() and re.match(r'^(amb|blu|brn|gry|grn|hzl|oth)$',
                                                 element["ecl"])): continue
    if not ("pid" in element.keys() and re.match(r'\d{9}$', element["pid"])): continue
    counter += 1


print("válasz 4/2: " + str(counter))

