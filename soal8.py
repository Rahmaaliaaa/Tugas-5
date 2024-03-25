a = 1
b = 2
c = 3

print(a, end = "")
print(b, end = "")
print(c, end = "")

for i in range(7):
    d = a + b + c
    print(d, end = "")
    a = b
    b = c
    c = d
print()     