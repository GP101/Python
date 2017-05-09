function MySwap &x &y = 
(
	t = x
	x = y
	y = t
)
x = 1
y = 3
MySwap &x &y
print "hello" + x as string
print "world" + y as string