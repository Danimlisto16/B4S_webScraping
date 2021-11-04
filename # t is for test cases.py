import itertools

def sumNnumbers(first, last):
    return (last / 2) * (first + last)

def verifyDays(listPossibilities, maxDay):
    sumN = sumNnumbers(1, maxDay)
    flag = False
    allComb = list(itertools.product(*listPossibilities))
    for i in allComb:
        sumTotal = 0
        for x in i:
            sumTotal = x + sumTotal
        if sumTotal == sumN:
            flag = True
            iterador = list(i)
    if flag:
        iterador.sort()
        return iterador
    else:
        return "impossible"


# t is for test cases

t = 0
while (t < 1 or t > 30):
    t = int(input(""))

#nCase
nCase = 1


solutions = []
while (nCase <= t):
    patients = int(input(""))
    nPatients = 1
    patientsList = []
    possibleDays = []
    while (nPatients <= patients):
        limits = input("")
        l = limits.split(" ")
        li = int(l[0])
        ls = int(l[1])
        if li == ls:
            for i in range(patients-1):
                possibleDays.append(0.1)
            possibleDays.append(li)
        else:
            for i in range(li, ls + 1):
                possibleDays.append(i)
        patientsList.append(possibleDays)
        nPatients = nPatients + 1
    sol = verifyDays(patientsList, patients)
    solutions.append(sol)
    nCase = nCase + 1

for i in solutions33:
    if i != "impossible":
        for x in i:
            print(x, " ", end='')
        print("")
    else:
        print(i)