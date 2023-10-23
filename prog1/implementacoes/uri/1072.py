n = int(input())
dentro = 0
fora = 0
for i in range(n):
    k = int(input())
    if k >=10 and k<=20:
        dentro+=1
    else:
        fora+=1
print(f"{dentro} in\n{fora} out")
