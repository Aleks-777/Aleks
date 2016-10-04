a = int(input())
b = [i**2 for i in range (a-1) if i % 3 == 1]
print(sum(b))
