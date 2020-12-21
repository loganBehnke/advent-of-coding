with open('d6_input.txt') as reader:
    line = reader.read()

groups = line.split('\n\n')
yesCount = 0
for group in groups:
    answersLst = []
    people = group.split('\n')
    groupSet = set(people[0])
    for person in people:
        newSet = set(person)
        groupSet = groupSet.intersection(newSet)

    yesCount = yesCount + len(groupSet)
print(yesCount)
