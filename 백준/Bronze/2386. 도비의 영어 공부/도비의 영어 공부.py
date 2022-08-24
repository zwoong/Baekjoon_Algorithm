while True:
    str = input().split()

    if str[0] == "#":
        break

    find_str = str[0]
    sum = 0
    for s in str[1:]:
        sum += s.count(find_str.lower())
        sum += s.count(find_str.upper())

    print("{0} {1}".format(find_str, sum))