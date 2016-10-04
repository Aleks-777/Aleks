N = int(input())
a = []
b = []
c =0
for i in range (N) :
    f = list(map(int, input().split()))
    a.append(f[0])
    b.append(f[1])
    f = []
#print(a)
#print(b)
T = int(input())
for i in range (N):
    if a[i] <= T and T <= b[i]:
        c +=1
print(c)