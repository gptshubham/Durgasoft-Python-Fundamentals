# index
s = 'shubham'
print(s[0])
print(s[3])
# print(s[100])
print(s[-1])
# print(s[-10])
print(s[-7])

# slice
s = "shubhamkumargupta"
print(s[7:12])
print(s[:7])
print(s[12:])
print(s[:])
print(s[3:100])
print(s[5:1])
print('empty string above')

# slice operator application
s = 'gupta'
print(s)
s = s[0].upper() + s[1:]
print(s)

s = 'gupta'
print(s)
s = s[:len(s)-1] + s[-1].upper()
print(s)

s = 'gupta'
print(s)
s = s[0].upper() + s[1:len(s)-1] + s[-1].upper()
print(s)

# + operator
print('shubh' + 'am')
# print('shubh' + 10)
print('shubh' + '10')

# * operator
print('shubh' * 3)
# print('shubh' * '3')
# print('shubh' * 3.3)
print(3 * 'shubh')
print('#' * 9)
print(' shubham')
print('#' * 9)
print('shubh' * False)
print('shubh' * True)
