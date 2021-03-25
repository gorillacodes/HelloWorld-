ignore = ['a', 'A']

with open('test.txt', 'r') as test, open('test2.txt', 'w') as test2:
    for line in test:
        if not any(ignorech in line for ignorech in ignore):
            test2.write(line)
