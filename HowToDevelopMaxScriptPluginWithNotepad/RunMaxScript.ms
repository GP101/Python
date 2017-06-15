rollout RunMaxScript "Run MaxScript" width:400
(
	editText pythonFile ""
	button runPythonFileButton "Run MaxScript..."
    
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
	
    on runPythonFileButton pressed do
    (
		fileIn( pythonFile.text )
        redrawViews()
    )
)

CreateDialog RunMaxScript