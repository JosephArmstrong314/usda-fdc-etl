import os

NUM_FILES = 500

b26_1 = 0
b26_2 = 0

count = 0

master = 'abcdefghijklmnopqrstuvwxyz'

names = []

for N in range(NUM_FILES):

    name = 'x' + master[b26_2] + master[b26_1]
    names.append(name)

    b26_1 += 1
    if (b26_1 == 26):
        b26_2 += 1
        b26_1 = 0
    count += 1

for n in range(len(names)):
    newName = f'brandedDownload{n}.txt'
    os.rename(names[n], newName)