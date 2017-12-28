
#TUPLE is immutable
x=(1,2,3,4)     #tuple
print(type(x),x)

#LIST is mutable
x=[1,2,3,4]     #list
print(type(x),x)

#list elements can be changed
x.append(8)  #8 is added at the end
print(x)

x.insert(0,10)  #10 is inserted at the 0th position
print(x)
x.insert(2,11)  #11 is inserted at the 2nd position
print(x)

print('Printing list using for loop')
for i in x:
    print(i)


#STRING
x='string'
print(type(x),x)

print('second character : ' ,x[2]) #prints 2nd character in the string i.e. r
print('characters 2-5 : ',x[2:5])   #slices the string and prints characters from 2nd to 4th position. REMEMBER- it does not print the 5th character

print('Printing string using for loop')
for i in x:
    print(i)