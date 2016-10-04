A = list(map(int, input().split()))
b = 0
c = 0
for i in range (0,9):
    if A[i] == 2 and A[i+1]!=2:
        b += 1
        c += 1
while b > 0:
    b -= 1
    A.pop(A.index(2))
v = sum(A)/(10-c)/1
print(int(v))