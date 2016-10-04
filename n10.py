n = int(input())+1
b = [1]
c = [1]
print (1)
if n > 2:
    print(1, 1)
while n-2 > 0 :
    b = [int(b[i]) + int(b[i-1]) for i in range (0,len(b))]
    b.extend(c)
    c.extend(b)
    print(*c)
    n -= 1
    a = b
    c = [1]