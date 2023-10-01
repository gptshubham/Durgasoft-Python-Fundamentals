# float to int
print(int(10.989))
print(int(-10.989))

# complex to int
# print(int(10+20j))
# print(int((10+20j).real()))

# bool to int
print(int(True))
print(int(False))

# str to int (condition - str contains integral value with base 10)
print(int('10'))
# print(int('shubh'))
# print(int('10.33'))
# print(int('0b1111'))

# int to float
print(float(15))
print(float(0b1111))
print(float(0xface))

# complex to float
# print(float(10+20j))

# bool to float
print(float(True))
print(float(False))

# string to float (condition - string contains int or float value in base-10)
print(float('10'))
print(float('10.33'))
# print(float('0b1111'))
# print(float('shubh'))

# int to complex
print(complex(10))
print(complex(10,20))
print(complex(0b1111))
print(complex(0b1111,0b111))

# float to complex
print(complex(10.33))
print(complex(10.33,20.33))

# Bool to complex
print(complex(True))
print(complex(True,20))
print(complex(False))
print(complex(False,20))

# str to complex
# print(complex('10','20'))
print(complex('10'))
print(complex('10.33'))
# print(complex('shubh'))
# print(complex(10,'20'))
# print(complex('10',20))

# int to bool
print(bool(10))
print(bool(0))
print(bool(-10))

# float to bool
print(bool(0.0))
print(bool(0.00001))
print(bool(-0.00001))

# complex to bool
print(bool(0+0j))
print(bool(1+0j))
print(bool(0+0.001j))

# string to bool
print(bool('True'))
print(bool('False'))
print(bool('shubh'))
print(bool(' '))
print(bool(''))

# any other type to string
a = str(10)
print(a,type(a))
a = str(10.33)
print(a,type(a))
a = str(True)
print(a,type(a))
a = str(10+20j)
print(a,type(a))
a = str(0b1111)
print(a,type(a))
