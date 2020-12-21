text = []
with open('d2_input.txt') as reader:
    line = reader.readline()
    while line != '':
        text.append(line)
        line = reader.readline()

# list of (min,max, letter, password)
valid = 0
for item in text:
    policy,password = item.split(': ')
    password = password.strip('\n')
    policy, letter = policy.split()
    policy = policy.strip()
    min,max = policy.split('-')
    if (password[int(min)-1] == letter or password[int(max)-1] == letter) and password[int(max)-1] != password[int(min)-1] :
        valid = valid + 1

print(valid)