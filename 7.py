import re


def read_to_array_string(array, file):
    fo = open(file, "r")
    line = fo.readline()
    while line:
        if line[len(line) - 1] == '\n':
            line = line[:-1]
        array.append(line)
        line = fo.readline()


def check_a_bag_content_shiny_gold(contents, bags):
    content = contents.split(", ")
    for item in content:
        mo = re.match(r'(\d+)\W(.+)', item)
        if mo:
            if mo.group(2) == "shiny gold":
                return True
            else:
                if check_a_bag_content_shiny_gold(bags[mo.group(2)], bags):
                    return True

    return False


def extract_bag(starter, bags):
    if bags[starter] == "no other":
        return 0
    else:
        counter = 0
        content = bags[starter].split(", ")
        for item in content:
            mo = re.match(r'(\d+)\W(.+)', item)
            counter += (int(mo.group(1)) + int(mo.group(1)) * extract_bag(mo.group(2), bags))
        return counter


arr = []
read_to_array_string(arr, "src_files/7.txt")
arr = list(map(lambda st: str.replace(st, "bags", "bag"), arr))
arr = list(map(lambda st: str.replace(st, " bag", ""), arr))
arr = list(map(lambda st: str.replace(st, ".", ""), arr))

bag_list = {}
for item in arr:
    mo = re.match(r'(\w*\W\w*)\Wcontain\W(.*)', item)
    bag_list[mo.group(1)] = mo.group(2)

counter = 0
for bag in bag_list.keys():
    if check_a_bag_content_shiny_gold(bag_list[bag], bag_list):
        counter += 1

print(counter)
arr = list(map(lambda st: str.replace(st, "bags", "bag"), arr))
arr = list(map(lambda st: str.replace(st, " bag", ""), arr))
arr = list(map(lambda st: str.replace(st, ".", ""), arr))
bag_list = {}

for item in arr:
    mo = re.match(r'(\w*\W\w*)\Wcontain\W(.*)', item)
    bag_list[mo.group(1)] = mo.group(2)

starter_bag = "shiny gold"

print(extract_bag(starter_bag, bag_list))
