from sys import stdin

data = [line.strip("\n") for line in stdin]
for line in data[:len(data) - 1]:
    if line.lower().find(data[-1].lower()) != -1:
        print(line)
