rollout unnamedRollout "Untitled" width:162 height:300
(
	button btn1 "Add Unwrap Uvw" pos:[20,19] width:118 height:36
    
    on btn1 pressed do
    (
        if selection.count == 1 then
        (
            setCommandPanelTaskMode #modify
            uvwmod = Unwrap_UVW()
            addModifier $ uvwmod
            uvwmod.edit()
        )
    )
)

CreateDialog unnamedRollout