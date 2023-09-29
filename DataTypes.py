"""
# int
# Decimal
a = 1111
print(a)
# Binary
x = 0b1111
print(x)
y = 0B1111
print(y)
# Octal
print(0o123)
# print(0o786)
print(0x10)
# Hexadecimal
print(0xFACE)

# Bace Conversion
print(bin(15))
print(0o123)
print(bin(0xface))

print(oct(100))
print(oct(0b111101))
print(0XFace)

print(hex(1000))
print(hex(0b10111111))
print(hex(0o123456))

# Float
f = 1.2e3
print(f)
f1 = 1.2e16
print(f1)

# Complex
x = 10+20j
print(type(x))
x1 = 10+20J
print(type(x1))
print(x.real)
print(x.imag)
x = 10.5+20.6j
print(x)
x = 0b1111+20j
print(x)
# x = 10+0b1111j
# print(x)
x = 10+20j
y = 20+20j
print(x+y)
print(x-y)
print(x*y)
print(x/y)

# Boolean
b = True
print(type(b))
# b = true
# print(type(b))
c = False
print(type(c))
print(b)
print(c)
print(c>b)
print(b>c)
print(True+True)
print(True-False)
print(True*False)
"""
# string
s = 'shubham'
print(s,type(s))
s = "shubham"
print(s,type(s))
s = 's'
print(s,type(s))
s = '''shubham
kumar
gupta'''
print(s,type(s))
s = """shubham
kumar
gupta"""
print(s,type(s))
s = "class by 'Durga' is very good."
print(s)
s = 'class by "Durga" is very good.'
print(s)
s = '''classes by 'Durga' for "Python" are very good.'''
print(s)
s = """classes by 'Durga' for "Python" are very good."""
print(s)