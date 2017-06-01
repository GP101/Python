import math
import random

for letter in 'python':
    if letter == 'h':
        break
    print letter,

for letter in 'python':
    if letter == 'h':
        continue
    print letter,

for letter in 'python':
    if letter == 'h':
        pass
        print 'pass do nothing'
    print letter,

print
print math.ceil(4.7) #5.0
print math.floor(4.7) #4.0
print round( 4.76, 1 ) #4.8
print random.random()*5
print random.randrange(1,2)

l = [1,5,2,4,3]
random.shuffle(l)
print l
print math.cos( math.pi )

