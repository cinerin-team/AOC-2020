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
counter = []

read_to_array_string_w_d_enter(arr, "src_files/6.txt")
print()

for blokkok in arr:
    igenek = set()
    igenek.clear()
    for betuk in blokkok:
        if betuk != " ":
            igenek.add(betuk)
    counter.append(len(igenek))

print(sum(counter))
counter.clear()

for blokkok in arr:
    igenek = {}
    person =1
    szamlalo =0
    for betuk in blokkok:
        if betuk == " ":
            person +=1
        else:
            if not betuk in igenek.keys():
                igenek[betuk] = 1
            else:
                igenek[betuk] = igenek[betuk] +1
    for betun_in_dict in igenek.keys():
        if igenek[betun_in_dict] == person:
            szamlalo +=1
    counter.append(szamlalo)

print(sum(counter))
