from collections import Counter

ids = []
counts = []
with open('input.txt') as f:
    for id in f.read().split():
        ids.append(id)

for id in ids:
    count = Counter(id)
    counts.append(count)

no_twices = 0
no_thrices = 0

for word in counts:
    isTwice = False
    isThrice = False
    for letter in word:
        print(letter)
        if word[letter] == 2:
        isTwice = True
        if word[letter] == 3:
            isThrice = True
    if isTwice:
        no_twices += 1
    if isThrice:
        no_thrices += 1
        
result = no_twices * no_thrices

print(result)
