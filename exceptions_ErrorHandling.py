#!/usr/bin/python3
# exceptions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC


try:
    fh = open('xlines.txt')         #file name is wrong
    for line in fh.readlines():
        print(line)

except IOError as e:
    print('Some error occurred. The error is {}'.format(e))

except:
    print('Some erorr occurred which is not an IO error.')


print('after the error')