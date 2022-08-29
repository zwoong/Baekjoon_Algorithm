n = int(input())

for _ in range(n):
    g = 0
    b = 0
    name = input()
    for s in name:
        if s == "g" or s == "G":
            g += 1
        elif s == "b" or s == "B":
            b += 1
    if g == b:
        print(name + " is " + "NEUTRAL")
    elif g > b:
        print(name + " is " + "GOOD")
    else:
        print(name + " is " + "A BADDY")
