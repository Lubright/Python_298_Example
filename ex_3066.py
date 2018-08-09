passbook = {'1': " Wor", 2.2: "gic",
            "Three": "rd", 4: " Ma", "Six": "ld.", 5: "A"}

line = '5-4-2.2-"1"-"Six"'
list_line = [e for e in line.split('-') if e != '']

for i, v in enumerate(list_line):
    if chr(34) in v or chr(39) in v:
        list_line[i] = list_line[i].replace('"', '')
        list_line[i] = list_line[i].replace("'", '')
    else:
        list_line[i] = eval(list_line[i])

# print(list_line)

for e in list_line:
    print(passbook[e], end='')
