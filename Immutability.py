x = 10
print(id(x))
x = x + 1
print(id(x))
y = x
print(id(y))
y += 1
print(id(y))

# object reusability
a = 10
b = 10
c = 10
print(id(a))
print(id(b))
print(id(c))

a = 10.33
b = 10.33
print(a is b)

a = True
b = True
print(a is b)

a = 'shubh'
b = 'shubh'
print(a is b)

# list - Mutable
L = [1, 2, 3, 4]
print(L)
print(id(L))
L[0] = 10
print(L)
print(id(L))
L2 = L
print(L2)
print(id(L2))
L[1] = 20
print(L)
print(L2)
print(L is L2)
L2[2] = 30
print(L)
print(L2)
print(L is L2)

# List Data Type
L = [10, 'shubh', 30, 40, 50, 60, 70]
print(L, type(L))
# index
print(L[0])
print(L[-1])
# Slice
print(L[1:4])
L = []
print(L)
L.append(10)
print(L)
L.append(20)
print(L)
L.append(30)
print(L)
L.append(40)
print(L)
L.remove(30)
print(L)
L[0] = 7777
print(L)