

try:
    fh = open('xlines.txt')         #file name is wrong
    for line in fh.readlines():
        print(line)

except IOError as e:
    print('Some error occurred. The error is {}'.format(e))

except:
    print('Some error occurred which is not an IO error.')


print('after the error')
