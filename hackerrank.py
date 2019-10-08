allStrings = []
number = int(input())

for _ in range(number):
    inputString = input()
    allStrings.append(inputString)

uniqueStrings = list(set(allStrings))
print(uniqueStrings)
print(len(uniqueStrings))

for eachString in uniqueStrings:
    print(allStrings.count(eachString), ' ', end='')
