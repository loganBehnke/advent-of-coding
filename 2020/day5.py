boardingpass = []
with open('d5_input.txt') as reader:
    line = reader.readline().strip('\n')
    while line != '':
        boardingpass.append(line)
        line = reader.readline().strip('\n')
seatIDs = []
for seat in boardingpass:
    low = 0
    high = 127
    for letter in seat[:-3]:
        if letter == 'F':
            high = int((high-low) / 2) + low
        elif letter == 'B':
            low = int((high-low) / 2) + 1 + low
    row = low
    low = 0
    high = 7
    for letter in seat[-3:]:
        if letter == 'L':
            high = int((high-low)/2) + low
        elif letter == 'R':
            low = int((high-low)/2) + low + 1
    col = low
    seatID = row * 8 + col
    seatIDs.append(seatID)
seatIDs.sort()
for seat in range(len(seatIDs)-1):
    if seatIDs[seat] + 1 != seatIDs[seat+1]:
        print(seatIDs[seat] + 1)
