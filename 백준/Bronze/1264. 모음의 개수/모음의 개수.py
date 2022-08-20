collection_fir = "aeiou"
collection_sec = "AEIOU"

while True:
    sum = 0
    str = input()
    if str == "#":
        break
    for i in collection_fir:
        sum += str.count(i)
    for i in collection_sec:
        sum += str.count(i)
    print(sum)

    