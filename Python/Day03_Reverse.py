import sys

def Reverse( s ):
    begin = 0
    end = len(s)-1
    while begin < end:
        ch = s[begin]
        s[begin] = s[end]
        s[end] = ch
        begin += 1
        end -=1

s = 'hello'
t = list(s)
Reverse(t)
s = ''.join(t)
print s
