rollout ViewFbx "View Fbx"
(
	button          btnView "View Fbx File"
	
	on btnView pressed do
	(
		local filename = "temp.fbx"

		local destpath = getdir( #export )
		local fullpath = destpath + "\\" + filename
		local exportAndLaunch = true
		if DoesFileExist( fullpath ) then
		(
			exportAndLaunch = QueryBox( fullpath + "\nexists. Overwrite?")
		)
		if exportAndLaunch then
		(
			exportfile filename #noPrompt
			shellLaunch fullpath ""
		)
	)
)

CreateDialog ViewFbx