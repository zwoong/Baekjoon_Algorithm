s = input().split()

reversed_fir = int("".join(reversed(s[0])))
reversed_sec = int("".join(reversed(s[1])))

print(reversed_fir) if reversed_fir > reversed_sec else print(reversed_sec)
