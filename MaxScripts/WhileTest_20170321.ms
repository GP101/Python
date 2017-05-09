a = #(1,3,5)
i = 1
x = 0
s = 0
while i <= 3 do
(
	--print a[i]
	s = a[i]
	x = x + s
	
	t = box()
	t.height = 1
	t.width = 1
	t.length = 1
	t.pos = [x,0,0]
	t.scale = [s,1,1]

	
	
	i = i + 1
)