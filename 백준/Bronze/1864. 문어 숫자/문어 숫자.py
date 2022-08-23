temp = ["-", "\\", "(", "@", "?", ">", "&", "%", "/"]
while True:
    str = input()
    if str == "#":
        break
    sum = 0
    for i in range(len(str), 0, -1):
        if str[len(str) - i] != "/":
            sum += temp.index(str[len(str) - i]) * 8**(i - 1)
        else:
            sum += -1 * 8**(i - 1)

    print(sum)
