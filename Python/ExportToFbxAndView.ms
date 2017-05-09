rollout ViewFbx "View Fbx"
(
	button          btnView "View Fbx File"
	
	on btnView pressed do
	(
		filename = "temp.fbx"

		destpath = getdir( #export )
		fullpath = destpath + "\\" + filename
		exportfile filename #noPrompt
		shellLaunch fullpath ""
	)
)

CreateDialog ViewFbx