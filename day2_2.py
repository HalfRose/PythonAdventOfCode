ids = []
results = []
with open('input.txt') as f:
    for id in f.read().split():
        ids.append(id)
        
for id1 in ids:
    for id2 in ids:
        differs_on = 0
        if id1 != id2:
            for index in range(len(id1)):
                if id1[index] != id2[index]:
                    differs_on += 1
            if differs_on == 1:
                results.append([id1, id2])

# the algorithm produces two symmetrical results so we can take the first one
result = results[0]
common_letters = []
for i in range(len(result[0])):
    if result[0][i] == result[1][i]:
        common_letters.append(result[0][i])
final_letters = "".join(common_letters)

print(final_letters)
