import os

pathes = os.environ['path']
#print type( pathes )

dir = ''
for char in pathes:
    dir = dir + char
    if char == ';':
        print dir
        dir = ''
