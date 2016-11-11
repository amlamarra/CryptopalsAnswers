#!/usr/bin/python3

with open("08.txt") as f:
    content = f.read()

lines = content.split("\n")
blocks = [[] for i in range(len(lines))]

for line in lines:
    for i in range(0, len(line), 32):
        blocks[lines.index(line)].append(line[i:i+32])

for block in blocks:
    seen = set()
    for i in range(len(block)):
        if block[i] in seen:
            print("Index: [{}][{}]  |  Duplicate: {}".format(blocks.index(block), i, block[i]))
            found = blocks.index(block)
        else:
            seen.add(block[i])

print("\nThis ciphertext was likely encrypted with AES in ECB mode:")
print(lines[found])
