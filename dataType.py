#int type data
name = 123

print (type(name))
#float type data
name = 123.123

print (type(name))
#int type data
name = 123j

print (type(name))
#str type data
myname = "shovon"

print ("my name is "+myname)

#bool type data
x = 8
y = 7

print (x<y)

#binary type data

rafelist=[1,2,5,2,23,243,12]

b=bytes(rafelist)
print(type(b))

#binary type data

rafelist=[1,2,5,2,23,143,12]

b1=bytearray(rafelist)
b1[1]= 100
print(b1[1])
#none type value
x =None
print(type(x))