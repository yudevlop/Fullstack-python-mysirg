a=5
b="5"
# print(a+b) # int + str = error
print(a+ int(b)) # int is a class but int() is a function which is used to type conversion
print(str(a) + str(b)) # str + str= no error


print(float(a)+float(b))
x=4
y=5.6
z=4j
print(x+y)
print(x+y+z) #number can be added whether it is int float or complex
#print(int(z)) # int() function can convert str into int only if contains only int neither float,str,complex
print(float(x))
print(int(y))
bool('abc')
print(bin(a))
s=0b1010
print(s)
h=345
print(chr(h))
d='$'
print(ord(d))

