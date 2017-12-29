
#Index in a string

s='this is a string'

for i,c in enumerate(s):        #prints the index for each character
    print(i, c)

#finding position of character
print('Finding position of s')
for i,c in enumerate(s):
    if c == 's':
        print('index {} is an s'.format(i))