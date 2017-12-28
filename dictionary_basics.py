
#DICTIONARY
#dictionary is mutable(can be modified)
#dictionary has a key value pair

d={'one':1,'two':2,'three':3,'four':4}      #one,two etc are keys. 1,2,3 etc are values

#print entire dictionary. the order of the elements can be anything
print(d)

#Dictionary objects are MUTABLE
d['seven']=7

#traverse the dictionary and print
for k in d:
    print(k,d[k])       #k stores the key and d[k] : its value

#sort the dictionary and display
print('sorted dictionary')
for k in sorted(d.keys()):  #sorts alphabetically
    print(k,d[k])

#Another way to define a dictionary
e=dict(
    one=1,two=2,three=3,four=4,five=5
)

print('dictionary e',e)

#Dictionary can accept any type of data
f=dict(
    one=1,two=2,three=3,four=4,five='five'
)
print('dictionary f',f)
