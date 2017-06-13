/** @brief  Invalid Face Breaker
    @date   jintaeks on 오후 4:03 2013-11-27 */

macroScript InvalidFaceBreaker
            category:"Dsu"
            Icon:#("Patches",3)
(
    ----------------------------------------------------------------------------------------------------
    -- method. seojtdoc. jintaeks on 오후 2:43 2013-11-19 qff
    local m_filename = "$temp\\DsuInvalidFaceBreaker4.cfg"
    local m_file
    local m_bIsCancelProcess = false -- jintaeks on 오후 7:49 2013-11-25

    ----------------------------------------------------------------------------------------------------
    -- helper functions

    ----------------------------------------------------------------------------------------------------
    function IsEqual a_ b_ =
    (
        if a_ - b_ > 0.0001 or a_ - b_ < -0.0001 then
            return false
        else
            return true
    )--function IsEqual a_ b_

    ----------------------------------------------------------------------------------------------------
    function BreakFaceMain bIsAutoBreak_ progressBar_ =
    (
        if selection.count == 1 then
        (
            -- get material info of selected object.
            local base_obj = $.baseobject
            local real_obj = selection[1]
            local map_channel = 1
            local obj = real_obj
            
            -- this is a workaround for max 9, because collapseNodeTo is buggy
            -- local obj = editable_mesh()
            -- obj.baseobject = copy real_obj.baseobject
            -- local save_obj = real_obj.baseobject
            -- hide real_obj
            -- convertTo obj PolyMeshObject
            
            setCommandPanelTaskMode #modify
            
            local facecount = obj.faces.count
            
            format "Analyzing and manipulating % ...\n" real_obj.name
            format "- % has % faces\n" real_obj.name facecount
            
            select real_obj
            uvwmod = Unwrap_UVW()
            addModifier real_obj uvwmod
            uvwmod.setMapChannel map_channel
            uvwmod.updateView()
            uvwmod.setResetPivotOnSelection false
            uvwmod.setTVSubObjectMode 3
            uvwmod.edit()

            --local polycount = uvwmod.numberPolygons()
            local errorFaces = #{}
            errorFaces[facecount] = False
            local numErrorFaces = 0
            
            --format "- polycount = %\n" polycount

            local iProgressUpdateStep = facecount / 100
            local iProgressUpdateCounter = 0
            
            local x, y, width, height, areaUvw, areaGeom
            for f = 1 to facecount do
            (
                areaUvw = 0
                uvwmod.getArea #{f} &x &y &width &height &areaUvw &areaGeom
                if( IsEqual areaUvw 0 ) then
                (
                    format "- error face = %\n" f
                    format "- x = %, y = %, width = %, height = %, areaUvw = %, areaGeom = %\n" x y width height areaUvw areaGeom
                    errorFaces[f] = true
                    numErrorFaces += 1
                )--if
                
                -- update progress bar. jintaeks on 오전 11:27 2013-11-14
                iProgressUpdateCounter += 1
                if iProgressUpdateCounter >= iProgressUpdateStep then
                (
                    iProgressUpdateCounter = 0
                    progressBar_.value = ( f as float / facecount ) * 100
                    windows.processPostedMessages()
                )--if
            )--for
            
            local ss = stringStream ""
            local strMsg
            if numErrorFaces >= 1 then
            (
                format "- breaking error faces\n"
                uvwmod.selectFaces errorFaces
                
                if bIsAutoBreak_ then
                (
                    uvwmod.breakSelected()
                    convertTo obj PolyMeshObject
                    format "breaked % faces" numErrorFaces to:ss
                )
                else
                (
                    format "selected % faces" numErrorFaces to:ss
                )--if.. else..
                
                -- real_obj.baseobject = obj.baseobject
                -- for geo in geometry do if geo.baseobject == save_obj then geo.baseobject = obj.baseobject
                -- unhide real_obj
                -- select real_obj
                
                strMsg = ( ss as string )
            )
            else
            (
                deleteModifier obj uvwmod
                strMsg = "No error face(s)"
            )--if.. else..
            
            format ( strMsg + "\n" )
            messageBox ( strMsg as string )
            
            progressBar_.value = 0
        )--if
    )--function BreakFaceMain

    ----------------------------------------------------------------------------------------------------
    function SliceFaceMain iSliceCheckWidth_ progressBar_ =
    (
        if selection.count == 1 then
        (
            local base_obj = $.baseobject
            local real_obj = selection[1]
            local map_channel = 1
            local obj = real_obj
            
            -- this is a workaround for max 9, because collapseNodeTo is buggy
            -- local obj = editable_mesh()
            -- obj.baseobject = copy real_obj.baseobject
            -- local save_obj = real_obj.baseobject
            -- hide real_obj
            -- convertTo obj PolyMeshObject
            
            setCommandPanelTaskMode #modify
            
            local facecount = obj.faces.count
            
            format "Analyzing and manipulating % ...\n" real_obj.name
            format "- % has % faces\n" real_obj.name facecount
            
            select real_obj
            uvwmod = Unwrap_UVW()
            addModifier real_obj uvwmod
            uvwmod.setMapChannel map_channel
            uvwmod.updateView()
            uvwmod.setResetPivotOnSelection false
            uvwmod.setTVSubObjectMode 3
            uvwmod.edit()

            --local polycount = uvwmod.numberPolygons()
            local errorFaces = #{}
            errorFaces[facecount] = False
            local numErrorFaces = 0
            
            --format "- polycount = %\n" polycount

            local iProgressUpdateStep = facecount / 100
            local iProgressUpdateCounter = 0
            
            local x, y, width, height, areaUvw, areaGeom
            for f = 1 to facecount do
            (
                areaUvw = 0
                uvwmod.getArea #{f} &x &y &width &height &areaUvw &areaGeom
                if width >= iSliceCheckWidth_ or height >= iSliceCheckWidth_ then
                (
                    format "- slice face = %\n" f
                    format "- x = %, y = %, width = %, height = %, areaUvw = %, areaGeom = %\n" x y width height areaUvw areaGeom
                    errorFaces[f] = true
                    numErrorFaces += 1
                )--if
                
                -- update progress bar. jintaeks on 오전 11:27 2013-11-14
                iProgressUpdateCounter += 1
                if iProgressUpdateCounter >= iProgressUpdateStep then
                (
                    iProgressUpdateCounter = 0
                    progressBar_.value = ( f as float / facecount ) * 100
                    windows.processPostedMessages()
                )--if
            )--for
            
            local ss = stringStream ""
            local strMsg
            if numErrorFaces >= 1 then
            (
                -- format "- slice error faces\n"
                uvwmod.selectFaces errorFaces
                
                -- if bIsAutoBreak_ then
                -- (
                    -- uvwmod.breakSelected()
                    -- convertTo obj PolyMeshObject
                    -- format "breaked % faces" numErrorFaces to:ss
                -- )
                -- else
                (
                    format "selected % faces" numErrorFaces to:ss
                )--if.. else..
                
                -- real_obj.baseobject = obj.baseobject
                -- for geo in geometry do if geo.baseobject == save_obj then geo.baseobject = obj.baseobject
                -- unhide real_obj
                -- select real_obj
                
                strMsg = ( ss as string )
            )
            else
            (
                deleteModifier obj uvwmod
                strMsg = "No slice face(s)"
            )--if.. else..
            
            format ( strMsg + "\n" )
            messageBox ( strMsg as string )
            
            progressBar_.value = 0
        )--if
    )--function SliceFaceMain

    ----------------------------------------------------------------------------------------------------
    function IsValidFace obj_ faceIndex_ =
    (
        -- if (classOf obj_) == Editable_Poly then
        -- (
            -- local faceNormal = (polyop.getFaceNormal obj_ faceIndex_)
        -- )
        -- else
        -- (
            -- return false
        -- )--if.. else..
    )--tag_getEdgeVerts()

    ----------------------------------------------------------------------------------------------------
    function __min a b =
    (
        if a < b then a else b
    )--function __min a b

    ----------------------------------------------------------------------------------------------------
    function __max a b =
    (
        if a > b then a else b
    )--function __max a b

    ----------------------------------------------------------------------------------------------------
    /** @brief  get scalar component of cross product
        @note   we do not use .z compoennt */
    function CrossProductSign x1 y1 x2 y2 =
    (
        return x1 * y2 - x2 * y1
    )--function CrossProductSign x1 y1 x2 y2 =


    ----------------------------------------------------------------------------------------------------
    /** @brief  check whether bounding rectangles of two line segment is intersecting or not
        @param  (p1, p2) first line segment
                (p3, p4) second line segment
        @return true when bounding rectangles of line segment are intersecting
        @date   jintaeks on 오전 11:31 2013-12-02 */
    function ProjQuickIsBoundingRectangleIntersect p1 p2 p3 p4 =
    (
        local x1, z1, x2, z2, x3, z3, x4, z4

        x1 = __min p1.x p2.x
        z1 = __min p1.y p2.y
        x2 = __max p1.x p2.x
        z2 = __max p1.y p2.y

        x3 = __min p3.x p4.x
        z3 = __min p3.y p4.y
        x4 = __max p3.x p4.x
        z4 = __max p3.y p4.y

        return ( x2 >= x3 ) and ( x4 >= x1 ) and ( z2 >= z3 ) and ( z4 >= z1 )
    )--function ProjQuickIsBoundingRectangleIntersect p1 p2 p3 p4


    ----------------------------------------------------------------------------------------------------
    /** @brief  get scalar component of cross product
        @note   we do not use .z component
        @date   jintaeks on 오전 11:34 2013-12-02 */
    function ProjCrossProduct v1 v2 =
    (
        return CrossProductSign v1.x v1.y v2.x v2.y
    )--function ProjCrossProduct v1 v2 =


    ----------------------------------------------------------------------------------------------------
    -- @brief   get difference vector, v1 - v2
    function ProjDifference v1 v2 =
    (
        local v = [ 0, 0, 0 ] as point3

        v.x = v1.x - v2.x
        v.y = v1.y - v2.y
        v.z = v1.z - v2.z
        return v
    )--function ProjDifference v1 v2 =


    ----------------------------------------------------------------------------------------------------
    /** @brief  check whether two line segments are intersecting or not
        @param  (p1, p2) first line segment
                (p3, p4) second line segment
        @date   jintaeks on 오전 11:29 2013-12-02 */
    function ProjIsIntersect p1 p2 p3 p4 =
    (
        if not ProjQuickIsBoundingRectangleIntersect p1 p2 p3 p4 then
        (
            return false
        )--if

        local i  = ProjCrossProduct ( ProjDifference p3 p1 ) ( ProjDifference p2 p1 )
        local j  = ProjCrossProduct ( ProjDifference p4 p1 ) ( ProjDifference p2 p1 )
        local i2 = ProjCrossProduct ( ProjDifference p1 p3 ) ( ProjDifference p4 p3 )
        local j2 = ProjCrossProduct ( ProjDifference p2 p3 ) ( ProjDifference p4 p3 )

        local ret  = if (i < 0 and j > 0) or (i > 0 and j < 0) then true else false
        local ret2 = if (i2 < 0 and j2 > 0) or (i2 > 0 and j2 < 0) then true else false

        return ret and ret2
    )--function ProjIsIntersect p1 p2 p3 p4 =


    ----------------------------------------------------------------------------------------------------
    /** @brief  check whether line segment (v1_, v2_ ) is intersecting
                with (vertices_[iBeginIndex_], vertices_[iBeginIndex_+1])
        @date   jintaeks on 오전 11:20 2013-12-02 */
    function IsEdgeIntersect vertices_ iBeginIndex_ numVertices_ v1_ v2_ =
    (
        for i = iBeginIndex_ to numVertices_ - 1 Do
        (
            if ProjIsIntersect vertices_[i] vertices_[i+1] v1_ v2_ then
            (
                return true
            )--if
        )--for
        
        return false
    )--function IsEdgeIntersect vertices_ numVertices_ v1_ v2_


    ----------------------------------------------------------------------------------------------------
    /** @function   FlattenFaceMain
        @brief      flatten wrong side faces
        @date       jintaeks on 오전 11:22 2013-11-28 */
    function FlattenFaceMain bIsAutoFlatten_ progressBar_ =
    (
        if selection.count == 1 then
        (
            -- get material info of selected object.
            local base_obj = $.baseobject
            local real_obj = selection[1]
            local map_channel = 1
            local obj = real_obj
            
            -- this is a workaround for max 9, because collapseNodeTo is buggy
            -- local obj = editable_mesh()
            -- obj.baseobject = copy real_obj.baseobject
            -- local save_obj = real_obj.baseobject
            -- hide real_obj
            -- convertTo obj PolyMeshObject
            
            setCommandPanelTaskMode #modify
            
            local facecount = obj.faces.count
            
            format "Analyzing and manipulating % ...\n" real_obj.name
            format "- % has % faces\n" real_obj.name facecount
            
            select real_obj
            uvwmod = Unwrap_UVW()
            addModifier real_obj uvwmod
            uvwmod.setMapChannel map_channel
            uvwmod.updateView()
            uvwmod.setResetPivotOnSelection false
            uvwmod.setTVSubObjectMode 3
            uvwmod.edit()

            --local polycount = uvwmod.numberPolygons()
            local errorFaces = #{}
            errorFaces[facecount] = False
            local numErrorFaces = 0
            
            --format "- polycount = %\n" polycount

            local iProgressUpdateStep = facecount / 100
            local iProgressUpdateCounter = 0
            
            local x, y, width, height, areaUvw, areaGeom
            for f = 1 to facecount do
            (
                uvwmod.selectFaces #{f}
                uvwmod.faceToVertSelect()
                local vertIndices = ( uvwmod.getSelectedVertices() ) as Array
                local numIndices = vertIndices.count
                local vertices = #()
                
                for vindex in vertIndices Do
                (
                    vertTemp = (uvwmod.getVertexPosition 0 vindex)
                    append vertices vertTemp
                    -- uvwmod.setVertexPosition 0 vindex vertTemp
                )--for
            
                local bIsValidFace = true
                local bIsIntersect = false
                for viOuter = 3 to numIndices - 1 do
                (
                    bIsIntersect = IsEdgeIntersect vertices 1 ( viOuter - 1 ) vertices[viOuter] vertices[viOuter+1]
                    --format "bIsIntersect = % %\n" bIsIntersect viOuter
                    if bIsIntersect then
                    (
                        format "bIsIntersect = % %\n" bIsIntersect viOuter
                        bIsValidFace = false
                        break
                    )--if
                )--for
                if bIsValidFace then
                (
                    bIsIntersect = IsEdgeIntersect vertices 2 ( numIndices - 2 ) vertices[numIndices] vertices[1]
                    --format "bIsIntersect = % final\n" bIsIntersect
                    if bIsIntersect then
                    (
                        format "bIsIntersect = % final\n" bIsIntersect
                        bIsValidFace = false
                    )--if
                )--if
                
                if not bIsValidFace then
                (
                    errorFaces[f] = true
                    numErrorFaces += 1
                    format "- error face = %\n" f
                )--if
                
                -- update progress bar. jintaeks on 오전 11:27 2013-11-14
                iProgressUpdateCounter += 1
                if iProgressUpdateCounter >= iProgressUpdateStep then
                (
                    iProgressUpdateCounter = 0
                    progressBar_.value = ( f as float / facecount ) * 100
                    windows.processPostedMessages()
                )--if
            )--for
            
            local ss = stringStream ""
            local strMsg
            if numErrorFaces >= 1 then
            (
                format "- flatten error faces\n"
                uvwmod.selectFaces errorFaces
                
                if bIsAutoFlatten_ then
                (
                    -- qff. needs parameter settings box. jintaeks on 오후 9:02 2013-11-28
                    uvwmod.flattenMap 45 #() 0.02 true 0 true true
                    convertTo obj PolyMeshObject
                    format "flattened % faces" numErrorFaces to:ss
                )
                else
                (
                    format "selected % faces" numErrorFaces to:ss
                )--if.. else..
                
                -- real_obj.baseobject = obj.baseobject
                -- for geo in geometry do if geo.baseobject == save_obj then geo.baseobject = obj.baseobject
                -- unhide real_obj
                -- select real_obj
                
                strMsg = ( ss as string )
            )
            else
            (
                deleteModifier obj uvwmod
                strMsg = "No error face(s)"
            )--if.. else..
            
            format ( strMsg + "\n" )
            messageBox ( strMsg as string )
            
            progressBar_.value = 0
        )--if
    )--function FlattenFaceMain
    
    ----------------------------------------------------------------------------------------------------
    /** @brief  find string value in an Array
        @param  arrFAces_ : Array
        @param  strEdgeInfo_ : string value
        @date   jintaeks on 오전 9:35 2013-12-03 */
    function FindArrayValue &arrFaces_ strEdgeInfo_ =
    (
        local iCount = arrFaces_.count as integer
        -- format "debug : FindArrayValue % items\n" iCount
        
        for i = 1 to iCount do
        (
            -- format "debug : compare % % %\n" i strEdgeInfo_ arrFaces_[i]
            if stricmp strEdgeInfo_ arrFaces_[i] == 0 do return i
        )--for
        
        return 0
    )--function FindArrayValue arrFaces_ strEdgeInfo_ =

    ----------------------------------------------------------------------------------------------------
    /** @function   BreakSameUvwFaceMain
        @brief      unweld wrong faces
        @date       jintaeks on 오후 5:45 2013-12-02 */
    function BreakSameUvwFaceMain bIsAutoUnweld_ progressBar_ =
    (
        if selection.count == 1 then
        (
            -- get material info of selected object.
            local base_obj = $.baseobject
            local real_obj = selection[1]
            local map_channel = 1
            local obj = real_obj
            
            -- this is a workaround for max 9, because collapseNodeTo is buggy
            -- local obj = editable_mesh()
            -- obj.baseobject = copy real_obj.baseobject
            -- local save_obj = real_obj.baseobject
            -- hide real_obj
            -- convertTo obj PolyMeshObject
            
            setCommandPanelTaskMode #modify
            
            local facecount = obj.faces.count
            
            format "Analyzing and manipulating % ...\n" real_obj.name
            format "- % has % faces\n" real_obj.name facecount
            
            select real_obj
            uvwmod = Unwrap_UVW()
            addModifier real_obj uvwmod
            uvwmod.setMapChannel map_channel
            uvwmod.updateView()
            uvwmod.setResetPivotOnSelection false
            uvwmod.setTVSubObjectMode 3
            uvwmod.edit()

            --local polycount = uvwmod.numberPolygons()
            local errorFaces = #{}
            errorFaces[facecount] = False
            local numErrorFaces = 0
            
            --format "- polycount = %\n" polycount

            local iProgressUpdateStep = facecount / 100
            local iProgressUpdateCounter = 0
            
            local x, y, width, height, areaUvw, areaGeom
            local arrFaces = #()

            for f = 1 to facecount do
            (
                -- format "face = %\n" f
                uvwmod.selectFaces #{f}
                uvwmod.faceToEdgeSelect()
                local edgeIndices = ( uvwmod.getSelectedEdges() ) as Array
                local numEdges = edgeIndices.count
               
                local strEdgeInfo = "edge"
                for vindex in edgeIndices Do
                (
                    strEdgeInfo = strEdgeInfo + ","
                    strEdgeInfo = strEdgeInfo + ( vindex as string )
                )--for
                -- format "debug : strUvwEdgeInfo = %\n" strEdgeInfo
                local bIsFaceExist = false
                iFace = FindArrayValue &arrFaces strEdgeInfo
                if iFace == 0 then
                (
                    -- format "debug : add new face %\n" f
                    append arrFaces strEdgeInfo
                    bIsFaceExist = false
                )
                else
                (
                    -- format "debug : face % already exist\n" f
                    bIsFaceExist = true
                )--if.. else..
                
                if bIsFaceExist then
                (
                    errorFaces[f] = true
                    numErrorFaces += 1
                )--if
                
                -- update progress bar. jintaeks on 오전 11:27 2013-11-14
                iProgressUpdateCounter += 1
                if iProgressUpdateCounter >= iProgressUpdateStep then
                (
                    iProgressUpdateCounter = 0
                    progressBar_.value = ( f as float / facecount ) * 100
                    windows.processPostedMessages()
                )--if
            )--for
            
            local ss = stringStream ""
            local strMsg
            if numErrorFaces >= 1 then
            (
                --format "- flatten error faces\n"
                uvwmod.selectFaces errorFaces
                
                if bIsAutoUnweld_ then
                (
                    uvwmod.breakSelected()
                    convertTo obj PolyMeshObject
                    format "breaked % faces" numErrorFaces to:ss
                )
                else
                (
                    format "selected % faces" numErrorFaces to:ss
                )--if.. else..
                
                -- real_obj.baseobject = obj.baseobject
                -- for geo in geometry do if geo.baseobject == save_obj then geo.baseobject = obj.baseobject
                -- unhide real_obj
                -- select real_obj
                
                strMsg = ( ss as string )
            )
            else
            (
                deleteModifier obj uvwmod
                strMsg = "No error face(s)"
            )--if.. else..
            
            format ( strMsg + "\n" )
            messageBox ( strMsg as string )
            
            progressBar_.value = 0
        )--if
    )--function BreakSameUvwFaceMain

    ----------------------------------------------------------------------------------------------------
    /** @brief  get matching edge counter
        @param  arrEdgeTarget_ : target edge index list
        @param  arrEdgeToFind_ : source edge index list
        @date   jintaeks on 오전 10:14 2013-12-04 */
    function FindMatchingAndGetCount arrEdgeTarget_ arrEdgeToFind_ =
    (
        local iMatchCounter = 0
        for i = 1 to arrEdgeTarget_.count do
        (
            for j = 1 to arrEdgeToFind_.count do
            (
                if arrEdgeTarget_[i] == arrEdgeToFind_[j] then
                (
                    iMatchCounter += 1
                )--if
            )--for
        )--for
        
        return iMatchCounter
    )--function FindMatchingAndGetCount arrEdgeTarget_ arrEdgeToFind_ =

    ----------------------------------------------------------------------------------------------------
    /** @brief  find partial matching face from an array of face edge array
        @param  arrarrFaceEdges_ : array of edge array
        @param  arrEdges_ : target face edge Array
        @date   jintaeks on 오전 10:49 2013-12-03 */
    function FindPartialMatchingFace arrarrFaceEdges_ arrEdges_ iSkipIndex_ =
    (
        for findex = iSkipIndex_ + 1 to arrarrFaceEdges_.count do
        (
            if findex == iSkipIndex_ do continue
            
            local arrEdges = arrarrFaceEdges_[findex] as array
            local iMatchCounter = FindMatchingAndGetCount ( arrEdges as array ) ( arrEdges_ as array )
            if iMatchCounter >= 1 then
            (
                return findex
            )--if
        )--for
        
        return 0
    )--function FindPartialMatchingFace arrarrFaceEdges_ arrEdges_ =


    ----------------------------------------------------------------------------------------------------
    function BreakMismatchingPolyUvwFaceMain bIsAutoBreak_ progressBar_ =
    (
        if selection.count == 1 then
        (
            -- get material info of selected object.
            local base_obj = $.baseobject
            local real_obj = selection[1]
            local map_channel = 1
            local obj = real_obj
            
            -- this is a workaround for max 9, because collapseNodeTo is buggy
            -- local obj = editable_mesh()
            -- obj.baseobject = copy real_obj.baseobject
            -- local save_obj = real_obj.baseobject
            -- hide real_obj
            -- convertTo obj PolyMeshObject
            
            setCommandPanelTaskMode #modify
            
            local facecount = obj.faces.count
            
            format "Analyzing and manipulating % ...\n" real_obj.name
            format "- % has % faces\n" real_obj.name facecount
            
            select real_obj
            uvwmod = Unwrap_UVW()
            addModifier real_obj uvwmod
            uvwmod.setMapChannel map_channel
            uvwmod.updateView()
            uvwmod.setResetPivotOnSelection false
            uvwmod.setTVSubObjectMode 3
            uvwmod.edit()

            --local polycount = uvwmod.numberPolygons()
            local errorFaces = #{}
            errorFaces[facecount] = False
            local numErrorFaces = 0
            
            --format "- polycount = %\n" polycount

            local iProgressUpdateStep = facecount / 100
            local iProgressUpdateCounter = 0
            
            local x, y, width, height, areaUvw, areaGeom
            local arrPolyFaceEdges = #( #() )
            arrPolyFaceEdges[facecount] = #()
            local arrUvwFaceEdges = #( #() )
            arrUvwFaceEdges[facecount] = #()

            /** construct Poly face edge info
                construct Uvw face edge info
                - jintaeks on 오전 11:03 2013-12-03 */
            for f = 1 to facecount do
            (
                -- format "debug : face = %\n" f
                uvwmod.selectFaces #{f}
                local arrFaceEdges = (polyop.getFaceEdges obj f) as array
                arrPolyFaceEdges[f] = arrFaceEdges
                
                uvwmod.faceToEdgeSelect()
                local edgeIndices = ( uvwmod.getSelectedEdges() ) as Array
                arrUvwFaceEdges[f] = edgeIndices
                
                local bIsFaceExist = false
                if bIsFaceExist then
                (
                    errorFaces[f] = true
                    numErrorFaces += 1
                )--if
                
                -- update progress bar. jintaeks on 오전 11:27 2013-11-14
                iProgressUpdateCounter += 1
                if iProgressUpdateCounter >= iProgressUpdateStep then
                (
                    iProgressUpdateCounter = 0
                    progressBar_.value = ( f as float / facecount ) * 100
                    windows.processPostedMessages()
                )--if
            )--for

            /**
            format "Poly faces\n"
            for findex = 1 to arrPolyFaceEdges.count Do
            (
                format "debug : findex = %\n" findex
                local arrEdges = arrPolyFaceEdges[findex] as array
                for eindex = 1 to arrEdges.count do
                (
                    format "eindex = %\n" arrEdges[eindex]
                )--for
            )--for

            format "Uvw faces\n"
            for findex = 1 to arrUvwFaceEdges.count Do
            (
                format "debug : findex = %\n" findex
                local arrEdges = arrUvwFaceEdges[findex] as array
                for eindex = 1 to arrEdges.count do
                (
                    format "eindex = %\n" arrEdges[eindex]
                )--for
            )--for
            */
            
            -- check partial matching faces.
            iProgressUpdateCounter = 0
            for f = 1 to arrUvwFaceEdges.count Do
            (
                local arrEdges = arrUvwFaceEdges[f] as array
                local iMatchingFace = FindPartialMatchingFace arrUvwFaceEdges arrEdges f
                -- when there exist partial matching face in Uvw faces
                if iMatchingFace != 0 then
                (
                    -- check there also exist partial matching face in Poly face
                    local iMatchingFace2 = FindPartialMatchingFace arrPolyFaceEdges arrPolyFaceEdges[f] f
                    -- error face if partial matching Uvw face and Poly face is different.
                    -- jintaeks on 오전 11:05 2013-12-03
                    if iMatchingFace != iMatchingFace2 then
                    (
                        errorFaces[f] = true
                        numErrorFaces += 1
                    )--if
                )--if
                
                -- update progress bar. jintaeks on 오전 11:27 2013-11-14
                iProgressUpdateCounter += 1
                if iProgressUpdateCounter >= iProgressUpdateStep then
                (
                    iProgressUpdateCounter = 0
                    progressBar_.value = ( f as float / facecount ) * 100
                    windows.processPostedMessages()
                )--if
            )--for
            
            local ss = stringStream ""
            local strMsg
            if numErrorFaces >= 1 then
            (
                --format "- flatten error faces\n"
                uvwmod.selectFaces errorFaces
                
                if bIsAutoBreak_ then
                (
                    uvwmod.breakSelected()
                    convertTo obj PolyMeshObject
                    format "breaked % faces" numErrorFaces to:ss
                )
                else
                (
                    format "selected % faces" numErrorFaces to:ss
                )--if.. else..
                
                -- real_obj.baseobject = obj.baseobject
                -- for geo in geometry do if geo.baseobject == save_obj then geo.baseobject = obj.baseobject
                -- unhide real_obj
                -- select real_obj
                
                strMsg = ( ss as string )
            )
            else
            (
                deleteModifier obj uvwmod
                strMsg = "No error face(s)"
            )--if.. else..
            
            format ( strMsg + "\n" )
            messageBox ( strMsg as string )
            
            progressBar_.value = 0
        )--if
    )--function BreakMismatchingPolyUvwFaceMain


    ----------------------------------------------------------------------------------------------------
    function InvalidMaterialDetectorMain progressBar_ =
    (
        if selection.count == 1 then
        (
            -- get material info of selected object.
            local base_obj = $.baseobject
            local real_obj = selection[1]
            local map_channel = 1
            local obj = real_obj
            
            setCommandPanelTaskMode #modify
            
            local facecount = obj.faces.count
            
            format "Analyzing and manipulating % ...\n" real_obj.name
            format "- % has % faces\n" real_obj.name facecount
            
            select real_obj
            uvwmod = Unwrap_UVW()
            addModifier real_obj uvwmod
            uvwmod.setMapChannel map_channel
            uvwmod.updateView()
            uvwmod.setResetPivotOnSelection false
            uvwmod.setTVSubObjectMode 3
            uvwmod.edit()

            --local polycount = uvwmod.numberPolygons()
            local errorFaces = #{}
            errorFaces[facecount] = False
            local numErrorFaces = 0
            
            --format "- polycount = %\n" polycount

            local iProgressUpdateStep = facecount / 100
            local iProgressUpdateCounter = 0
            
            local x, y, width, height, areaUvw, areaGeom
            local arrPolyFaceEdges = #( #() )
            arrPolyFaceEdges[facecount] = #()
            local arrUvwFaceEdges = #( #() )
            arrUvwFaceEdges[facecount] = #()

            /** construct Poly face edge info
                construct Uvw face edge info
                - jintaeks on 오전 11:03 2013-12-03 */
            for f = 1 to facecount do
            (
                local real_mat_id = obj.GetFaceMaterial f
                local id_in_mmat = 0
                if classof real_obj.material == Standard then
                (
                    if real_mat_id != 1 then
                    (
                        id_in_mmat = 0
                    )--if
                )
                else
                (
                    id_in_mmat = findItem real_obj.material.materialIDList real_mat_id
                )--if.. else..
            
                if id_in_mmat <= 0 then
                (
                    errorFaces[f] = true
                    numErrorFaces += 1
                )--if
                
                -- update progress bar. jintaeks on 오전 11:27 2013-11-14
                iProgressUpdateCounter += 1
                if iProgressUpdateCounter >= iProgressUpdateStep then
                (
                    iProgressUpdateCounter = 0
                    progressBar_.value = ( f as float / facecount ) * 100
                    windows.processPostedMessages()
                )--if
            )--for

            local ss = stringStream ""
            local strMsg
            if numErrorFaces >= 1 then
            (
                --format "- flatten error faces\n"
                uvwmod.selectFaces errorFaces
                format "selected % faces" numErrorFaces to:ss
                strMsg = ( ss as string )
            )
            else
            (
                deleteModifier obj uvwmod
                strMsg = "No error face(s)"
            )--if.. else..
            
            format ( strMsg + "\n" )
            messageBox ( strMsg as string )
            
            progressBar_.value = 0
        )--if
    )--function InvalidMaterialDetectorMain progressBar_


     ----------------------------------------------------------------------------------------------------
    /** @brief  remove invalid face material Id
        @date   jintaeks on 16:59 2013-12-18 */
    function _RemoveInvalidFaceMaterial &obj &material_ progressBar_ =
    (
        setCommandPanelTaskMode #modify
        
        local map_channel = 1
        local facecount = obj.faces.count
        
        format "Analyzing and manipulating % ...\n" obj.name
        format "- % has % faces\n" obj.name facecount
        
        select obj
        uvwmod = Unwrap_UVW()
        addModifier obj uvwmod
        uvwmod.setMapChannel map_channel
        uvwmod.updateView()
        uvwmod.setResetPivotOnSelection false
        uvwmod.setTVSubObjectMode 3
        uvwmod.edit()

        --local polycount = uvwmod.numberPolygons()
        local errorFaces = #{}
        errorFaces[facecount] = False
        local numErrorFaces = 0
        local numMtrlIds = 0
        local arrMtrlIds = #()
        
        --format "- polycount = %\n" polycount

        local iProgressUpdateStep = facecount / 100
        local iProgressUpdateCounter = 0

        local iDefaultMtrlId = 1
        if classof material_ == Standard then
        (
            iDefaultMtrlId = 1
        )
        else if classof material_ == MultiMaterial then
        (
            iDefaultMtrlId = material_.materialIDList[1]
        )
        else
        (
            messageBox "Do not support this type of material"
            return undefined
        )--if.. else if.. else..
        
        /** construct Poly face edge info
            construct Uvw face edge info
            - jintaeks on 오전 11:03 2013-12-03 */
        for f = 1 to facecount do
        (
            local real_mat_id = polyop.getFaceMatID obj f
            --format "materialId = %\n" real_mat_id

            if classof material_ == Standard then
            (
                polyop.setFaceMatID obj f iDefaultMtrlId
                if arrMtrlIds[real_mat_id] != true then
                (
                    arrMtrlIds[real_mat_id] = true
                    numMtrlIds += 1
                )--if
            )
            else if classof material_ == MultiMaterial then
            (
                local id_in_mmat = findItem material_.materialIDList real_mat_id
                if id_in_mmat <= 0 then
                (
                    polyop.setFaceMatID obj f iDefaultMtrlId
                    errorFaces[f] = true
                    numErrorFaces += 1
                )
                else
                (
                    if arrMtrlIds[id_in_mmat] != true then
                    (
                        arrMtrlIds[id_in_mmat] = true
                        numMtrlIds += 1
                    )--if
                )--if.. else..
            )--if.. else if..
            
            -- update progress bar. jintaeks on 오전 11:27 2013-11-14
            iProgressUpdateCounter += 1
            if iProgressUpdateCounter >= iProgressUpdateStep then
            (
                iProgressUpdateCounter = 0
                progressBar_.value = ( f as float / facecount ) * 100
                windows.processPostedMessages()
            )--if
        )--for

        local ss = stringStream ""
        local strMsg = "No redundant material(s)"
        
        if classof material_ == Standard then
        (
            if numMtrlIds >= 2 then
            (
                format "% materials merged" numMtrlIds to:ss
                strMsg = ( ss as string )
            )--if
        )
        else if classof material_ == MultiMaterial then
        (
            local iDifference = ( numMtrlIds - material_.materialIDList.count )
            if iDifference != 0 then
            (
                format "% different material(s) merged into %" numMtrlIds iDefaultMtrlId to:ss
            )--if
        )--if.. else if..

        deleteModifier obj uvwmod
        
        format ( strMsg + "\n" )
        messageBox ( strMsg as string )
        
        progressBar_.value = 0
    )--function _RemoveInvalidFaceMaterial progressBar_

    function RemoveInvalidFaceMaterialMain progressBar_ =
    (
        if selection.count == 1 then
        (
            -- get material info of selected object.
            local base_obj = $.baseobject
            local obj = selection[1]

            if classof obj.material == Standard then
            (
                _RemoveInvalidFaceMaterial &obj &obj.material progressBar_
            )
            else
            (
                if classof obj.material == MultiMaterial then
                (
                    _RemoveInvalidFaceMaterial &obj &obj.material progressBar_
                )
                else if classof obj.material == Shell_Material then
                (
                    _RemoveInvalidFaceMaterial &obj &obj.material.originalMaterial progressBar_
                    --_RemoveInvalidFaceMaterial &obj.material.bakedMaterial
                )--if.. else if..
            )--if.. else..
        )--if
    )--function

    ----------------------------------------------------------------------------------------------------
    -- rollout definition. seojtdoc
    rollout rollInvalidFaceBreaker "Invalid Face Breaker"
    (
        group "Breaker"
        (
            checkbox chkAutoBreak "Auto Break" checked:true
            button btnBreaker "Break 0 Area Uvw Faces" align:#right
        )--group "Breaker"

        group "Slicer"
        (
            spinner spinnerSlicerUvWidth "Uv Width:" range:[1,999,1] type:#integer fieldWidth:80 align:#left
            button btnSlicer "Select Slicer Uvw Faces" align:#right
        )--group "Breaker"

        group "Flattener"
        (
            checkbox chkAutoFlatten "Auto Flatten" checked:true
            button btnFlattener "Flatten wrong side Uvw Faces" align:#right
        )--group "Flattener"

        group "Shared Face Breaker"
        (
            checkbox chkAutoUnweld "Auto Unweld " checked:false
            button btnUnwelder "Break Shared Uvw Faces" align:#right
        )--group "Unwelder"

        group "Mismatching Face Breaker"
        (
            checkbox chkAutoBreakMismatchingFace "Auto break" checked:false
            button btnMismatchingFaceBreaker "Break Mismatching Poly,Uvw Faces" align:#right
        )--group "Mismatching Face Breaker"
        
        group "Invalid Material Detector"
        (
            button btnInvalidMaterialDetector "Select Invalid Material Faces" align:#right
        )--group "Mismatching Face Breaker"

        group "Remove Invalid Face Material Id"
        (
            button btnRemoveInvalidFaceMaterialId "Remove Invalid Face Material Id" align:#right
        )--group "Remove Invalid Face Material Id"

        progressBar m_progressBar
        label lblAuthor "jintaeks@dongseo.ac.kr" height:16
        label lblDsuCopyright "Copyright (c) 2017 Dicon, DSU" height:16

        ------

        on rollInvalidFaceBreaker open do
        (
            m_file = openFile m_filename mode:"rt"

            if m_file == undefined then
            (
                -- create a new ini file because it doesn't exist
                m_file = createFile m_filename

                format "%\n%\n%\n" true false false
                format "50\n"

                chkAutoBreak.checked = true
                chkAutoFlatten.checked = false
                spinnerSlicerUvWidth.value = 50
            )
            else
            (
                chkAutoBreak.checked = execute (readLine m_file)
                chkAutoFlatten.checked = execute (readLine m_file)
                spinnerSlicerUvWidth.value = execute (readLine m_file)
            )--if.. else..
        )--on rollInvalidFaceBreaker open do

        on rollInvalidFaceBreaker close do
        (
            if m_file != undefined then
            (
                close m_file
            )--if

            deleteFile m_filename
            m_file = createFile m_filename

            format "%\n" chkAutoBreak.checked to:m_file
            format "%\n" chkAutoFlatten.checked to:m_file
            format "%\n" spinnerSlicerUvWidth.value to:m_file

            close m_file
        )--on rollInvalidFaceBreaker  close do

        on btnBreaker pressed do
        (
            if selection.count == 1 then
            (
                BreakFaceMain chkAutoBreak.checked m_progressBar
            )
            else
            (
                messageBox "No object selected"
            )--if.. else..
        )--on btnBreaker pressed do
        
        on btnSlicer pressed do
        (
            if selection.count == 1 then
            (
                SliceFaceMain spinnerSlicerUvWidth.value m_progressBar
            )
            else
            (
                messageBox "No object selected"
            )--if.. else..
        )--on btnSlicer pressed do

        on btnCancelProcess pressed do
        (
            m_bIsCancelProcess = true
        )--on btnCancelProcess pressed do
        
        on btnFlattener pressed Do
        (
            if selection.count == 1 then
            (
                FlattenFaceMain chkAutoFlatten.checked m_progressBar
            )
            else
            (
                messageBox "No object selected"
            )--if.. else..
        )--on btnFlattener pressed Do
        
        on btnUnwelder pressed do
        (
            if selection.count == 1 then
            (
                BreakSameUvwFaceMain chkAutoUnweld.checked m_progressBar
            )
            else
            (
                messageBox "No object selected"
            )--if.. else..
        )--on btnUnwelder pressed do
        
        on btnMismatchingFaceBreaker pressed do
        (
            if selection.count == 1 then
            (
                BreakMismatchingPolyUvwFaceMain chkAutoBreakMismatchingFace.checked m_progressBar
            )
            else
            (
                messageBox "No object selected"
            )--if.. else..
        )--on btnMismatchingFaceBreaker pressed do
        
        on btnInvalidMaterialDetector pressed do
        (
            if selection.count == 1 then
            (
                InvalidMaterialDetectorMain m_progressBar
            )
            else
            (
                messageBox "No object selected"
            )--if.. else..
        )--on btnInvalidMaterialDetector pressed do
        
        on btnRemoveInvalidFaceMaterialId pressed do
        (
            if selection.count == 1 then
            (
                RemoveInvalidFaceMaterialMain m_progressBar
            )
            else
            (
                messageBox "No object selected"
            )--if.. else..
        )--on btnRemoveInvalidFaceMaterialId pressed do
    )--rollout rollInvalidFaceBreaker "Invalid Face Breaker"

    on execute do
    (
        --createDialog rollInvalidFaceBreaker 300 446
        theNewFloater = newRolloutFloater "Invalid Face Breaker v1.0.5" 280 600
        addRollout rollInvalidFaceBreaker theNewFloater rolledUp:false
    )--on execute do
)--macroScript InvalidFaceBreaker
