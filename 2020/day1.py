
inputF = []
with open("d1_input.txt", 'r') as reader:
    line = reader.readline()
    while line != '':
        inputF.append(int(line))
        line = reader.readline()
    done = False
    for i in inputF:
        for j in inputF:
            for k in inputF:
                if i+j+k == 2020:
                    print(i*j*k)
                    done = True
                    break
            if done:
                break
        if done:
            break
