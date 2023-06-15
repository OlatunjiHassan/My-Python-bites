import random, time

#def keepstreaks(element, streak):



numberOfStreaks = 0
luck = ["H", "T"]
fileH = []
fileT = []
recordT = 0
recordH = 0
indexH = []
indexT = []
for experimentNumber in range(10000):
    q = random.choice(luck)
    if q == "H":
        fileT.clear()
        fileH.append(q)
        if len(fileH) == 6:
            recordH += 1

    if q == "T":
        fileH.clear()
        fileT.append(q)
        if len(fileT) == 6:
            recordT += 1

print("The total number of 6 heads streak is " + str(recordH))
print("\nThe total number of 6 tails streak is " + str(recordT))
numberOfStreaks = recordH + recordT
print("\nTotal streaks is " + str(numberOfStreaks))

print(f"\nprobability of streak: {numberOfStreaks / 100}%")



