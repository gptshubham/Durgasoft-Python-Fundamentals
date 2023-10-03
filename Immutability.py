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

# Tuple Data Type
t = (10,20,30,10,'shubh')
print(type(t))
print(t[0])
print(t[1:4])
print(t[-1])
print(t[1:])
print(t[:3])
# t[0] = 7777
# t.append(50)
# t.remove(10)
t = ()
print(t,type(t))
t = (10)
print(t,type(t))  # what the hell
t = (10,)
print(t,type(t))

# Set Data Types
s1 = {1,2,3}
s2 = {2,3,1}
s3 = {3,2,1}
print(s1==s2==s3)
print(s1,type(s1))
s = {10,20,30,10,'shubham',40}
print(s)    # order duffers everytime I run this line .
# print(s[0])
# print(s[1:3])
s.add(50)
print(s)
s.remove(30)
print(s)
s = {}    # not an empty set but ____.
print(s,type(s))
s = set()   # empty set.
print(s,type(s))

# Frozen Set
s = {10,20,30,40}
fs = frozenset(s)
print(fs)
print(type(fs))
# fs.add(50)
# fs.remove(20)

# Dict
d = {100:'shubham',200:'kumar',300:'gupta'}
print(d)
print(type(d))
d = {}
print(type(d))
d[400]='skg007'
print(d)
d[100]='shubham'
print((d))
d[200]='kumar'
print(d)
d[300]='gupta'
print(d)
# value update in dictionary
d[100]='abhishek'
print(d)