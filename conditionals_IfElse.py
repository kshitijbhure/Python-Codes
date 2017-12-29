

#IF-ELSE statements
print('1. IF-ELSE sample')
a,b=10,5
if a>b:
    print('a={} is greater than b={}'.format(a,b))
else:
    print('a={} is not greater than b={}'.format(a,b))


#Substitute and short code for the above code - CONDITIONAL EXPRESSION
print('2. CONDITIONAL EXPRESSION sample')
a,b=10,5
v = 'a is greater than b' if a>b else 'a is not greater than b'
print(v)

#multiple conditions IF-ELIF-ELSE
print('3. IF-ELIF-ELSE sample')
x='seven'
if x=='one':        #remember double '=' signs
    print('x is one')
elif x=='two':
    print('x is two')
elif x=='three':
    print('x is three')
else:
    print('x is something else')