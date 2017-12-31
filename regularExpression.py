
# Regular expression sample

import re   # import re for regular expression


f = open('regexFile.txt')

# prints all the lines that have Lenore or Nevermore - SEARCH keyword
for line in f:
    if re.search('(Len|Neverm)ore', line):
        print(line, end='')

print('\n\n End of first part \n')

# Search and replace - SUB keyword
p = open('regexFile.txt')
for line in p:
    print (re.sub('(Len|Neverm)ore', '###', line),end='')

print('\n\n End of second part \n')

#Reusing the regular expression
q = open('regexFile.txt')
pattern = re.compile('(Len|Neverm)ore', re.IGNORECASE)         # store the pattern in a variable and use it later, IGNORECASE used to ignore the case sensitive characters
# 'search' and 'substitute' both used in single code. this will display only the lines which has the pattern
for line in q:
    if re.search(pattern, line):
        print(pattern.sub('###',line),end='')



