rollout MakeTriangle "MakeTriangle" width:200 height:300
(
	editText countText "" pos:[23,29] width:136 height:23
	button createButton "Create" pos:[22,85] width:138 height:28
    
	function CreateBox x y z n =
	(
		local i = 1
		while i <= n do 
		(
			local j = 1
			while j <= n do
			(
				local b = box()
				b.width = 1
				b.height = 1
				b.length = 1
				b.pos = [x+i,y+j,z]
				j = j + 1
			)
			i = i + 1
		)
	)
	
    on createButton pressed do
    (
		local x = 0
		local y = 0
		local z = 0
        local i = 1
		local count = countText.text as integer
		local n = count
        while i <= count do
        (
			createBox (x+i) (y+i) (z+i) n
            n = n - 2
			i = i + 1
        )
    )
)
CreateDialog MakeTriangle