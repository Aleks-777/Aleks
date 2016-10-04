a = list(map(int, input().split()))
for i in range(1, len(a), 2):
    a.insert(i, a[-1])
    a.pop(-1)
print(' '.join(map(str, a[::1])), end=" ")