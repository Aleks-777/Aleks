b, c = map(int, input().split())
a = []
for i in range(c+1):
    if i <= (b-1):
        a.append(1)
    else:
        a.append(sum(a[i - 3:i]))
print(a[-1])