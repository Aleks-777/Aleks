n = int(input())
a = []
b = 0
a =  list(map(int, input().split()))
Pick = int(input())
c = n - 2
for i in range (n-2):
    s = a[i] + a[i+1] + a[i+2]
    if s > b :
        b = s
print(b)