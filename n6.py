n = int(input())
A = list(map(int, input().split()))
for i in range (len(A)//2):
    b = A.index(max(A))
    A.pop(b)
    c = A.index(min(A))
    A.pop(c)
print(*A)