rollout CreateBox "Untitled" width:162 height:300
(
	editText edt1 "" pos:[21,37] width:101 height:29
	button btn1 "Create" pos:[28,93] width:93 height:29
	
	function MySwap &a &b =
	(
		t = a
		a = b
		b = t
	)
	
	function CreateBox1 n xoffset yoffset =
	(
		i = 1
		x = 0
		y = 0
		z = 0
		while i <= n do
		(
			t = box()
			t.width = 1
			t.height = 1
			t.length = 1
			t.pos = [x,y,z]
			x = x + xoffset
			y = y + yoffset
			
			i = i + 1
		)
	)
	
	on btn1 pressed do -- event handler
	(
		n = edt1.text as integer
		CreateBox1 n 1 1
	)
)

CreateDialog CreateBox