import re


def hasKeys(fields):
    if fields.get('byr') == None:
        return False
    if fields.get('iyr') == None:
        return False
    if fields.get('eyr') == None:
        return False
    if fields.get('hgt') == None:
        return False
    if fields.get('hcl') == None:
        return False
    if fields.get('ecl') == None:
        return False
    if fields.get('pid') == None:
        return False
    return True


def heightcheck(hightField):
    unitLst = ['cm', 'in']
    hight = hightField[:-2]
    unit = hightField[-2:]
    if unit == 'in':
        if 59 <= int(hight) <= 76:
            return True
    if unit == 'cm':
        if 150 <= int(hight) <= 193:
            return True
    return False


with open('d4_input.txt') as reader:
    line = reader.read()

# list of passport items
ppText = []
ppText = line.split('\n\n')

fields = ppText[1].replace('\n', ' ').split(' ')

# keys
# byr iyr eyr hgt hcl ecl pid cid
eyeColor = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
valid = 0
for passport in ppText:

    fields = dict(subStr.split(':')
                  for subStr in passport.replace('\n', ' ').split(' '))
    if hasKeys(fields):
        byr = fields.get('byr')
        iyr = fields.get('iyr')
        eyr = fields.get('eyr')
        hgt = fields.get('hgt')
        hcl = fields.get('hcl')
        ecl = fields.get('ecl')
        pid = fields.get('pid')
        if int(byr) >= 1920 and int(byr) <= 2002:
            if int(iyr) >= 2010 and int(iyr) <= 2020:
                if int(eyr) >= 2020 and int(eyr) <= 2030:
                    if ecl in eyeColor:
                        if re.search(r"\d{9}", pid) and len(pid) == 9:
                            if re.search(r"^#[\da-f]{6}", hcl):
                                if heightcheck(hgt):
                                    valid = valid + 1
                                    continue
        else:
            print(fields)


print(valid)
