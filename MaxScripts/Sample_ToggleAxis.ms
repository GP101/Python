rollout unnamedRollout "Untitled" width:162 height:300
(
    button btnHello "Hello" pos:[21,24] width:111 height:24
    
    on btnHello pressed Do
    (
        varAxis = getRefCoordSys()

        if varAxis == #World or varAxis == #Hybrid then
            (toolMode.coordsys #Local)
        else if varAxis == #Local then
            (toolMode.coordsys #View)
    )
)

CreateDialog unnamedRollout