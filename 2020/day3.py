map = []
colLength = 0
with open('d3_input.txt') as reader:
    line = reader.readline().strip('\n')
    colLength = len(line)
    while line != '':
        map.append(line)
        line = reader.readline().strip('\n')

# right 1, down 1
row = 0
col = 0
treeCount1 = 0
while row < len(map):
    if map[row][col] == '#':
        treeCount1 = treeCount1 + 1
    row = row + 1
    col = (col + 1) % colLength

# right 3, down 1
row = 0
col = 0
treeCount2 = 0
while row < len(map):
    if map[row][col] == '#':
        treeCount2 = treeCount2 + 1
    row = row + 1
    col = (col + 3) % colLength

# right 5, down 1
row = 0
col = 0
treeCount3 = 0
while row < len(map):
    if map[row][col] == '#':
        treeCount3 = treeCount3 + 1
    row = row + 1
    col = (col + 5) % colLength

# right 7, down 1
row = 0
col = 0
treeCount4 = 0
while row < len(map):
    if map[row][col] == '#':
        treeCount4 = treeCount4 + 1
    row = row + 1
    col = (col + 7) % colLength

# right 1, down 2
row = 0
col = 0
treeCount5 = 0
while row < len(map):
    if map[row][col] == '#':
        treeCount5 = treeCount5 + 1
    row = row + 2
    col = (col + 1) % colLength

print(treeCount1*treeCount2*treeCount3*treeCount4*treeCount5)
