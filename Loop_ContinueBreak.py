


s='this is a string'

#CONTINUE
for c in s:
    if c == 's': continue   #skips the iteration if c=s
    print(c, end='')

print('')       #blank line

#BREAK
for c in s:
    if c == 's': break  #if s is found it breaks the loop
    print(c, end='')