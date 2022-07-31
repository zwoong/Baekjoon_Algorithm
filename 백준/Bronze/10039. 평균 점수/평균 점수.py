원섭 = int(input())
세희 = int(input())
상근 = int(input())
숭 = int(input())
강수 = int(input())

if 원섭 < 40:
    원섭 = 40
if 세희 < 40:
    세희 = 40
if 상근 < 40:
    상근 = 40
if 숭 < 40:
    숭 = 40
if 강수 < 40:
    강수 = 40

print(int((원섭 + 세희 + 상근 + 숭 + 강수) / 5))
