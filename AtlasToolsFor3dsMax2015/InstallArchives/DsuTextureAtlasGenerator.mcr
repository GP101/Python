-- Copyright 2009 3d-io
-- 3D-IO Games & Video Production GmbH | Rüdesheimer Straße 9 | 65197 Wiesbaden | GERMANY
-- Contact: info@3d-io.com
-- Author: Friedrich Hanisch, friedrich@3d-io.com

-- Version 1.0.5

/* Max Script listener output for Atlas01. jintaeks on 2013-11-11
    TAG begins.
    Analyzing and manipulating Atlas01 ...
    ... Atlas01 has 1214 faces
    Probably 2244 errors in mesh(!) of Atlas01, i.e. those map faces are too small/thin!
    ... analyzing Atlas01's uvs and geometry ...
    ...... found 4 materials with 4 new textures
    ...... 1300 slice planes need to be generated
    ... Atlas01: slicing geometry
    ... Atlas01: normalizing tex coords, analyzing 8693 edges ...
    ...... broke 1868 of 8693 texture edges in 23 secs
    TAG will make a texture atlas now.
    Packing 4 textures
    Drawing the texture atlas with size 512*1024 ...
    ... adding C:\Users\digitech17\Desktop\¿ÀºêÁ§Æ®¼öÁ¤\°³¼±¹®_Re\Build001_Test01_Dif01.dds
    ... adding C:\Users\digitech17\Desktop\¿ÀºêÁ§Æ®¼öÁ¤\°³¼±¹®_Re\Build001_Test01_Dif03.dds
    ... adding C:\Users\digitech17\Desktop\¿ÀºêÁ§Æ®¼öÁ¤\°³¼±¹®_Re\Build001_Test01_Dif02.dds
    ... adding C:\Users\digitech17\Desktop\¿ÀºêÁ§Æ®¼öÁ¤\°³¼±¹®_Re\Build001_Test01_Dif04.dds
    TAG makes new UV coordinates.
    Rearrange Atlas01's UVs
    TAG ended.
*/

-- include atlas info manager. jintaeks on ¿ÀÈÄ 5:00 2013-11-13
--include @"F:\techsupport\source\DsuAtlasMaxPlugin\KAtlasInfo.ms"


macroScript TexAtlasGen2
            category:"Dsu"
            Icon:#("Patches",1)
(
    --fileIn "KAtlasInfo.ms"
    /** @struct KMaterialInfo
        @brief  a material information
        @since  jintaeks ¿ÀÀü 10:56 2013-11-13
        @date   jintaeks on ¿ÀÀü 10:19 2013-11-19
                - added 'm_bIsRotateCcw' to manipulate texture rotation */
    struct KMaterialInfo
    (
        m_strName, -- material name
        m_iLeft, -- texture left position in atlas
        m_iTop, -- texture top position in atlas
        m_iWidth, -- texture width of this texture
        m_iHeight, -- texture height of this texture
        --
        m_bIsDiffuse, -- has diffuse map
        m_bIsBump, -- has bump map
        m_bIsSpecular, -- has specular map
        m_bIsGlossiness, -- has glossiness map
        --
        m_strDiffuse, -- diffuse map filename
        m_strBump, -- bump map filename
        m_strSpecular, -- specular level map filename
        m_strGlossiness, -- glossiness map filename
        --
        m_bIsRotateCcw, -- texture is rotated in Ccw.
        
        function Print =
        (
            format "Mtrl name = %\n" m_strname
            format "Mtrl left = %\n" m_iLeft
            format "Mtrl top = %\n" m_iTop
            format "Mtrl width = %\n" m_iWidth
            format "Mtrl height = %\n" m_iHeight
            if m_bIsDiffuse == true then
            (
                format "Mtrl diffuse = %\n" m_strDiffuse
            )--if
            if m_bIsBump == true then
            (
                format "Mtrl bump = %\n" m_strBump
            )--if
            if m_bIsSpecular == true then
            (
                format "Mtrl specular = %\n" m_strSpecular
            )--if
            if m_bIsGlossiness == true then
            (
                format "Mtrl glossiness = %\n" m_strGlossiness
            )--if
            format "Rotate Ccw = %\n" ( m_bIsRotateCcw as integer )
        ),--function Print

        /** @brief  function IsFileNameExist
            @param  filename_ : [in] filename(can be contain path name)
            @return #diffuse #bump #specular #glossiness undefined
            @example function IsFileNameExist
            local iFilenameType = mtrl.IsFilenameExist "C:\\build001_test01_dif04_n.dds"
            if iFilenameType != undefined do format "%\n" iFilenameType
            - jintaeks on ¿ÀÈÄ 2:33 2013-11-13 */
        function IsFileNameExist filename_ =
        (
            local inFilename = filenameFromPath filename_
            if m_bIsDiffuse == true then
            (
                filename = filenameFrompath m_strDiffuse
                if stricmp filename inFilename == 0 do return #diffuse
            )--if
            if m_bIsBump == true then
            (
                filename = filenameFrompath m_strBump
                if stricmp filename inFilename == 0 do return #bump
            )--if
            if m_bIsSpecular == true then
            (
                filename = filenameFrompath m_strSpecular
                if stricmp filename inFilename == 0 do return #specular
            )--if            
            if m_bIsGlossiness == true then
            (
                filename = filenameFrompath m_strGlossiness
                if stricmp filename inFilename == 0 do return #glossiness
            )--if            
            
            return undefined
        ), --function IsFileNameExist()
        
        function Void = () -- placeholder for consistent function definition
    )--struct KMaterialInfo

    /** @struct KAtlasInfo
        @brief  atlas information
        @date   jintaeks on ¿ÀÈÄ 3:22 2013-11-13 */
    struct KAtlasInfo
    (
        m_aMaterialInfo,    -- KMaterialInfo array
        m_strAtlasName,     -- atlas name(equal to selected object name)
        m_iAtlasWidth,      -- atlas width in pixel
        m_iAtlasHeight,     -- atlas height in pixel
        
        -- @brief   initialize atlas information from string data
        -- @date    jintaeks on ¿ÀÈÄ 3:23 2013-11-13
        function Initialize strData_ =
        (
            m_aMaterialInfo = #()
            m_strAtlasName = ""
            m_iAtlasWidth = 0
            m_iAtlasHeight = 0
            
            local iParseState = 0 -- 0 for normal state, 1 for material parse state
            local iMaterialCount = 0
            local strInfo = #()
            strInfo = FilterString  strData_ "\n"
            
            for str in strInfo Do
            (
                local strKeyValue
                local strKey
                local strValue
                
                try
                (
                    strKeyValue = FilterString str "="
                    strKey = trimRight ( trimLeft strKeyValue[1] )
                    strValue = trimRight ( trimLeft strKeyValue[2] )
                )
                catch
                (
                    return undefined
                )--try.. catch..

                if iParseState == 0 then -- normal parse state
                (
                    if stricmp strKey "Object" == 0 then
                    (
                        m_strAtlasName = trimLeft ( trimRight strValue )
                    )
                    else if stricmp strKey "Width" == 0 then
                    (
                        m_iAtlasWidth = ( trimLeft ( trimRight strValue ) ) as integer
                    )
                    else if stricmp strKey "Height" == 0 then
                    (
                        m_iAtlasHeight = ( trimLeft ( trimRight strValue ) ) as integer
                    )
                    else if stricmp strKey "Material" == 0 then
                    (
                        local astrMtrlInfo = FilterString strValue ","
                        if astrMtrlInfo.count == 6 then
                        (
                            local mtrl = KMaterialInfo()
                            mtrl.m_strName = trimLeft( trimRight astrMtrlInfo[1] )
                            mtrl.m_iLeft = ( trimLeft ( trimRight astrMtrlInfo[2] ) ) as integer
                            mtrl.m_iTop = ( trimLeft ( trimRight astrMtrlInfo[3] ) ) as integer
                            mtrl.m_iWidth = ( trimLeft ( trimRight astrMtrlInfo[4] ) ) as integer
                            mtrl.m_iHeight = ( trimLeft ( trimRight astrMtrlInfo[5] ) ) as integer
                            mtrl.m_bIsDiffuse = false
                            mtrl.m_bIsBump = false
                            mtrl.m_bIsSpecular = false
                            mtrl.m_bIsGlossiness = false
                            mtrl.m_bIsRotateCcw = false
                            
                            -- set texture rotate in Ccw state. jintaeks on ¿ÀÀü 10:26 2013-11-19
                            local strIsRotateCcw = trimLeft ( trimRight astrMtrlInfo[6] )
                            if stricmp strIsRotateCcw "true" == 0 then
                            (
                                mtrl.m_bIsRotateCcw = true
                            )--if
                                
                            append m_aMaterialInfo mtrl
                            iMaterialCount += 1
                        )--if
                    )
                    else if stricmp strKey "Diffuse" == 0 then
                    (
                        m_aMaterialInfo[iMaterialCount].m_strDiffuse = strValue
                        m_aMaterialInfo[iMaterialCount].m_bIsDiffuse = true
                    )
                    else if stricmp strKey "Bump" == 0 then
                    (
                        m_aMaterialInfo[iMaterialCount].m_strBump = strValue
                        m_aMaterialInfo[iMaterialCount].m_bIsBump = true
                    )
                    else if stricmp strKey "SpecularLevel" == 0 then
                    (
                        m_aMaterialInfo[iMaterialCount].m_strSpecular = strValue
                        m_aMaterialInfo[iMaterialCount].m_bIsSpecular = true
                    )
                    else if stricmp strKey "Glossiness" == 0 then
                    (
                        m_aMaterialInfo[iMaterialCount].m_strGlossiness = strValue
                        m_aMaterialInfo[iMaterialCount].m_bIsGlossiness = true
                    )--if.. else if..
                )--if.. else..
            )--for
            
            return true
        ),--function Initialize strData_ =
        
        -- @brief   print atlas information
        -- @date    jintaeks on ¿ÀÈÄ 3:24 2013-11-13
        function Print =
        (
            format "Atlas Info\n"
            format "name = %\n" m_strAtlasName
            format "width = %\n" m_iAtlasWidth
            format "height = %\n" m_iAtlasHeight
            format "num mtrl = %\n" m_aMaterialInfo.count
            for mtrl in m_aMaterialInfo Do
            (
                mtrl.Print()
            )--for
        ),--function Print =
        
        -- @brief   get number of materials
        -- @date    jintaks on ¿ÀÈÄ 3:27 2013-11-13
        function GetNumMaterial =
        (
            return m_aMaterialInfo.count
        ),--function GetNumMaterial =
        
        -- @brief   find KMaterialInfo by containing filename
        -- @param   filename_ : [in] texture filanem(may contain path name)
        -- @return  KMaterialInfo or undefined
        -- @date    jintaeks on ¿ÀÈÄ 3:27 2013-11-13
        function FindMaterialByContainingFilename filename_ =
        (
            for mtrl in m_aMaterialInfo do
            (
                if mtrl.IsFileNameExist filename_ != undefined then
                (
                    return mtrl
                )--if
            )--for
            return undefined
        ),--function FindMaterialByContainingFilename filename_
        
        -- @brief   find material by it's name
        -- @parame  strMaterialName_ : [in] material name
        -- @date    jintaeks on ¿ÀÈÄ 12:12 2013-11-18
        function FindMaterialByMaterialName strMaterialName_ =
        (
            for mtrl in m_aMaterialInfo do
            (
                if stricmp strMaterialName_ mtrl.m_strName == 0 then
                (
                    return mtrl
                )--if
            )--for
            return undefined
        ),--function FindMaterialByMaterialName strMaterialName_ =
        
        function IsBump =
        (
            if m_aMaterialInfo == undefined then
            (
                return false
            )--if
            
            if m_aMaterialInfo.count <= 0 then
            (
                return false
            )--if
            
            for mtrl in m_aMaterialInfo do
            (
                if mtrl.m_bIsBump == true then
                (
                    return true
                )--if
            )--for
            
            return false
        ),

        function IsSpecular =
        (
            if m_aMaterialInfo == undefined then
            (
                return false
            )--if
            
            if m_aMaterialInfo.count <= 0 then
            (
                return false
            )--if
            
            for mtrl in m_aMaterialInfo do
            (
                if mtrl.m_bIsSpecular == true then
                (
                    return true
                )--if
            )--for
            
            return false
        ),

        function IsGlossiness =
        (
            if m_aMaterialInfo == undefined then
            (
                return false
            )--if
            
            if m_aMaterialInfo.count <= 0 then
            (
                return false
            )--if
            
            for mtrl in m_aMaterialInfo do
            (
                if mtrl.m_bIsGlossiness == true then
                (
                    return true
                )--if
            )--for
            
            return false
        ),

        function Void = () -- placeholder for consistent function definition
    )--struct KAtlasInfo

    
    -- seojtdoc. jintaeks on ¿ÀÈÄ 2:43 2013-11-19 qff
    local filename = "$temp\\DsuTextureAtlasGenerator2.cfg"
    local file
    local m_bIsUseExternalAtlasManager = true -- use external atlas info manager. jintaeks on ¿ÀÈÄ 5:43 2013-11-13
    local m_atlasInfo -- atlas info. jintaeks on ¿ÀÈÄ 5:02 2013-11-13
    local texture_atlas
    local m_bitmaps -- jintaeks on ¿ÀÈÄ 4:08 2013-11-20
    local m_bIsAtlasGenerated = false -- jintaeks on ¿ÀÈÄ 7:49 2013-11-25
    local m_bIsCancelProcess = false -- jintaeks on ¿ÀÈÄ 7:49 2013-11-25

    /** @struct SMaterialInfo
        @brief  material info for a object */
    struct SMaterialInfo
    (
        mats_in_multi_used = #{}, -- materials can have different ids than their position in multimaterial ...
        mmat_ids = #(),
        num_materials_used = 0,
        mmatid_to_texid = #()
    )--struct SMaterialInfo
    
    /** @struct SBitmap
        @brief  single bitmap informatoin
        @date   ¿ÀÈÄ 12:02 2013-11-18
                - added materialName to resolve ambigity */
    struct SBitmap
    (
        bmp,
        filename,
        materialName, -- added to resolve duplcate multiple same filenames for different materials. jintaeks ¿ÀÈÄ 12:00 2013-11-18
        rotated = false, -- counterclockwise 90 degrees, or not
        area,
        height,
        width,
        x = -100,
        y = -100,
        is_cutted,

        function Rotate =
        (
            (swap height width);
            rotated = not rotated
        )--function Rotate =
    )--struct SBitmap
    
    ---

    /** @function   MakeValueFrom0To1
        @brief      make value from 0 to 1
                    this function is used to normalize uv coordinate
        @date       jintaeks on ¿ÀÀü 9:52 2013-11-26 */
    function MakeValueFrom0To1 v_ =
    (
        if v_ > 0 then
            return v_ - (v_ as integer )
        Else
            return v_ - ( v_ as integer ) + 1.0 -- add 1.0 to pose correct uv coordinate.
    )--function MakeValueFrom0To1 v_
    
    /** @brief  get edge vertices of a face
        @return (begin vertex, end vertex) of edge
        @date   jintaeks on 2013-11-12 */
    function tag_getEdgeVerts obj face_index edge_index =
    (
        if (classOf obj) == Editable_Poly then
        (
            -- get the face's vertices as an array. jintaeks on 2013-11-12
            local verts = (polyop.getFaceVerts obj face_index)
            local edges = (polyop.getFaceEdges obj face_index)
     
            edge_index = findItem edges edge_index
            if edge_index == edges.count then
                return #(verts[edge_index], verts[1]) -- for last edge, it's second vertex is begin vertex. jintaeks on 2013-11-12
            else
                return #(verts[edge_index], verts[edge_index+1])
        )
        else
        (
            return "ERROR"
        )--if.. else..
    )--tag_getEdgeVerts()

    /** @brief  get the <point3 uvw> of face vertices at 'index'
        @return a vertex of face at index as a <point3>
        @date   jintaeks on 2013-11-12 */
    function tag_getMapVert obj map_channel_ face_indices vertex_ =
    (
        if (classOf obj) == Editable_Poly then
        (
            if (classof face_indices) == integer then face_indices = #(face_indices)
            else face_indices = face_indices as Array
            
            local mesh_verts = #()
            local text_verts = #()
            for i in face_indices do
            (
                join mesh_verts (polyop.getFaceVerts obj i)
                -- get vertex indices of the specified map face as an array. jintaeks on 2013-11-12
                join text_verts (polyop.getMapFace obj map_channel_ i)
            )
            local index = findItem mesh_verts vertex_ -- get vertex index. jintaeks on 2013-11-12
            -- get the coordinates of the specified map vertex as a <point3>. jintaeks on 2013-11-12
            return (polyop.getMapVert obj map_channel_ text_verts[index])
        )
        else
        (
            return "ERROR"
        )--if.. else..
    )--tag_getMapVert()

    /** @brief  set the map coordinates of the vertex as <point3 uvw>
        @param  index_ : [in] vertex index
        @param  vert_ : [in] mapping <point3 uvw>
        @date   jintaeks on ¿ÀÈÄ 2:49 2013-11-12 */
    function tag_setMapVert obj map_channel_ face_indices index vert_ =
    (
        if (classOf obj) == Editable_Poly then
        (
            if (classof face_indices) == integer then face_indices = #(face_indices)
            else face_indices = face_indices as Array

            local mesh_verts = #()
            local text_verts = #()
            for i in face_indices do
            (
                join mesh_verts (polyop.getFaceVerts obj i)
                join text_verts (polyop.getMapFace obj map_channel_ i)
            )
            index = findItem mesh_verts index
            polyop.setMapVert obj map_channel_ text_verts[index] vert_
        )
        else
        (
            "ERROR"
        )--if.. else..
    )--function tag_setMapVert obj map_channel_ face_indices index vert_ =
     
    /** @brief  get World position of object vertex.
        @return get vertex as <point3> in World space
        @param  index_ : [in] vertex index_
        @date   jintaeks on 2013-11-12 */
    function tag_getVertexWorld obj_ index_ =
    (
        if (classOf obj_) == Editable_Poly then
            return (in coordsys world polyop.getVert obj_ index_)
        else
            return "ERROR"
    )--function tag_getVertexWorld obj_ index_ =
     
    /** @brief  slice faces_ of obj by local plane ( normal_, center_ )
        @return true when slices is successful
        @date   jintaeks on 2013-11-12 */
    function tag_slice obj_ faces_ normal_ center_ =
    (
        if (classOf obj_) == Editable_Poly then
        (
            -- get local plane of 'obj_'. jintaeks on 2013-11-12
            local plane = (ray center_ normal_)
            -- return 'true' when slice is successful. jintaeks on 2013-11-12
            return polyop.slice obj_ faces_ plane
        )
        else
        (
            return false
        )--if.. else..
    )--function tag_slice obj_ faces_ normal_ center_ =
     
    -- helper functions
     
    /** @brief check whether a and b is mathematically equal or not.
        @date   jintaeks on ¿ÀÈÄ 2:40 2013-11-12 */
    function tag_equal_int a b =
    (
        if a - b > 0.001 or a - b < -0.001 then
            return false
        else
            return true
    )--tag_equal()
     
    ---
    /** @brief  check face is mirrored or not.
        @return true when face is mirrored.
        @param  face_index : [in] face index
        @date   jintaeks on 2013-11-12 */
    function tag_checkMirror obj map_channel_ face_index =
    (
        local sum = 0
        
        if (classOf obj) == Editable_Poly then
        (
            local verts = (polyop.getFaceVerts obj face_index)
            local edges = (polyop.getFaceVerts obj face_index)
            
            for i = 1 to edges.count do
            (
                local edge_verts
                local tv1, tv2, tv3
     
                if i == edges.count-1 then
                (
                    tv1 = (tag_getMapVert obj map_channel_ face_index verts[i])
                    tv2 = (tag_getMapVert obj map_channel_ face_index verts[i+1])
                    tv3 = (tag_getMapVert obj map_channel_ face_index verts[1])
                )
                else if i == edges.count then
                (
                    tv1 = (tag_getMapVert obj map_channel_ face_index verts[i])
                    tv2 = (tag_getMapVert obj map_channel_ face_index verts[1])
                    tv3 = (tag_getMapVert obj map_channel_ face_index verts[2])
                )
                else
                (
                    tv1 = (tag_getMapVert obj map_channel_ face_index verts[i+0])
                    tv2 = (tag_getMapVert obj map_channel_ face_index verts[i+1])
                    tv3 = (tag_getMapVert obj map_channel_ face_index verts[i+2])
                )--if.. else..
                
                local edge1_vect = normalize (tv2 - tv1)
                local edge2_vect = normalize (tv3 - tv1)
        
                -- (cross edge1_vect edge2_vect)
                sum += (cross edge1_vect edge2_vect).z
            )--for i = 1 to edges.count do
        )--if
        
        return (sum <= 0)
    )--function tag_checkMirror obj map_channel_ face_index =
 
    /** @brief  generate atlas texture
        @param  texture_atlas_filename_ : [in] full path texture filename to create
        @param  size_of_texatlas_x : [in] atlas texture width
        @param  size_of_texatlas_y : [in] atlas texture height
        @param  bitmaps : [in] bitmaps to write
        @param  isPrintMsgs_ : [in] print log message to Max Script Listener
        @date   jintaeks on ¿ÀÈÄ 4:57 2013-11-14 */
    function _GenerateAtlasTexture
        &texture_atlas
        texture_atlas_filename_
        size_of_texatlas_x
        size_of_texatlas_y
        &bitmaps_
        isPrintMsgs_
        isDoUndo_
        padding_
        isPadding_tresize_
        =
    (    
        -- create the texture atlas, at last
        -- local texture_atlas
        try
        (
            texture_atlas = Bitmap size_of_texatlas_x size_of_texatlas_y
        )
        catch
        (
            messagebox "The texture atlas couldn't be generated because Max ran out of Memory.\nTry restarting max, wireframe view and/or a renderfarm ..."
            format "Error! Couldn't generate bitmap for texture atlas with size %*%!\n" size_of_texatlas_x size_of_texatlas_y
            return -1
        )
        texture_atlas.filename = texture_atlas_filename_

        if isPrintMsgs_ then
        (
            format "Drawing the texture atlas with size %*% ...\n" size_of_texatlas_x size_of_texatlas_y
        )--if
        
        -- draw the textures into the atlas
        for sbmp in bitmaps_ do with undo isDoUndo_
        (
            if isPrintMsgs_ do format "... adding %\n" sbmp.filename
            
            if sbmp.filename == undefined do continue
    
            if sbmp.x < 0 do continue -- should not happen, y'know?!
            
            -- no padding for uv mapped objects, right?
            local tp = padding_
            if not sbmp.is_cutted do tp = 0

            -- but don't forget the padding!
            local temp_bitmap = sbmp.bmp
            if tp > 0 and isPadding_tresize_ then
            (
                if sbmp.bmp.width <= (tp*2) or sbmp.bmp.height <= (tp*2) do
                (
                    messagebox "Padding number too big! Check your texture sizes!"
                    return -1
                )
                temp_bitmap = Bitmap (sbmp.bmp.width-(tp*2)) (sbmp.bmp.height-(tp*2))
                copy sbmp.bmp temp_bitmap
            )--if
            
            local pixels

            if not sbmp.rotated then
            (
                for i = 0 to temp_bitmap.height-1 do
                (
                    pixels = getPixels temp_bitmap [0, i] temp_bitmap.width
                    setPixels texture_atlas [tp+sbmp.x, tp+sbmp.y+i] pixels
                )--for
            )
            else -- rotate the texture CCW
            (
                for i = 0 to temp_bitmap.height-1 do
                (
                    local pixels = getPixels temp_bitmap [0, i] temp_bitmap.width
                    for j = 0 to temp_bitmap.width-1 do
                    (
                        setPixels texture_atlas [tp+sbmp.x+i, tp+sbmp.y+temp_bitmap.width-(j+1)] #(pixels[j+1])
                    )--for
                )--for
            )--if.. else..
            close temp_bitmap
            
            -- the frame (padding)
            if tp > 0 do
            (
                local ox, oy, nw, nh
                ox = sbmp.x+tp -- origin x, y
                oy = sbmp.y+tp
                nw = sbmp.width-(tp*2) -- new width, height
                nh = sbmp.height-(tp*2)
                --format "debug : ox = % oy = % nw = % nh = %\n" ox oy nw nh
                -- fixed bug. crash problem when texutre is rotated. jintaeks on ¿ÀÀü 11:06 2013-11-29
                if sbmp.rotated then
                (
                    swap nw nh
                )--if
                
                -- top
                pixels = getPixels texture_atlas [ox, oy] nw
                for i = 0 to tp-1 do
                    setPixels texture_atlas [ox, sbmp.y+i] pixels
                -- bottom
                pixels = getPixels texture_atlas [ox, oy+nh-1] nw
                for i = 0 to tp-1 do
                    setPixels texture_atlas [ox, oy+nh+i] pixels
                for i = 0 to nh-1 do
                (
                    -- left
                    pixels = getPixels texture_atlas [ox, oy+i] 1
                    for j = 0 to tp-2 do append pixels pixels[1]
                    setPixels texture_atlas [sbmp.x, oy+i] pixels
                    -- right
                    pixels = getPixels texture_atlas [ox+nw-1, oy+i] 1
                    for j = 0 to tp-2 do append pixels pixels[1]
                    -- qff. jintaeks on ¿ÀÀü 10:09 2013-11-29
                    setPixels texture_atlas [ox+nw, oy+i] pixels
                )
                -- the corners
                local pixels_lt = getPixels texture_atlas [ox, oy] 1
                local pixels_rt = getPixels texture_atlas [ox+nw-1, oy] 1
                local pixels_lb = getPixels texture_atlas [ox, oy+nh-1] 1
                local pixels_rb = getPixels texture_atlas [ox+nw-1, oy+nh-1] 1
                for j = 0 to tp-2 do
                (
                    append pixels_lt pixels_lt[1]
                    append pixels_rt pixels_rt[1]
                    append pixels_lb pixels_lb[1]
                    append pixels_rb pixels_rb[1]
                )--for
                for i = 0 to tp-1 do
                (
                    setPixels texture_atlas [sbmp.x, sbmp.y+i] pixels_lt
                    setPixels texture_atlas [ox+nw, sbmp.y+i] pixels_rt
                    setPixels texture_atlas [sbmp.x, oy+nh+i] pixels_lb
                    setPixels texture_atlas [ox+nw, oy+nh+i] pixels_rb
                )--for
            )--if
            
            windows.processPostedMessages() -- jintaeks on ¿ÀÀü 11:42 2013-11-14
        )--for
        
        try
        (
            save texture_atlas quiet:true
            --close texture_atlas. -- garbage collector will clear it. jintaeks on ¿ÀÀü 11:49 2013-11-13
        )
        catch
        (
            if not isDo_ignore_errors do messagebox "Could not save texture atlas!"
            if isPrintMsgs_ do format "Error: texture atlas was not saved to any file.\n"
        )--try.. catch..
    )--function _GenerateAtlasTexture
 
    ---------------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------------
     
    -- Texture Atlas Generator main function. jintaeks on ¿ÀÀü 11:40 2013-11-14 qff
    function TAG
        objs
        progBar_:undefined -- progress bar to display progressing state. jintaeks on ¿ÀÀü 11:41 2013-11-14
        map_channel_:1
        texture_atlas_filename_:"C:\\TEMP\\TESTTEXTUREATLAS.tga"
        padding_:2
        isPadding_tresize_:true
        isDo_undo_:off
        isDo_slicing_:true
        isDo_generate_ta_:true
        isDo_msgs_:false
        isDo_break_all_:false
        isDo_force_padding_:false
        isDo_ignore_errors:false
        =
    (
        if objs.count == 0 do
        (
            return -1
        )--if
        
        local tag_objs = #()
        for o in objs where (((classOf o == Editable_Poly) or (classOf o == PolyMeshObject)) and ((classOf o.material == Standardmaterial) or (classOf o.material == Multimaterial))) do
        (
            append tag_objs o
        )--for

        if tag_objs.count == 0 do
        (
            messagebox "Select correct object type, with correct material type!"
            return -1
        )--if
        
        -- get rid of instanced objects!
        local instances
        for i = 1 to tag_objs.count do with undo isDo_undo_
        (
            if tag_objs[i] != #empty do
            (
                if (InstanceMgr.GetInstances tag_objs[i] &instances) > 1 do
                (
                    for i2 = i+1 to tag_objs.count do
                    (
                        for j in instances do
                        (
                            if tag_objs[i2] == j do
                                tag_objs[i2] = #empty
                        )--for
                    )--for
                )--if
            )--if
        )--for i = 1 to tag_objs.count do with undo isDo_undo_
        local is_too_much = -1
        do
        (
            is_too_much = (findItem tag_objs #empty)
            if is_too_much != 0 do deleteItem tag_objs is_too_much
        ) while is_too_much != 0
            
        if isDo_msgs_ do format "TAG begins.\n"

        if (objs.count-tag_objs.count) > 0 and isDo_msgs_ do format "... % objects won't be manipulated (wrong class or material, or were instances)\n" (objs.count-tag_objs.count)

        local textures = #()
        local materialNames = #() -- material names for 'textures'. jintaeks on ¿ÀÈÄ 12:04 2013-11-18
        local cutted_textures = #{} -- special feature: uvmaps don't have padding
                                    -- no texture will have padding when slicing isn't needed, that's a bug ...
        local material_info = #()
        material_info[tag_objs.count] = 0
        
        -------------------------------------------------------------
        -- begin loop        
        local o = 0
        for real_obj in tag_objs do with undo isDo_undo_
        (
            o += 1
            local obj = real_obj
            
            /** when there is a modifier on top of the modifier stack.
                query to user and convert to editable poly when user selected 'yes'
                - jintaeks on ¿ÀÈÄ 4:58 2013-12-03 */
            if real_obj.modifiers.count >= 1 do
            (
                local bIsQueryResult = queryBox "Convert to Editable Poly?" beep:false
                if bIsQueryResult then
                (
                    convertTo real_obj PolyMeshObject
                    obj = real_obj
                )--if
            )--if

            if isDo_slicing_ or isDo_force_padding_ do
            (
                -- this is a workaround for max 9, because collapseNodeTo is buggy
                obj = editable_mesh()
                obj.baseobject = copy real_obj.baseobject
                local save_obj = real_obj.baseobject
                hide real_obj
                convertTo obj PolyMeshObject
            )--if
        
            select obj
            setCommandPanelTaskMode #modify
            windows.processPostedMessages() -- jintaeks on ¿ÀÀü 11:42 2013-11-14
            
            if isDo_msgs_ do format "Analyzing and manipulating % ...\n" real_obj.name
            
            local facecount = obj.faces.count
            local is_UVmapped = false
            
            if isDo_msgs_ do format "... % has % faces\n" real_obj.name facecount
         
            material_info[o] = SMaterialInfo()
            
            local faces_cutplanes = #()
            if isDo_slicing_ do faces_cutplanes[facecount] = #()
         
            -------------------------
            -------------------------
            -- Preparation: Test for UV faces - are their areas too small? Does it have a UV map?
            -------------------------
            
            if isDo_slicing_ do
            (
                -- look for modifiers ...
                if real_obj.modifiers.count >= 1 do
                (
                    for mod in real_obj.modifiers do
                    (
                        if (classOf mod) == Unwrap_UVW or (classOf mod) == Uvwmap do
                        (
                            if not isDo_ignore_errors do
                            (
                                local ss = stringStream ""
                                format "% has at least one modifier which manipulates the meshes' UV coordinates. If you want to see TAG's effect, you probably will have to delete/deactivate it." real_obj.name to:ss
                                messagebox (ss as string)
                            )--if
                            if isDo_msgs_ do format "... Warning: % has UVW modifier!\n" real_obj.name
                        )--if
                    )--for mod in real_obj.modifiers do
                )--if real_obj.modifiers.count > 0 do
                
                -- map channel doesn't seem to be updated otherwise, hmm ...
                local uvwmod = Unwrap_UVW()
                addModifier obj uvwmod
                uvwmod.setMapChannel map_channel_
                uvwmod.setConstantUpdate false
                uvwmod.setShowSelectedVertices false
                uvwmod.updateView()
                uvwmod.setTVSubObjectMode 3 -- set the sub object mode 0 - None, 1 - Vertex, 2 - Edge, 3 - Face
                windows.processPostedMessages() -- jintaeks on ¿ÀÀü 11:42 2013-11-14

                -- first test: is the object uv mapped?
                local x, y, width, height, areaUVW, areaGeom
                uvwmod.getArea #{1..facecount} &x &y &width &height &areaUVW &areaGeom
                is_UVmapped = ((x >= 0.001) and (x+width <= 0.999) and (y >= 0.001) and (y+height <= 0.999))

                deleteModifier obj uvwmod
                windows.processPostedMessages() -- jintaeks on ¿ÀÀü 11:42 2013-11-14

                if not is_UVmapped do
                (
                    -- messageBox "not is_UVmapped"
                    
                    local error_faces = #{}
                    local meshmod = Turn_to_Mesh() -- getting area with getArea() only works with mesh, not poly 
                    addModifier obj meshmod
                    uvwmod = Unwrap_UVW()
                    addModifier obj uvwmod
                    uvwmod.setMapChannel map_channel_
                    uvwmod.setConstantUpdate false
                    uvwmod.setShowSelectedVertices false
                    uvwmod.updateView()
                    uvwmod.edit()
                    uvwmod.setTVSubObjectMode 3 -- set the sub object mode 0 - None, 1 - Vertex, 2 - Edge, 3 - Face
    
                    local polycount = uvwmod.numberPolygons()
                    for f = 1 to polycount do
                    (
                        uvwmod.getArea #{f} &x &y &width &height &areaUVW &areaGeom
                        if (width < 0.0001 or height < 0.0001 or areaUVW < 0.0001) and areaGeom > 0.01 do
                        (
                            append error_faces f
                            format "error faces % \n" f
                        )
                    )--for
                    
                    if error_faces.count > 0 then
                    (
                        local resume_process = true
                        if not isDo_ignore_errors then resume_process = queryBox "Errors in UVWs! Do you want to continue? Press \"No\" to stop the process and check the problematic faces selected in an Unwrap Modifier. Click \"Yes\" to resume anyway, with the risk of a bad result."
                        if not resume_process then
                        (
                            -- from the workaround
                            addmodifier real_obj meshmod
                            addmodifier real_obj uvwmod
                            unhide real_obj
                            select real_obj
                            
                            uvwmod.selectFaces error_faces
                            uvwmod.edit()
                            uvwmod.setTVSubObjectMode 3 -- set the sub object mode 0 - None, 1 - Vertex, 2 - Edge, 3 - Face
                            if isDo_msgs_ do format "Stopped because of % errors in %!\n" error_faces.count real_obj.name
                            delete obj
                            return -1
                        )--if
                        if isDo_msgs_ do format "Probably % errors in mesh(!) of %, i.e. those map faces are too small/thin!\n" error_faces.count real_obj.name
                    )--if
                
                    deleteModifier obj uvwmod
                    deleteModifier obj meshmod
                )--if not is_UVmapped do
            )--if isDo_slicing_ do
            
            -- messageBox "after : if isDo_slicing_"
            
            ------------------------
            ------------------------
            -- First step: analyze the model and save the slice planes in an array
            ------------------------
            print "analyze the model and save the slice planes in an array"
            
            setCommandPanelTaskMode #create
            windows.processPostedMessages() -- jintaeks on ¿ÀÀü 11:42 2013-11-14

            if (isDo_slicing_ or isDo_force_padding_) and not is_UVmapped then
            (
                local faces_cutplanes_count = 0
                local textures_used = 0
                if isDo_msgs_ do format "... analyzing %'s uvs and geometry ...\n" real_obj.name
                
                for f = 1 to facecount do with undo isDo_undo_
                (
                    -- it's likely that we need some sliceplanes for some faces
                    faces_cutplanes[f] = #()

                    local act_edges = (polyop.getFaceEdges obj f)                    
                    if act_edges != undefined do
                    (
                        local edgecount = act_edges.count
                        
                        edge_cutpoints_x = #() -- count is same as edgecount at the end
                        edge_cutpoints_y = #()
                        
                        local is_mirrored = tag_checkMirror obj map_channel_ f
                        
                        -- build two tables: one with so called x-points, the other one with y-points
                        -- e.g. x-points are all at texture uv with y = ...,-1.0,0.0,1.0,2.0,...
                        -- so I have to save the min value (e.g. -1.0), in min_y
                        --
                        -- it has to be guaranteed that the table with the x-points
                        -- will be filled correctly (no gaps), so find the right pos (e.g. [3] for 1.0)
                        
                        -- find the minimum texture coords        
                        local absminx = 1000000
                        local absminy = 1000000
                        
                        for i in act_edges do with undo isDo_undo_
                        (
                            local vertices = (tag_getEdgeVerts obj f i)
                
                            local tv1 = (tag_getMapVert obj map_channel_ f vertices[1])
                            local tv2 = (tag_getMapVert obj map_channel_ f vertices[2])
                            
                            local minx = if tv1.x < tv2.x then tv1.x else tv2.x
                            local miny = if tv1.y < tv2.y then tv1.y else tv2.y
                            
                            absminx = if absminx < minx then absminx else minx
                            absminy = if absminy < miny then absminy else miny
                        )--for
                        
                        absminx = (ceil(absminx)) as integer
                        absminy = (ceil(absminy)) as integer
                        
                        -- save cutting points for every edge
                        -- those cutting points are found at every x/y-axis of texture uvs
                        for i in act_edges do with undo isDo_undo_
                        (
                            local vertices = (tag_getEdgeVerts obj f i)
                            
                            local tv1 = (tag_getMapVert obj map_channel_ f vertices[1])
                            local tv2 = (tag_getMapVert obj map_channel_ f vertices[2])
                            tv1 = [tv1.x, tv1.y] -- convert to Point2
                            tv2 = [tv2.x, tv2.y]
                            local dir = tv2-tv1
                            
                            local minx = if tv1.x < tv2.x then tv1.x else tv2.x
                            local maxx = if tv1.x >= tv2.x then tv1.x else tv2.x
                            local miny = if tv1.y < tv2.y then tv1.y else tv2.y
                            local maxy = if tv1.y >= tv2.y then tv1.y else tv2.y
                            
                            -- the x-axes ( ... -2, -1, 0, 1, ...)
                            local tempx = (ceil(minx)) as float
                            while tempx < ceil(maxx) do
                            (
                                local new_percent = (tempx-tv1.x)/dir.x
                                local new_vect = dir*new_percent
                                
                                -- get the cutpoint in 3d space
                                local new_dir = (tag_getVertexWorld obj vertices[2]) - (tag_getVertexWorld obj vertices[1])
                                local new_point = (tag_getVertexWorld obj vertices[1]) + (new_dir*new_percent)
                                
                                if edge_cutpoints_x[tempx-absminx+1] == undefined do
                                    edge_cutpoints_x[tempx-absminx+1] = #()
                                    
                                append edge_cutpoints_x[tempx-absminx+1] #(i, new_point, tv1.y + new_vect.y, tempx) -- edgenumber, point, texcoords
                                    
                                tempx += 1
                            )--while
                            
                            -- the y-axes ( ... -2, -1, 0, 1, ...)            
                            local tempy = (ceil(miny)) as integer
                            while tempy < ceil(maxy) do with undo isDo_undo_
                            (
                                local new_percent = (tempy-tv1.y)/dir.y
                                local new_vect = dir*new_percent
                                
                                -- get the cutpoint in 3d space
                                local new_dir = (tag_getVertexWorld obj vertices[2]) - (tag_getVertexWorld obj vertices[1])
                                local new_point = (tag_getVertexWorld obj vertices[1]) + (new_dir*new_percent)
                                
                                if edge_cutpoints_y[tempy-absminy+1] == undefined do
                                    edge_cutpoints_y[tempy-absminy+1] = #()
                
                                append edge_cutpoints_y[tempy-absminy+1] #(i, new_point, tv1.x + new_vect.x, tempy) -- edgenumber, coord, texcoords
                                
                                tempy += 1
                            )--while
                        )--for i in act_edges do with undo isDo_undo_
                        
                        -- get the points, get their position in 3d-space, build a sliceplane
                        -- we have to check if edges cross (they shouldn't)
                        -- first: for y
                        for i = 1 to edge_cutpoints_y.count do with undo isDo_undo_
                        (
                            local allpoints = deepCopy edge_cutpoints_y[i]
                            local points = edge_cutpoints_y[i]
                            local act_point_i = 0
                            
                            while points.count > 1 do
                            (
                                act_point_i += 1
                                local act_edge = copy points[1][1]
                                local act_point = copy points[1][2]
                                local act_TC = copy points[1][3]
                                local act_TC2 = copy points[1][4]
                                
                                -- get the first point (the active one) out of the list
                                deleteItem points 1
                                        
                                -- and test it against every other point on the same "line"
                                for other_points_i = 1 to points.count do with undo isDo_undo_
                                (
                                    local other_edge = points[other_points_i][1]
                                    local other_point = points[other_points_i][2]
                                    local other_TC = copy points[other_points_i][3]
                                    
                                    -- find out if other edges are crossing
                                    local is_near = true
                                    for test_points_i = 1 to allpoints.count while is_near do
                                    (
                                        if test_points_i != act_point_i and test_points_i != (act_point_i+other_points_i) do
                                        (
                                            local test_TC = allpoints[test_points_i][3]
                                            if act_TC < other_TC then
                                                if test_TC >= act_TC and test_TC <= other_TC do is_near = false
                                            else
                                                if test_TC <= act_TC and test_TC >= other_TC do is_near = false
                                        )
                                    )
                                    if is_near do
                                    (                
                                        -- angle between edges ...
                                        local verta = tag_getEdgeVerts obj f act_edge
                                        local verto = tag_getEdgeVerts obj f other_edge
                                
                                        local tva1 = (tag_getMapVert obj map_channel_ f verta[1])
                                        local tva2 = (tag_getMapVert obj map_channel_ f verta[2])
                                        local tvo1 = (tag_getMapVert obj map_channel_ f verto[1])
                                        local tvo2 = (tag_getMapVert obj map_channel_ f verto[2])
                    
                                        -- which one is on the left?
                                        local going_on = true
                                        if not is_mirrored then
                                        (
                                            if act_TC < other_TC then
                                                if (tva1.y <= tva2.y) do going_on = false
                                            else
                                                if (tvo1.y <= tvo2.y) do going_on = false
                                        )
                                        else
                                        (
                                            if act_TC < other_TC then
                                                if (tva1.y >= tva2.y) do going_on = false
                                            else
                                                if (tvo1.y >= tvo2.y) do going_on = false
                                        )--if.. else..
                                        
                                        if going_on do
                                        (
                                            local plane_normal = cross (polyop.getFaceNormal obj f) (other_point-act_point)
                                            plane_normal = normalize plane_normal
                                                                
                                            append faces_cutplanes[f] #(act_point, plane_normal, false, act_TC2) -- center, normal, is-x-axis, which axis
                                            faces_cutplanes_count += 1
                                        )--if
                                    )--if
                                )--for other_points_i = 1 to points.count do with undo isDo_undo_
                            )--while points.count > 1 do
                        )--for i = 1 to edge_cutpoints_y.count do with undo isDo_undo_
                        
                        -- the same for x
                        for i = 1 to edge_cutpoints_x.count do with undo isDo_undo_
                        (
                            local allpoints = deepCopy edge_cutpoints_x[i]
                            local points = edge_cutpoints_x[i]
                            local act_point_i = 0
                            
                            while points.count > 1 do
                            (
                                act_point_i += 1
                                local act_edge = copy points[1][1]
                                local act_point = copy points[1][2]
                                local act_TC = copy points[1][3]
                                local act_TC2 = copy points[1][4]
                                
                                -- get the first point (the active one) out of the list
                                deleteItem points 1
                                        
                                -- and test it against every other point on the same "line"
                                for other_points_i = 1 to points.count do with undo isDo_undo_
                                (
                                    local other_edge = points[other_points_i][1]
                                    local other_point = points[other_points_i][2]
                                    local other_TC = points[other_points_i][3]
                                    
                                    -- find out if other edges are crossing
                                    local is_near = true
                                    for test_points_i = 1 to allpoints.count while is_near do
                                    (
                                        if test_points_i != act_point_i and test_points_i != (act_point_i+other_points_i) do
                                        (
                                            local test_TC = allpoints[test_points_i][3]
                                            if act_TC < other_TC then
                                                if test_TC >= act_TC and test_TC <= other_TC do is_near = false
                                            else
                                                if test_TC <= act_TC and test_TC >= other_TC do is_near = false
                                        )
                                    )
                                    
                                    if is_near do
                                    (
                                        -- angle between edges ...
                                        local verta = tag_getEdgeVerts obj f act_edge
                                        local verto = tag_getEdgeVerts obj f other_edge
                                
                                        local tva1 = (tag_getMapVert obj map_channel_ f verta[1])
                                        local tva2 = (tag_getMapVert obj map_channel_ f verta[2])
                                        local tvo1 = (tag_getMapVert obj map_channel_ f verto[1])
                                        local tvo2 = (tag_getMapVert obj map_channel_ f verto[2])
                    
                                        -- which one is on the left?
                                        local going_on = true
                                        if not is_mirrored then
                                        (
                                            if act_TC < other_TC then
                                                if (tva1.x >= tva2.x) do going_on = false
                                            else
                                                if (tvo1.x >= tvo2.x) do going_on = false
                                        )
                                        else
                                        (
                                            if act_TC < other_TC then
                                                if (tva1.x <= tva2.x) do going_on = false
                                            else
                                                if (tvo1.x <= tvo2.x) do going_on = false
                                        )--if.. else..
                            
                                        if going_on do
                                        (
                                            local plane_normal = cross (polyop.getFaceNormal obj f) (other_point-act_point)
                                            plane_normal = normalize plane_normal
                                            
                                            append faces_cutplanes[f] #(act_point, plane_normal, true, act_TC2) -- center, normal, is-x-axis, which axis
                                            faces_cutplanes_count += 1
                                        )--if
                                    )--if
                                )--for other_points_i = 1 to points.count do with undo isDo_undo_
                            )--while points.count > 1 do
                        )--for i = 1 to edge_cutpoints_x.count do with undo isDo_undo_
                
                        if (classOf real_obj.material) == Multimaterial do
                        (
                            -- count materials, for later use
                            local real_mat_id = obj.GetFaceMaterial f
                            local id_in_mmat = findItem real_obj.material.materialIDList real_mat_id
                            
                            -- format "debug : material_info[%].mats_in_multi_used[%]\n" o id_in_mmat
                            -- @note 'id_in_mmat' can be 0, when material is invalid. jintaeks on ¿ÀÀü 10:04 2013-12-04
                            -- wasn't the material saved before?
                            if id_in_mmat >= 1 and material_info[o].mats_in_multi_used[id_in_mmat] == false do
                            (
                                material_info[o].mats_in_multi_used[id_in_mmat] = true
                                append material_info[o].mmat_ids id_in_mmat
                                local tex_id
                                try
                                (
                                    tex_id = findItem textures real_obj.material.materialList[id_in_mmat].diffuseMap.filename
                                )
                                catch
                                (
                                    -- from the workaround
                                    select real_obj
                                    unhide real_obj
                                    delete obj

                                    messagebox "Error in materials! Are you really using multi and standard materials only?"
                                    return -1
                                )--try.. catch..
                                if tex_id == 0 then
                                (
                                    append textures real_obj.material.materialList[id_in_mmat].diffuseMap.filename
                                    -- append material name. jintaeks on ¿ÀÈÄ 12:06 2013-11-18
                                    append materialNames real_obj.material.materialList[id_in_mmat].name
                                    print real_obj.material.names[id_in_mmat]
                                    material_info[o].mmatid_to_texid[id_in_mmat] = textures.count
                                    textures_used += 1
                                )
                                else
                                (
                                    material_info[o].mmatid_to_texid[id_in_mmat] = tex_id
                                )--if.. else..
                                
                                material_info[o].num_materials_used += 1
                            )--if material_info[o].mats_in_multi_used[id_in_mmat] == false do
                        )--if (classOf real_obj.material) == Multimaterial do
                    )--if act_edges != undefined do
                )--for f = 1 to facecount do with undo isDo_undo_

                if (classOf real_obj.material) == Multimaterial and isDo_msgs_ do format "...... found % materials with % new textures\n" material_info[o].num_materials_used textures_used         
                if isDo_msgs_ do format "...... % slice planes need to be generated\n" faces_cutplanes_count
                
                obj.preserveUVs = true
         
            )
            else -- if not isDo_slicing_ or is_UVmapped then
            (
                if (classOf real_obj.material) == Multimaterial do
                (
                    local textures_used = 0
                    
                    for f = 1 to facecount do with undo isDo_undo_
                    (
                        -- count materials, for later use
                        local real_mat_id = obj.GetFaceMaterial f
                        local id_in_mmat = findItem real_obj.material.materialIDList real_mat_id
                        
                        if id_in_mmat == 0 do
                        (
                            -- from the workaround
                            select real_obj
                            unhide real_obj
                            delete obj
                            
                            messagebox "Multimaterial or object with multimaterial has errors!"
                            format "Error: Material ID not found!\n"
                            return -1
                        )--if
                        
                        -- wasn't the material saved before?
                        if material_info[o].mats_in_multi_used[id_in_mmat] == false do
                        (
                            material_info[o].mats_in_multi_used[id_in_mmat] = true
                            append material_info[o].mmat_ids id_in_mmat
                            local tex_id
                            try
                            (
                                tex_id = findItem textures real_obj.material.materialList[id_in_mmat].diffuseMap.filename
                            )
                            catch
                            (
                                -- from the workaround
                                select real_obj
                                unhide real_obj
                                delete obj

                                messagebox "Error in materials! Are you really using multi and standard materials with bitmaps only?"
                                return -1
                            )--try.. catch..

                            if tex_id == 0 then
                            (
                                append textures real_obj.material.materialList[id_in_mmat].diffuseMap.filename
                                -- append material name. jintaeks on ¿ÀÈÄ 12:07 2013-11-18
                                append materialNames real_obj.material.materialList[id_in_mmat].name
                                print real_obj.material.names[id_in_mmat]
                                material_info[o].mmatid_to_texid[id_in_mmat] = textures.count
                                textures_used += 1
                            )
                            else
                            (
                                material_info[o].mmatid_to_texid[id_in_mmat] = tex_id
                            )--if.. else..
                            
                            material_info[o].num_materials_used += 1
                        )--if material_info[o].mats_in_multi_used[id_in_mmat] == false do
                    )--for f = 1 to facecount do with undo isDo_undo_

                    if isDo_msgs_ do format "...... % has % materials with % new textures\n" real_obj.name material_info[o].num_materials_used textures_used
                )--if (classOf real_obj.material) == Multimaterial do
            )--if.. else..
            
            if (classOf real_obj.material) == Standardmaterial do
            (
                material_info[o].mats_in_multi_used[1] = true
                material_info[o].mmat_ids[1] = 1
                local tex_id
                try
                (
                    tex_id = findItem textures real_obj.material.diffuseMap.filename
                )
                catch
                (
                    if isDo_slicing_ or isDo_force_padding_ do
                    (
                        select real_obj
                        unhide real_obj
                        delete obj
                    )
                    messagebox "Error in materials! Are you really using multi and standard materials with bitmaps only?"
                    return -1
                )--try.. catch..

                if tex_id == 0 then
                (
                    append textures real_obj.material.diffuseMap.filename
                    -- append material name. jintaeks on ¿ÀÈÄ 12:08 2013-11-18
                    append materialNames real_obj.material.name
                    print real_obj.material.names[id_in_mmat]
                    material_info[o].mmatid_to_texid[1] = textures.count
                    if isDo_msgs_ do format "...... % has only one material with a new texture\n" real_obj.name
                )
                else
                (
                    material_info[o].mmatid_to_texid[1] = tex_id
                    if isDo_msgs_ do format "...... % has only one material with no new texture\n" real_obj.name
                )--if.. else..
                    
                material_info[o].num_materials_used = 1
            )--if (classOf real_obj.material) == Standardmaterial do
            
            ----------------------------
            ----------------------------
            -- Second step: slice the geometry.
            ----------------------------
            print "slice the geometry"

            if isDo_slicing_ and not is_UVmapped do
            (
                if isDo_msgs_ do format "... %: slicing geometry\n" real_obj.name

                -- progress bar update related variables. jintaeks on ¿ÀÀü 11:40 2013-11-14
                local iProgressUpdateStep = facecount / 100
                local iProgressUpdateCounter = 0

                -- the slicing begins
                for f = 1 to facecount do with undo isDo_undo_
                (
                    -- update progress bar. jintaeks on ¿ÀÀü 11:27 2013-11-14
                    iProgressUpdateCounter += 1
                    if iProgressUpdateCounter >= iProgressUpdateStep then
                    (
                        iProgressUpdateCounter = 0
                        progBar_.value = ( f as float / facecount ) * 100
                        windows.processPostedMessages()
                    )--if

                    -- get the material and look if it's cutted ... to find out uvmaps, y'know?
                    if faces_cutplanes[f].count > 0 then
                    (
                        local old_edgecount = obj.edges.count
                        
                        setFaceSelection obj #(f)
                
                        local act_verts = obj.numVerts
                        
                        for i = 1 to faces_cutplanes[f].count do with undo isDo_undo_
                        (
                            local active_faces = getFaceSelection obj
                            local success = (tag_slice obj active_faces faces_cutplanes[f][i][2] faces_cutplanes[f][i][1])
                            
                            if success == false do
                            (
                                local going_on = true
                                if not isDo_ignore_errors do going_on = querybox "A specific face couldn't be sliced, which will result in a incorrect UV map.\nCheck your UVs and Geometry, please. Continue anyway?"
                                if not going_on do
                                (
                                    -- from the workaround
                                    delete obj
                                    select real_obj
                                    obj = real_obj
                                
                                    uvwmod = Unwrap_UVW()
                                    addModifier obj uvwmod
                                    uvwmod.setMapChannel map_channel_
                                    uvwmod.updateView()
                                    uvwmod.selectFaces active_faces
                                    uvwmod.edit()
                                    uvwmod.setTVSubObjectMode 3 -- set the sub object mode 0 - None, 1 - Vertex, 2 - Edge, 3 - Face
                                    return -1
                                )
                            )
                                
                            local xaxis = faces_cutplanes[f][i][3]
                            local tc_val = faces_cutplanes[f][i][4]
                            
                            for j = act_verts+1 to obj.numVerts do with undo isDo_undo_
                            (
                                local tv = (tag_getMapVert obj map_channel_ (getFaceSelection obj) j)
                                if xaxis then tv.x = tc_val else tv.y = tc_val
                                tag_setMapVert obj map_channel_ (getFaceSelection obj) j tv
                            )--for
                            
                            act_verts = obj.numVerts
                        )--for i = 1 to faces_cutplanes[f].count do with undo isDo_undo_
                    )--if faces_cutplanes[f].count > 0 then
                )--for f = 1 to facecount do with undo isDo_undo_
            )--if isDo_slicing_ and not is_UVmapped do

            --------------------------
            --------------------------
            -- Intermission! Check if materials are cutted ...
            --------------------------
            print "Check if materials are cutted"

            setCommandPanelTaskMode #modify
            windows.processPostedMessages() -- jintaeks on ¿ÀÀü 11:42 2013-11-14

            if isDo_slicing_ or (isDo_generate_ta_ and isDo_force_padding_) do
            (
                select obj
                uvwmod = Unwrap_UVW()
                addModifier obj uvwmod
                uvwmod.setMapChannel map_channel_
                uvwmod.updateView()
                uvwmod.setResetPivotOnSelection true
                uvwmod.setTVSubObjectMode 3 -- set the sub object mode 0 - None, 1 - Vertex, 2 - Edge, 3 - Face
                
                if (classOf real_obj.material) == Multimaterial then
                (
                    local x, y, width, height, temp
                    -- iterate through all material ids to check if they need padding
                    for i = 1 to material_info[o].num_materials_used do with undo isDo_undo_
                    (
                        local bmp_id = material_info[o].mmatid_to_texid[material_info[o].mmat_ids[i]]
                        if not cutted_textures[bmp_id] do
                        (
                            uvwmod.selectByMatID material_info[o].mmat_ids[i]
                            uvwmod.getArea (uvwmod.getSelectedPolygons()) &x &y &width &height &temp &temp
                            if not (((x >= 0.001) and (x+width <= 0.999) and (y >= 0.001) and (y+height <= 0.999))) do
                            (
                                cutted_textures[bmp_id] = true
                            )--if
                        )--if
                    )--for
                )
                else
                (
                    local x, y, width, height, temp
                    uvwmod.getArea #{1..facecount} &x &y &width &height &areaUVW &areaGeom
                    if not (((x >= 0.001) and (x+width <= 0.999) and (y >= 0.001) and (y+height <= 0.999))) do
                    (
                        cutted_textures[material_info[o].mmatid_to_texid[1]] = true
                    )--if
                )--if.. else..
                        
                deleteModifier obj uvwmod
                windows.processPostedMessages() -- jintaeks on ¿ÀÀü 11:42 2013-11-14
            )--if isDo_slicing_ or (isDo_generate_ta_ and isDo_force_padding_) do
            
            --------------------------
            --------------------------
            -- Third step: "normalize" the texture coords, i.e. break and move all chunks into the range 0.0..1.0
            --------------------------
            print "normalize the texture coords"
            
            if isDo_slicing_ and not is_UVmapped do
            (
                select obj
                uvwmod = Unwrap_UVW()
                addModifier obj uvwmod
                uvwmod.setMapChannel map_channel_
                uvwmod.updateView()
                uvwmod.setResetPivotOnSelection true
                -- uvwmod.setConstantUpdate false
                uvwmod.setShowSelectedVertices false
                uvwmod.edit()
                windows.processPostedMessages() -- jintaeks on ¿ÀÀü 11:42 2013-11-14
                uvwmod.setTVSubObjectMode 1 -- set the sub object mode 0 - None, 1 - Vertex, 2 - Edge, 3 - Face
                uvwmod.selectVertices #{1..uvwmod.numberVertices()}
                uvwmod.vertToEdgeSelect()
                local num_tedges = (uvwmod.getSelectedEdges()).count
                -- if num_tedges > 1000 then
                -- (
                    -- num_tedges = 1000
                -- )--if

                if isDo_break_all_ then
                (
                    uvwmod.setTVSubObjectMode 2
                    if isDo_msgs_ do format "... %: normalizing tex coords, breaking all % edges\n" real_obj.name num_tedges
                    uvwmod.breakSelected()
                )
                else
                (
                    if isDo_msgs_ do format "... %: normalizing tex coords, analyzing % edges ...\n" real_obj.name num_tedges    
                    uvwmod.selectVertices #{}
                    uvwmod.setTVSubObjectMode 2
                    windows.processPostedMessages() -- jintaeks on ¿ÀÀü 11:42 2013-11-14

                    local edges_to_break = #{}
                    edges_to_break[num_tedges] = false

                    local vert_indices
                    local vert1
                    local vert2
                    -- local uvwmod_selectedges = uvwmod.selectEdges
                    -- local uvwmod_edgetovertselect = uvwmod.edgeToVertSelect
                    -- local uvwmod_getselectedvertices = uvwmod.getSelectedVertices
                    -- local uvwmod_getvertexposition = uvwmod.getVertexPosition

                    -- find the edges to break
                    -- this little piece of code is the (extreme) bottleneck in big meshes ...
                    local start = timeStamp()
                    -- progress bar update related variables. jintaeks on ¿ÀÀü 11:40 2013-11-14
                    local iProgressUpdateStep = num_tedges / 100
                    local iProgressUpdateCounter = 0

                    for i = 1 to num_tedges do with undo isDo_undo_
                    (
                        -- update progress bar. jintaeks on ¿ÀÀü 11:27 2013-11-14
                        iProgressUpdateCounter += 1
                        if iProgressUpdateCounter >= iProgressUpdateStep then
                        (
                            iProgressUpdateCounter = 0
                            progBar_.value = ( i as float / num_tedges ) * 100
                            
                            local ss = stringStream ""
                            format "progress %(%/%)" progBar_.value i num_tedges to:ss
                            --messagebox (ss as string)
                            print ( ss as string )

                            windows.processPostedMessages()
                        )--if
                    
                        uvwmod.selectEdges #{i}
                        uvwmod.edgeToVertSelect()
                        local vert_indices = uvwmod.getSelectedVertices() as Array
                        if vert_indices.count >= 2 then -- jintaeks on ¿ÀÈÄ 5:38 2013-11-25
                        (
                            vert1 = (uvwmod.getVertexPosition 0 vert_indices[1])
                            vert2 = (uvwmod.getVertexPosition 0 vert_indices[2])
                            if (tag_equal_int (floor (vert1.x+0.5)) vert1.x) and (tag_equal_int vert1.x vert2.x) then
                            (
                                edges_to_break[i] = true
                            )
                            else if (tag_equal_int (floor (vert1.y+0.5)) vert1.y) and (tag_equal_int vert1.y vert2.y) then
                            (
                                edges_to_break[i] = true
                            )--if.. else if..
                        )--if
                        
                        if m_bIsCancelProcess do break
                    )--for
                    progBar_.value = 100
                    windows.processPostedMessages()
                    local end = timeStamp()
                    
                    local ss = stringStream ""
                    format "break % edges..." edges_to_break.count to:ss
                    print ( ss as string )
                    if edges_to_break.count >= 1 then
                    (
                        uvwmod.selectEdges edges_to_break
                        print "breakSelected..."
                        -- stuck problem on 'breakSelected'. jintaeks on ¿ÀÀü 9:46 2013-11-26
                        uvwmod.breakSelected()
                    )--if
                    
                    if isDo_msgs_ do format "...... broke % of % texture edges in % secs\n" edges_to_break.numberSet num_tedges ((end - start)/1000)
                )--if.. else..

                print "convertTo PolyMeshObject"
                convertTo obj PolyMeshObject
                -- maxOps.CollapseNodeTo obj 1 off
                
                uvwmod = Unwrap_UVW()
                addModifier obj uvwmod
                windows.processPostedMessages() -- jintaeks on ¿ÀÀü 11:42 2013-11-14
                uvwmod.setMapChannel map_channel_
                uvwmod.setResetPivotOnSelection true
                uvwmod.setConstantUpdate false
                uvwmod.setShowSelectedVertices false
                uvwmod.setTVSubObjectMode 3

                -- moving all the chunks
                local num_polys = uvwmod.numberPolygons()
                local x, y, temp
                if isDo_break_all_ then
                (
                    for i = 1 to num_polys do with undo isDo_undo_
                    (
                        uvwmod.selectFaces #{i}
                        local x_move = 0.0
                        local y_move = 0.0
                        uvwmod.getArea #{i} &x &y &temp &temp &temp &temp
                        while x < 0.0 do (x += 1.0; x_move += 1.0)
                        while x >= 0.999 do (x -= 1.0; x_move -= 1.0)
                        while y < 0.0 do (y += 1.0; y_move += 1.0)
                        while y >= 0.999 do (y -= 1.0; y_move -= 1.0)
                        uvwmod.moveSelected [x_move, y_move, 0.0]
                    )--for
                )
                else
                (
                    -- progress bar update related variables. jintaeks on ¢¯AAu 11:40 2013-11-14
                    local iProgressUpdateStep = num_polys / 100
                    local iProgressUpdateCounter = 0
                
                    local poly_is_edited = #{}
                    for i = 1 to num_polys do with undo isDo_undo_
                    (
                        -- update progress bar. jintaeks on ¿ÀÀü 11:27 2013-11-14
                        iProgressUpdateCounter += 1
                        if iProgressUpdateCounter >= iProgressUpdateStep then
                        (
                            iProgressUpdateCounter = 0
                            progBar_.value = ( i as float / num_polys ) * 100
                            windows.processPostedMessages()
                        )--if
                    
                        if not poly_is_edited[i] do
                        (                        
                            uvwmod.selectFaces #{i}
                            
                            local do_expand = true
                            local old_selected_number
                            local selected_polys = #{}
                            do
                            (
                                old_selected_number = (uvwmod.getSelectedPolygons()).numberSet
                                uvwmod.expandSelection()
                                selected_polys = uvwmod.getSelectedPolygons()
                                if selected_polys.numberSet == old_selected_number do do_expand = false
                            ) while do_expand
                            uvwmod.breakSelected() --- cleaning up - some vertices may have "survived" the breaking before
                            
                            join poly_is_edited selected_polys

                            local x_move = 0.0
                            local y_move = 0.0
                            uvwmod.getArea selected_polys &x &y &temp &temp &temp &temp
                            
                            while x < 0.0 do (x += 1.0; x_move += 1.0)
                            while x >= 0.999 do (x -= 1.0; x_move -= 1.0)
                            while y < 0.0 do (y += 1.0; y_move += 1.0)
                            while y >= 0.999 do (y -= 1.0; y_move -= 1.0)
                            
                            -- format "moveSelected % %\n" x_move y_move
                            -- qff. jintaeks on ¿ÀÈÄ 5:33 2013-11-29
                            -- big memory increase problem after 'uvwmod.moveSelected'
                            if false then
                            (
                                uvwmod.moveSelected [x_move, y_move, 0.0]
                            )
                            else
                            (
                                /** fixed big memory increase problem of 'uvwmod.moveSelected'
                                    - jintaeks on ¿ÀÈÄ 2:33 2013-12-03 */
                                uvwmod.faceToVertSelect()
                                local vertIndices = ( uvwmod.getSelectedVertices() ) as Array
                                local numIndices = vertIndices.count
                                -- local vertices = #()
                                local vertTemp = [0, 0, 0] as point3
                                
                                for vindex in vertIndices Do
                                (
                                    vertTemp = (uvwmod.getVertexPosition 0 vindex)
                                    vertTemp.x += x_move
                                    vertTemp.y += y_move
                                    --append vertices vertTemp
                                    uvwmod.setVertexPosition 0 vindex vertTemp
                                )--for
                            )--if.. else..
                        )--if
                        if m_bIsCancelProcess do break
                    )--for
                )--if.. else..
                
                convertTo obj PolyMeshObject
                -- maxOps.CollapseNodeTo obj 1 off
            )--if isDo_slicing_ and not is_UVmapped do
            
            if real_obj != obj do
            (
                -- continue the workaround, *sigh*
                real_obj.baseobject = obj.baseobject
                for geo in geometry do if geo.baseobject == save_obj then geo.baseobject = obj.baseobject
                delete obj
                unhide real_obj
            )--if
            progBar_.value = 100
            windows.processPostedMessages() -- jintaeks on ¿ÀÀü 11:42 2013-11-14
        )--for real_obj in tag_objs do with undo isDo_undo_
            
        if isDo_msgs_ and (isDo_slicing_ or isDo_generate_ta_) do format "TAG will make a texture atlas now.\n"

        --------------------------
        --------------------------
        -- Fourth step: rendering a texture atlas
        --------------------------
        
        /** @brief  load bitmaps_ from disk
            @param  bitmaps_ : [out] bitmaps loaded
            @param  textures : [in] texture filenames
            @param  num_textures : [in] number of textures
            @date   jintaeks on ¿ÀÈÄ 8:08 2013-11-14 */
        function LoadBitmaps &bitmaps_ textures num_textures materialNames_ cutted_textures isPadding_tresize_ padding_=
        (
            bitmaps_ = #()
            bitmaps_[num_textures] = undefined -- pre-size the array

            -- format "LoadBitmaps...\n"
            
            -- iterate through all material ids
            for i = 1 to num_textures do
            (
                -- prepare the textures
                sbmp = SBitmap()
                if textures[i] != undefined then
                (
                    try
                    (
                        sbmp.bmp = openBitmap textures[i]
                    )
                    catch
                    (
                        messagebox "One of the textures couldn't be found! (Probably wrong path.)\n Please select the correct one."
                        local new_bmp = getOpenFileName caption:"Select Texture" filename:textures[i]
                        if new_bmp == undefined then
                        (
                            format "Aborted texture packing!\nError: % wasn't found.\n" textures[i]
                            return -1
                        )
                        else
                        (
                            sbmp.bmp = openBitmap new_bmp
                        )--if.. else..
                    )--try.. catch..
                )
                else
                (
                    sbmp.bmp = bitmap 32 32
                )--if.. else..
                
                sbmp.filename = textures[i]
                -- set material name for this bitmap. jintaeks on ¿ÀÈÄ 12:02 2013-11-18
                sbmp.materialName = materialNames_[i]
                sbmp.width = sbmp.bmp.width
                sbmp.height = sbmp.bmp.height
                sbmp.is_cutted = cutted_textures[i]
                if sbmp.is_cutted do
                (
                    sbmp.width += if not isPadding_tresize_ then (2 * padding_) else 0
                    sbmp.height += if not isPadding_tresize_ then (2 * padding_) else 0
                )--if
                sbmp.area = sbmp.width * sbmp.height
                bitmaps_[i] = sbmp
                
                -- format "file = %\n" textures[i]
            )--for
        )--function LoadBitmaps &bitmaps_ textures num_textures =
        
        /** @brief  rearrange bitmaps using 'm_atlasInfo'
            @date   jintaeks on ¿ÀÈÄ 8:27 2013-11-14 */
        function RearrangeBitmapsUsingAtlasInfo &bitmaps_ =
        (
            for sbmp in bitmaps_ do
            (                    
                -- commented out. jintaeks on ¿ÀÈÄ 12:15 2013-11-18
                --local kMtrlInfo = m_atlasInfo.FindMaterialByContainingFilename sbmp.filename
                -- find material by it's material name. jintaeks on ¿ÀÈÄ 12:15 2013-11-18
                local kMtrlInfo = m_atlasInfo.FindMaterialByMaterialName sbmp.materialName
                if kMtrlInfo != undefined then
                (
                    sbmp.x = kMtrlInfo.m_iLeft
                    sbmp.y = kMtrlInfo.m_iTop
                    
                    if sbmp.width != kMtrlInfo.m_iWidth or sbmp.height != kMtrlInfo.m_iHeight then
                    (
                        local iNewWidth = kMtrlInfo.m_iWidth
                        local iNewHeight = kMtrlInfo.m_iHeight
                        if kMtrlInfo.m_bIsRotateCcw == true then
                        (
                            swap iNewWidth iNewHeight
                        )--if
                        
                        local b = bitmap iNewWidth iNewHeight
                        copy sbmp.bmp b
                        close sbmp.bmp
                        
                        sbmp.bmp = bitmap iNewWidth iNewHeight
                        copy b sbmp.bmp
                        close b

                        sbmp.width = iNewWidth
                        sbmp.height = iNewHeight
                    )--if
                    
                    -- set rotated flag. jintaeks on ¿ÀÀü 10:35 2013-11-19
                    sbmp.rotated = false
                    if kMtrlInfo.m_bIsRotateCcw == true then
                    (
                        --sbmp.Rotate()
                        sbmp.rotated = true
                    )--if
                )--if
            )--for
        )--function RearrangeBitmapsUsingAtlasInfo &bitmaps_
        
        function GetNewTextureFilenameUsingAtlasInfo &newTextures_ textures_ materialNames_ textureType_:#diffuse =
        (
            local numTextures = textures_.count
            newTextures_ = #()
            newTextures_[numTextures] = undefined
            for i = 1 to numTextures Do
            (
                -- commented out.
                -- this isn'e well works when there is duplicate files in several materials.
                -- jintaeks on ¿ÀÈÄ 12:10 2013-11-18
                --local kMtrlInfo = m_atlasInfo.FindMaterialByContainingFilename textures_[i]

                -- new method. fine material by it's material name. jintaeks on ¿ÀÈÄ 12:11 2013-11-18
                local kMtrlInfo = m_atlasInfo.FindMaterialByMaterialName materialNames_[i]

                if kMtrlInfo != undefined then
                (
                    if textureType_ == #diffuse then
                        newTextures_[i] = kMtrlInfo.m_strDiffuse
                    else if textureType_ == #bump then
                        newTextures_[i] = kMtrlInfo.m_strBump
                    else if textureType_ == #specular then
                        newTextures_[i] = kMtrlInfo.m_strSpecular
                    else if textureType_ == #glossiness then
                        newTextures_[i] = kMtrlInfo.m_strGlossiness
                )
                else
                (
                    newTextures_[i] = undefined -- textures_[i]
                )--if.. else..
            )--for
        )--function GetNewTextureFilenameUsingAtlasInfo &newTextures textures
        
        local area_of_all_textures = 0    
        local num_textures = textures.count 
        -- local bitmaps = #()
        -- bitmaps[num_textures] = undefined -- pre-size the array
        
        --if m_bIsCancelProcess do return
        print "fill bitmaps to atlas"
        
        if isDo_slicing_ or isDo_generate_ta_ do
        (
            if isDo_msgs_ and isDo_generate_ta_ do format "Packing % textures\n" num_textures
        
            -- load bitmaps from disk. jintaeks on ¿ÀÈÄ 8:10 2013-11-14
            LoadBitmaps &m_bitmaps textures num_textures materialNames cutted_textures isPadding_tresize_ padding_

            -- calc area of all textures.
            for sbmp in m_bitmaps Do
            (
                area_of_all_textures += sbmp.area
            )--for
            
            -- sort the textures, biggest first
            function compareSBMP v1 v2 =
            (
                if v1.area < v2.area then 1
                else if v1.area == v2.area then 0
                else -1
            )--function compareSBMP v1 v2 =
            
            -- get the size of the texture atlas
            local size_of_texatlas_x = (sqrt area_of_all_textures)
            local size_of_texatlas_y
            local i = 0
            while size_of_texatlas_x > 0 do
            (
                size_of_texatlas_x = bit.shift size_of_texatlas_x -1
                i += 1
            )--while
            size_of_texatlas_y = size_of_texatlas_x = bit.shift 1 (i-1)
            
            -- jintaeks on ¿ÀÈÄ 5:19 2013-11-13. seojtdoc
            -- replace atlas size with atlas manager's info. jintaeks on ¿ÀÈÄ 5:37 2013-11-13
            if m_bIsUseExternalAtlasManager == true then
            (
                size_of_texatlas_x = m_atlasInfo.m_iAtlasWidth
                size_of_texatlas_y = m_atlasInfo.m_iAtlasHeight
            )--if
        
            -- manage the trunks and the textures
            function add_to_trunk trunks_array trunk_index bitmaps_array bitmap_index =
            (
                -- bitmap fits exactly:
                if bitmaps_array[bitmap_index].width == trunks_array[trunk_index][3] and bitmaps_array[bitmap_index].height == trunks_array[trunk_index][4] then
                (
                    bitmaps_array[bitmap_index].x = trunks_array[trunk_index][1]
                    bitmaps_array[bitmap_index].y = trunks_array[trunk_index][2]
                    deleteItem bitmaps_array bitmap_index
                    deleteItem trunks_array trunk_index
                )
                else -- it's smaller
                (
                    bitmaps_array[bitmap_index].x = trunks_array[trunk_index][1]
                    bitmaps_array[bitmap_index].y = trunks_array[trunk_index][2]
                    
                    -- create a new trunk
                    append trunks_array #( trunks_array[trunk_index][1]+bitmaps_array[bitmap_index].width,
                                           trunks_array[trunk_index][2],
                                           trunks_array[trunk_index][3]-bitmaps_array[bitmap_index].width,
                                           bitmaps_array[bitmap_index].height)
                    -- make the old one smaller
                    trunks_array[trunk_index][2] += bitmaps_array[bitmap_index].height
                    trunks_array[trunk_index][4] -= bitmaps_array[bitmap_index].height
        
                    deleteItem bitmaps_array bitmap_index
                )--if.. else..
                
                -- sort the trunks
                function compareTRUNKS v1 v2 =
                (
                    if v1[3]*v1[4] > v2[3]*v2[4] then  1
                    else if v1[3]*v1[4] == v2[3]*v2[4] then 0
                    else -1
                )--function compareTRUNKS v1 v2 =
                qsort trunks_array compareTRUNKS
            )--function add_to_trunk trunks_array trunk_index bitmaps_array bitmap_index =
            
            -- use external atlas info manager when specified. jintaeks ¿ÀÈÄ 7:58 2013-11-13
            if m_bIsUseExternalAtlasManager == true then
            (
                -- replace bitmap position and size with atlas managers's info. jintaeks on ¿ÀÈÄ 5:37 2013-11-13
                RearrangeBitmapsUsingAtlasInfo &m_bitmaps
            )
            else -- fill the texture atlas, virtually
            (
                local act_trk = 1
                local done_packing
                local resize_switch = true
                do with undo isDo_undo_ -- the packing
                (
                    local free_trunks = #(#(0, 0, size_of_texatlas_x, size_of_texatlas_y)) -- x,y,w,h
                    local rest_bitmaps = copy m_bitmaps #noMap
                    qsort rest_bitmaps compareSBMP
                
                    while true do
                    (
                        if rest_bitmaps.count == 0 do
                        (
                            done_packing = true
                            exit
                        )--if
                        if free_trunks.count == 0 do
                        (
                            -- texture too small ...
                            done_packing = false
                            exit
                        )--if
                
                        local found_fitting_bitmap = false
                        for act_bmp = 1 to rest_bitmaps.count while not found_fitting_bitmap do
                        (
                            -- get the smallest trunk & the biggest texture which fit
                            if rest_bitmaps[act_bmp].width <= free_trunks[act_trk][3] and rest_bitmaps[act_bmp].height <= free_trunks[act_trk][4] then
                            (
                                add_to_trunk free_trunks act_trk rest_bitmaps act_bmp
                                found_fitting_bitmap = true
                            )
                            else if rest_bitmaps[act_bmp].width <= free_trunks[act_trk][4] and rest_bitmaps[act_bmp].height <= free_trunks[act_trk][3] then
                            (
                                rest_bitmaps[act_bmp].Rotate()
                                add_to_trunk free_trunks act_trk rest_bitmaps act_bmp
                                found_fitting_bitmap = true
                            )--if.. else if..
                        )--for
                        
                        -- the trunk is too small (or slim) for any remaining texture
                        if not found_fitting_bitmap do
                        (
                            deleteItem free_trunks act_trk
                        )--if
                    )--while
                    
                    if not done_packing do -- resize the tex texture
                    (
                         if resize_switch then size_of_texatlas_y = 2*size_of_texatlas_y
                         else size_of_texatlas_x = 2*size_of_texatlas_x
                            
                         resize_switch = not resize_switch
                         
                         for sbmp in m_bitmaps where sbmp.rotated do sbmp.Rotate()
                    )--if
                ) while done_packing == false
            )--if.. else..
        )--if isDo_slicing_ or isDo_generate_ta_ do
        
        local texture_atlasBump = undefined
        local texture_atlasSpecular = undefined
        local texture_atlasGlossiness = undefined

        --if m_bIsCancelProcess do return
        print "generating atlas"
        
        if isDo_generate_ta_ do
        (    
            _GenerateAtlasTexture &texture_atlas texture_atlas_filename_ \
                size_of_texatlas_x size_of_texatlas_y &m_bitmaps \
                isDo_msgs_ isDo_undo_ padding_ isPadding_tresize_

            if m_atlasInfo.IsBump() then
            (
                local strPath = getFilenamePath texture_atlas_filename_
                local strFileNameOnly = getFilenameFile texture_atlas_filename_
                local strFileExt = getFilenameType texture_atlas_filename_
                local strNewTextureAtlasFilename = strPath + strFileNameOnly + "_N" + strFileExt
                local newTextures
                GetNewTextureFilenameUsingAtlasInfo &newTextures textures materialNames textureType_:#bump
                LoadBitmaps &m_bitmaps newTextures num_textures materialNames cutted_textures isPadding_tresize_ padding_
                RearrangeBitmapsUsingAtlasInfo &m_bitmaps

                _GenerateAtlasTexture &texture_atlasBump strNewTextureAtlasFilename \
                    size_of_texatlas_x size_of_texatlas_y &m_bitmaps \
                    isDo_msgs_ isDo_undo_ padding_ isPadding_tresize_
            )--if

            if m_atlasInfo.IsSpecular() then
            (
                local strPath = getFilenamePath texture_atlas_filename_
                local strFileNameOnly = getFilenameFile texture_atlas_filename_
                local strFileExt = getFilenameType texture_atlas_filename_
                local strNewTextureAtlasFilename = strPath + strFileNameOnly + "_S" + strFileExt
                local newTextures
                GetNewTextureFilenameUsingAtlasInfo &newTextures textures materialNames textureType_:#specular
                LoadBitmaps &m_bitmaps newTextures num_textures materialNames cutted_textures isPadding_tresize_ padding_
                RearrangeBitmapsUsingAtlasInfo &m_bitmaps

                _GenerateAtlasTexture &texture_atlasSpecular strNewTextureAtlasFilename \
                    size_of_texatlas_x size_of_texatlas_y &m_bitmaps \
                    isDo_msgs_ isDo_undo_ padding_ isPadding_tresize_
            )--if

            if m_atlasInfo.IsGlossiness() then
            (
                local strPath = getFilenamePath texture_atlas_filename_
                local strFileNameOnly = getFilenameFile texture_atlas_filename_
                local strFileExt = getFilenameType texture_atlas_filename_
                local strNewTextureAtlasFilename = strPath + strFileNameOnly + "_G" + strFileExt
                local newTextures
                GetNewTextureFilenameUsingAtlasInfo &newTextures textures materialNames textureType_:#glossiness
                LoadBitmaps &m_bitmaps newTextures num_textures materialNames cutted_textures isPadding_tresize_ padding_
                RearrangeBitmapsUsingAtlasInfo &m_bitmaps

                _GenerateAtlasTexture &texture_atlasGlossiness strNewTextureAtlasFilename \
                    size_of_texatlas_x size_of_texatlas_y &m_bitmaps \
                    isDo_msgs_ isDo_undo_ padding_ isPadding_tresize_
            )--if
        )--if isDo_generate_ta_ do

        if texture_atlas != undefined then
        (
            m_bIsAtlasGenerated = true
            display texture_atlas
        )--if
        
        if texture_atlasBump != undefined then
        (
            display texture_atlasBump
        )--if
        if texture_atlasSpecular != undefined then
        (
            display texture_atlasSpecular
        )--if
        if texture_atlasGlossiness != undefined then
        (
            display texture_atlasGlossiness
        )--if
        windows.processPostedMessages() -- jintaeks on ¿ÀÀü 11:42 2013-11-14

        --------------------------
        --------------------------
        -- Fifth step: scale and position uvs.
        --------------------------
        print "scale and position uvs"
        
        if isDo_slicing_ and isDo_msgs_ do format "TAG makes new UV coordinates.\n"
        
        if isDo_slicing_ do
        (
            local o = 0
            for real_obj in tag_objs do with undo isDo_undo_
            (
                o += 1

                -- this is a workaround for max 9, because collapseNodeTo is buggy
                local obj = editable_mesh()
                obj.baseobject = copy real_obj.baseobject
                local save_obj = real_obj.baseobject
                hide real_obj

                if isDo_msgs_ do format "Rearrange %'s UVs\n" real_obj.name
                
                select obj
                uvwmod = Unwrap_UVW()
                addModifier obj uvwmod
                uvwmod.setMapChannel map_channel_
                uvwmod.updateView()
                uvwmod.setResetPivotOnSelection true
                uvwmod.setTVSubObjectMode 3
                --uvwmod.edit()

                -- format "debug\n"
                -- format "size_of_texatlas_x = %\n" size_of_texatlas_x
                -- format "size_of_texatlas_y = %\n" size_of_texatlas_y
                
                -- every chunk must be scaled, oriented and translated ...
                -- thus, iterate through all material ids
                for i = 1 to material_info[o].num_materials_used do with undo isDo_undo_
                (
                    local bmp_id = material_info[o].mmatid_to_texid[material_info[o].mmat_ids[i]]
                    
                    local cwidth = m_bitmaps[bmp_id].bmp.width
                    local cheight = m_bitmaps[bmp_id].bmp.height
                    local scale_factor_x
                    local scale_factor_y
            
                    local tp = padding_
                    -- no padding for uvmaps, eh
                    if not cutted_textures[bmp_id] do tp = 0
                    
                    if isPadding_tresize_ do
                    (
                        cwidth -= (tp*2)
                        cheight -= (tp*2)
                    )--if
            
                    if not m_bitmaps[bmp_id].rotated then
                    (
                        scale_factor_x = (cwidth as float) / (size_of_texatlas_x as float)
                        scale_factor_y = (cheight as float) / (size_of_texatlas_y as float)
                    )
                    else
                    (
                        scale_factor_x = (cwidth as float) / (size_of_texatlas_y as float)
                        scale_factor_y = (cheight as float) / (size_of_texatlas_x as float)
                    )--if.. else..
         
                    if (classOf real_obj.material) == Multimaterial then
                    (
                        uvwmod.selectByMatID real_obj.material.materialIDList[material_info[o].mmat_ids[i]]
                    )
                    else if (classOf real_obj.material) == Standardmaterial then
                    (
                        uvwmod.selectPolygons #{1..uvwmod.numberPolygons()}
                    )--if.. else if..
                    uvwmod.updateView()
                    uvwmod.unwrap.breakSelected() -- cleaning up!
                    uvwmod.detachEdgeVertices()

                    local x, y, width, height, temp

                    local new_selection = #{}
                    -- collect faces that uv is less than 0 or greater than 1.
                    -- these uv's will be normalized.
                    -- jintaeks on ¿ÀÀü 9:49 2013-11-26
                    local trimmed_selection = #{} -- jintaeks on ¿ÀÈÄ 4:39 2013-11-25
                    local sel_polys = (uvwmod.getSelectedPolygons()) as Array
                    for f in sel_polys do
                    (
                        uvwmod.getArea #{f} &x &y &width &height &temp &temp
                        -- qff. jintaeks on ¿ÀÈÄ 3:21 2013-11-25
                        if ((x >= -0.001) and (x+width <= 1.002) and (y >= -0.001) and (y+height <= 1.002)) then
                        (
                            new_selection[f] = true
                        )
                        else
                        (
                            new_selection[f] = true
                            trimmed_selection[f] = true
                        )--if.. else..
                    )--for
                    
                    /** for vertices which is not in range from 0 to 1.
                        normalize it's uv to rearrange from 0 to 1.
                        - jintaeks on ¿ÀÀü 9:55 2013-11-26 */
                    uvwmod.selectPolygons trimmed_selection
                    uvwmod.selectFaces trimmed_selection
                    uvwmod.faceToVertSelect()
                    local vert_indices = ( uvwmod.getSelectedVertices() ) as Array
                    local vertTemp
                    
                    for vindex in vert_indices Do
                    (
                        vertTemp = (uvwmod.getVertexPosition 0 vindex)
                        vertTemp.x = MakeValueFrom0To1 vertTemp.x
                        vertTemp.y = MakeValueFrom0To1 vertTemp.y
                        uvwmod.setVertexPosition 0 vindex vertTemp
                        --print vertTemp
                    )--for

                    /** normal processing of vertices
                        - jintaeks on ¿ÀÀü 9:55 2013-11-26 */
                    uvwmod.selectPolygons new_selection
                 
                    if false then
                    (
                        -- disabled old texture rearrange code. jintaeks on ¿ÀÈÄ 7:41 2013-11-22
                        --
                        -- scale the uvs
                        uvwmod.scaleSelectedCenter scale_factor_x 1
                        uvwmod.scaleSelectedCenter scale_factor_y 2
                
                        -- rotate uvs (if needed)
                        if m_bitmaps[bmp_id].rotated do
                        (
                            swap scale_factor_x scale_factor_y
                            uvwmod.rotateSelectedCenter (pi/2.0)
                        )--if
                
                        -- the position should be absolutely centered now, because we move it relatively
                        uvwmod.getArea (uvwmod.getSelectedFaces()) &x &y &width &height &temp &temp
                        local tar_x = 0.5 - (width*0.5)
                        local tar_y = 0.5 - (height*0.5)
                        uvwmod.moveSelected [tar_x - x, tar_y - y, 0.0]
                    
                        -- move uvs    
                        local move_x = ((m_bitmaps[bmp_id].x+tp) as float) / (size_of_texatlas_x as float) - 0.5 + (scale_factor_x * 0.5)
                        local move_y = ((m_bitmaps[bmp_id].y+tp) as float) / (size_of_texatlas_y as float) - 0.5 + (scale_factor_y * 0.5)
                        uvwmod.moveSelected [move_x, -move_y, 0.0]
                    )
                    Else
                    (
                        -- relocated uv coordiate. jintaeks on ¿ÀÈÄ 7:44 2013-11-22
                        --

                        format "bmpId % \n" bmp_id
                        
                        -- select vertices. jintaeks on ¿ÀÈÄ 2:08 2013-11-22
                        uvwmod.selectFaces new_selection
                        uvwmod.faceToVertSelect()
                        local vert_indices = ( uvwmod.getSelectedVertices() ) as Array
                        local vertTemp
                        local uvMoveWidth = 0
                        local uvMoveHeight = cheight
                        
                        if m_bitmaps[bmp_id].rotated then
                        (
                            local matRotAboutZ = ( ( rotateZMatrix 90 ) as matrix3 )
                            for vindex in vert_indices Do
                            (
                                vertTemp = (uvwmod.getVertexPosition 0 vindex)
                                vertTemp = vertTemp * matRotAboutZ
                                vertTemp.x += 1 -- right shift rotated uv. jintaesk on ¿ÀÈÄ 4:01 2013-11-22
                                uvwmod.setVertexPosition 0 vindex vertTemp
                                --print vertTemp
                            )--for
                            swap scale_factor_x scale_factor_y
                            uvMoveWidth = 0
                            uvMoveHeight = cwidth
                        )--if
                        
                        for vindex in vert_indices Do
                        (
                            vertTemp = (uvwmod.getVertexPosition 0 vindex)
                            vertTemp.x *= scale_factor_x
                            vertTemp.y *= scale_factor_y

                            uvwmod.setVertexPosition 0 vindex vertTemp
                            --print vertTemp
                        )--for
                        
                        -- move uvs    
                        local move_x = ((m_bitmaps[bmp_id].x + uvMoveWidth + tp) as float) / (size_of_texatlas_x as float)
                        /** fixed critical bug.
                            @note   don't use like below.
                                    maybe numerical rounding error.
                            @date   jintaeks on ¿ÀÈÄ 10:19 2013-11-29
                        local move_y = 1.0 - ((m_bitmaps[bmp_id].y + uvMoveHeight + tp) as float) / (size_of_texatlas_y as float)
                        uvwmod.moveSelected [move_x, move_y, 0.0]
                        */
                        local move_y = ((m_bitmaps[bmp_id].y + uvMoveHeight + tp) as float) / (size_of_texatlas_y as float)
                        uvwmod.moveSelected [move_x, 1.0 - move_y, 0.0]
                        
                        format "m_bitmaps[bmp_id].x = %, m_bitmaps[bmp_id].y = %\n" ( m_bitmaps[bmp_id].x ) ( m_bitmaps[bmp_id].y )
                        format "uvMoveWidth = %, uvMoveHeight = %\n" uvMoveWidth uvMoveHeight
                        format "move_x = %, move_y = %\n" ( move_x ) ( move_y )
                    )--if.. else..
                )--for i = 1 to material_info[o].num_materials_used do with undo isDo_undo_
                
                --------------------------
                --------------------------
                -- Last step: finish the model
                --------------------------
             
                convertTo obj PolyMeshObject

                -- set face material id to 1. jintaeks on 20:44 2013-12-18
                --
                local facecount = obj.faces.count
                -- progress bar update related variables. jintaeks on ¢¯AAu 11:40 2013-11-14
                local iProgressUpdateStep = facecount / 100
                local iProgressUpdateCounter = 0

                for f = 1 to facecount do
                (
                    polyop.setFaceMatID obj f 1
                
                    -- update progress bar. jintaeks on ¿ÀÀü 11:27 2013-11-14
                    iProgressUpdateCounter += 1
                    if iProgressUpdateCounter >= iProgressUpdateStep then
                    (
                        iProgressUpdateCounter = 0
                        progBar_.value = ( f as float / facecount ) * 100
                        windows.processPostedMessages()
                    )--if
                )--for
                
                -- continue the workaround, *sigh*
                real_obj.baseobject = obj.baseobject
                for geo in geometry do
                (
                    if geo.baseobject == save_obj then geo.baseobject = obj.baseobject
                )--for
                delete obj
                unhide real_obj
                windows.processPostedMessages() -- jintaeks on ¿ÀÀü 11:42 2013-11-14
            )--for real_obj in tag_objs do with undo isDo_undo_
        )--if isDo_slicing_ do
        
        select tag_objs
        progBar_.value = 0
        windows.processPostedMessages() -- jintaeks on ¿ÀÀü 11:42 2013-11-14
     
        if isDo_msgs_ do format "TAG ended.\n"
     
        return 1
    )--function TAG()

    /** @brief  create material string info for 'mtrl_'
        @return constructed material string info.
        @date   jintaeks on 2013-11-11 */
    function CreateMaterialStringKey mtrl_ =
    (
        if classof mtrl_ == Standard then
        (
            local map = ""
            if mtrl_.diffuseMap != undefined and mtrl_.diffuseMap.filename != undefined do
            (
                map += "diffuse = "
                map += mtrl_.diffuseMap.filename + "\n"
            )
            if mtrl_.opacityMap != undefined and mtrl_.opacityMap.filename != undefined do
            (
                map += "opacity = "
                map += mtrl_.opacityMap.filename + "\n"
            )
            if mtrl_.specularLevelMap != undefined and mtrl_.specularLevelMap.filename != undefined do
            (
                map += "specularLevel = "
                map += mtrl_.specularLevelMap.filename + "\n"
            )
            if mtrl_.glossinessMap != undefined and mtrl_.glossinessMap.filename != undefined do
            (
                map += "glossiness = "
                map += mtrl_.glossinessMap.filename + "\n"
            )
            if mtrl_.bumpMap != undefined and mtrl_.bumpMap.filename != undefined do
            (
                map += "bump = "
                map += mtrl_.bumpMap.filename + "\n"
            )
            if mtrl_.reflectionMap != undefined and mtrl_.reflectionMap.filename != undefined do
            (
                map += "reflection = "
                map += mtrl_.reflectionMap.filename + "\n"
            )
                
            --map += mtrl_.shaderType as string + mtrl_.wire as string + mtrl_.twoSided as string + mtrl_.faceMap as string + mtrl_.faceted as string + mtrl_.ambient as string
            --+ mtrl_.Diffuse as string + mtrl_.Specular as string + mtrl_.selfIllumAmount as string + mtrl_.opacity as string + mtrl_.specularLevel as string + mtrl_.glossiness as string
            --+ mtrl_.Soften as string + mtrl_.diffuseMapEnable as string + mtrl_.diffuseMapAmount as string + mtrl_.specularLevelMapEnable as string
            --+ mtrl_.specularLevelMapAmount as string + mtrl_.glossinessMapEnable as string + mtrl_.glossinessMapAmount as string + mtrl_.bumpMapEnable as string
            --+ mtrl_.bumpMapAmount as string + mtrl_.reflectionMapEnable as string + mtrl.reflectionMapAmount as string
            return tolower( map )
        )--if
        
        return undefined
    )--function CreateMaterialStringKey()
    
    /** @brief  get material info
        @param materialInfo_ : [out] constructed text material info.
        @date   jintaeks on 2013-11-11 */
    function GetMaterialInfo &materialInfo_ &material_ =
    (
        --messageBox material_.name
        if classOf material_ == StandardMaterial then
        (
            local stringKey = CreateMaterialStringKey material_
            if stringKey != undefined then
            (
                materialInfo_ += "material = " + material_.name + "\n"
                materialInfo_ += stringKey
            )--if
        )
        else
        (
            for mtrl in material_ do
            (
                if classof mtrl == Shell_Material then
                (
                )
                else if classof mtrl == MultiMaterial then
                (
                )
                else
                (
                    GetMaterialInfo &materialInfo_ &mtrl -- recursion for standard material. jintaeks on 2013-11-12
                )--if.. else if.. esle..
            )--for
        )--if.. else..
    )--function GetMaterialInfo

    --------------------------------------------------------------------------------------
    --------------------------------------------------------------------------------------

    -- rollout definition. seojtdoc
    rollout ro_tag "Texture Atlas Generator"
    (
        group "Settings"
        (
            checkbox cb_do_undo "Disable Undo" checked:true
            checkbox cb_do_messages "Generate Messages" checked:true
            checkbox cb_do_auto_resume "Ignore Warnings" checked:false
        )
        group "Object"
        (
            checkbox cb_ob_slicing "Slice Geometry and Generate UVs" checked:true
            --label lb_ob_slicing "Generate UVs" pos:[31,119]
            checkbox cb_ob_breakall "Break all Edges" checked:false
            spinner sp_ob_map_channel "Map Channel:" range:[1,99,1] type:#integer fieldWidth:80 align:#left
        )
        group "Textures"
        (
            spinner sp_tx_padding "Padding:" range:[0, 32, 2] type:#integer fieldWidth:80 align:#left
            checkbox cb_tx_resize "Shrink in Atlas" checked:true
        )
        group "Atlas File"
        (
            checkbox cb_ta_create "Create" checked:true
            checkbox cb_ta_force_padding "No Padding" checked:false enabled:false
            edittext et_ta_filename ""
            button bn_ta_filename "Choose Path & Filename" align:#right
            button btnScenePath "Auto set to scene path" align:#right
            button btnFilePath "Auto set to file path" align:#right
        )
        group "Texture Locator"
        (
            button btnTextureLocator "Edit Texture Position"  align:#right -- jintaeks on 2013-11-12
        )
        group "Generator"
        (
            button bn_do_it "Generate Texture Atlas" align:#right
            progressBar m_progressBar -- progress bar. jintaeks on ¿ÀÀü 11:02 2013-11-14
            button btnCancelProcess "Cancel Process"  align:#right -- jintaeks ¿ÀÈÄ 8:01 2013-11-25
        )
        --button bnTest "Test"
        
        --label lb_3d_io "2009 (c) 3d-io" height:16
        label author "jintaeks@dongseo.ac.kr" height:16
        label dsu "Copyright (c) 2017 Dicon, DSU" height:16
        
        ------

        on cb_ob_slicing changed arg do
        (
            cb_ob_breakall.enabled = arg
            if cb_ta_create.checked do
            (
                cb_ta_force_padding.enabled = not arg
            )--if
            if cb_ta_force_padding.enabled do
            (
                sp_tx_padding.enabled = not cb_ta_force_padding.checked
                cb_tx_resize.enabled = not cb_ta_force_padding.checked
            )--if
        )--on cb_ob_slicing changed arg do
        
        on cb_ta_create changed arg do
        (
            et_ta_filename.enabled = arg
            bn_ta_filename.enabled = arg
            if not arg or (arg and not cb_ob_slicing.checked) do
            (
                cb_ta_force_padding.enabled = arg
            )--if
        )--on cb_ta_create changed arg do
        
        on cb_ta_force_padding changed arg do
        (
            sp_tx_padding.enabled = not arg
            cb_tx_resize.enabled = not arg
        )--on cb_ta_force_padding changed arg do
        
        on bn_ta_filename pressed do
        (
            local output_name = getSaveFileName caption:"Image File" \
                                                types:"Targa (*.tga)|*.tga|BMP (*.bmp)|*.bmp|JPEG (*.jpg)|*.jpg|All Files (*.*)|*.*|" \
                                                initialDir:"$images"
            if output_name != undefined do
            (
                et_ta_filename.text = output_name
            )--if
        )--on bn_ta_filename pressed do

         on btnScenePath pressed Do
         (
            local strMaxScenePath = GetDir #scene -- "C:\Users\jintaeks\Documents\3dsMax\scenes"
            if strMaxScenePath[ strMaxScenePath.count] != "\\" then
            (
                strMaxScenePath += "\\"
            )--if
            
            if selection.count == 1 then
            (
                et_ta_filename.text = strMaxScenePath
                et_ta_filename.text += selection[1].name
                et_ta_filename.text += "_atlas.tga"
            )
            else
            (
                et_ta_filename.text = strMaxScenePath + "atlas.tga"
            )--if.. else..
         )--on btnScenePath pressed Do
         
         on btnFilePath pressed do
         (
            local strMaxScenePath = maxFilePath -- "F:\techsupport\source\DsuAtlasMaxPlugin\"
            if strMaxScenePath[ strMaxScenePath.count] != "\\" then
            (
                strMaxScenePath += "\\"
            )--if
            
            if selection.count == 1 then
            (
                et_ta_filename.text = strMaxScenePath
                et_ta_filename.text += selection[1].name
                et_ta_filename.text += "_atlas.tga"
            )
            else
            (
                et_ta_filename.text = strMaxScenePath + "atlas.tga"
            )--if.. else..
         )--on btnFilePath pressed do

        on bn_do_it pressed do
        (
            if selection.count == 1 then
            (
                -- jintaeks on ¿ÀÈÄ 4:13 2013-12-03
                if classOf selection[1].material == Standardmaterial then
                (
                    messageBox "Cannot process standard material"
                    return -1
                )--if

                -- jintaeks on ¿ÀÈÄ 7:50 2013-11-25
                m_bIsAtlasGenerated = false
                m_bIsCancelProcess = false
                
                local bIsProcessAtlas = false

                /** when external atlas manager flag is enalbed.
                    we create atlas info object and get information from clipboard
                    - jintaeks on ¿ÀÀü 10:30 2013-11-19 */
                if m_bIsUseExternalAtlasManager == true then
                (
                    -- create atlas info and get clipboard text data.
                    m_atlasInfo = KAtlasInfo()
                    local strData
                    try
                    (
                        strData = getclipboardText()
                    )
                    catch
                    (
                        strData = undefined
                    )--try.. catch..

                    if strData != undefined then
                    (
                        -- initialize atlas info from clipboard data.
                        local initializeResult = m_atlasInfo.Initialize strData -- initialize atlas info. jintaeks on ¿ÀÈÄ 5:10 2013-11-13
                        if initializeResult == true then
                        (
                            local iNumMtrlInAtlas = m_atlasInfo.GetNumMaterial()
                            if iNumMtrlInAtlas >= 1 then
                            (
                                bIsProcessAtlas = true
                            )
                            else
                            (
                                messageBox "No material info"
                            )--if.. else..
                        )
                        else
                        (
                            messageBox "Invalid Texture Location info"
                        )--if.. else..
                    )--if
                )
                else
                (
                    bIsProcessAtlas = true
                )--if.. else..

                if bIsProcessAtlas == true then
                (
                    -- disable relevant Ui controls.
                    bn_do_it.enabled = false
                    btnTextureLocator.enabled = false
                    
                    -- main Texture atlas generator function.
                    TAG selection map_channel_:sp_ob_map_channel.value \
                        progBar_:m_progressBar \
                        padding_:sp_tx_padding.value \
                        isPadding_tresize_:cb_tx_resize.checked \
                        texture_atlas_filename_:et_ta_filename.text \
                        isDo_undo_:(not cb_do_undo.checked) \
                        isDo_slicing_:cb_ob_slicing.checked \
                        isDo_generate_ta_:cb_ta_create.checked \
                        isDo_break_all_:cb_ob_breakall.checked \
                        isDo_msgs_:cb_do_messages.checked \
                        isDo_force_padding_:(not cb_ta_force_padding.checked) \
                        isDo_ignore_errors:cb_do_auto_resume.checked
                    
                    -- restore relevant Ui controls.
                    bn_do_it.enabled = true
                    btnTextureLocator.enabled = true

                    -- close bitmap data. jintaeks on ¿ÀÈÄ 4:10 2013-11-20
                    for sbmp in m_bitmaps do
                    (
                        close sbmp.bmp
                    )--for

                    if m_bIsAtlasGenerated == true then
                    (
                        messageBox "Atlas generated!"
                    )
                    else
                    (
                        messageBox "Atlas generation failed"
                    )--if.. else..
                    
                )--if
                
                -- gc light:true
            )
            else
            (
                messageBox "No object selected"
            )--if.. else..
        )--on bn_do_it pressed do
        
        on btnCancelProcess pressed do
        (
            m_bIsCancelProcess = true
        )--on btnCancelProcess pressed do
        
        /** @brief  event handler for texture locator button pressed.
            @date   jintaeks on 2013-11-11 */
        on btnTextureLocator pressed do
        (
            if selection.count == 1 then
            (
                -- get material info of selected object.
                local base_obj = $.baseobject
                local materialInfo = ""
                GetMaterialInfo &materialInfo &selection[1].material
                
                -- construct output .odm filename.
                local maxPath = GetDir #maxRoot
                local scenePath = maxFilePath -- get current .max file path.
                local outputFilename = scenePath + selection[1].name + ".odm"
                if outputFilename != undefined  then
                (
                    -- write material information to file.
                    local outputFile = createfile outputFilename
                    format "%" materialInfo to:outputFile
                    close outputFile
                    
                    -- launch texture locator.
                    --shellLaunch @"F:\techsupport\source\DsuAtlasMaxPlugin\DsuAtlasTextureLocator.exe" outputFilename
                    local textureLocatorFilePath = maxPath + "DsuAtlasTextureLocator.exe"
                    shellLaunch textureLocatorFilePath outputFilename
                    --messageBox materialInfo
                    
                    -- get clipboard text. jintaeks on 2013-11-08
                    --local clipboardText = getclipboardText()
                    --messageBox clipboardText
                )--if
            )
            else
            (
                messageBox "select a object"
            )--if.. else..
        )--on btnTextureLocator pressed do
        
        on ro_tag open do
        (
            file = openFile filename mode:"rt"
            
            if file == undefined then
            (
                -- create a new ini file because it doesn't exist
                file = createFile filename

                format "%\n%\n%\n" true true true
                format "%\n%\n%\n" true false true
                format "1\n"
                format "%\n%\n%\n" true false false
                format "C:\\TEMP\\TEXTUREATLAS.tga\n"
                format "%\n%\n"  true true
                format "2\n%\n%\n%\n" true true true
                
                --
                
                cb_do_undo.checked = true
                cb_do_messages.checked = true
                cb_do_auto_resume.checked = true

                cb_ob_slicing.checked = true
                cb_ob_breakall.checked = false
                cb_ob_breakall.enabled = true
                
                sp_ob_map_channel.value = 1

                cb_ta_create.checked = true
                cb_ta_force_padding.checked = false
                cb_ta_force_padding.enabled = false
                et_ta_filename.text = "C:\\TEMP\\TEXTUREATLAS.tga"
                et_ta_filename.enabled = true
                bn_ta_filename.enabled = true
                
                sp_tx_padding.value = 0
                sp_tx_padding.enabled = true
                cb_tx_resize.checked = true
                cb_tx_resize.enabled = true
            )
            else
            (
                cb_do_undo.checked = execute (readLine file)
                cb_do_messages.checked = execute (readLine file)
                cb_do_auto_resume.checked = execute (readLine file)

                cb_ob_slicing.checked = execute (readLine file)
                cb_ob_breakall.checked = execute (readLine file)
                cb_ob_breakall.enabled = execute (readLine file)
                
                sp_ob_map_channel.value = (readLine file) as integer

                cb_ta_create.checked = execute (readLine file)
                cb_ta_force_padding.checked = execute (readLine file)
                cb_ta_force_padding.enabled = execute (readLine file)
                et_ta_filename.text = readLine file
                et_ta_filename.enabled = execute (readLine file)
                bn_ta_filename.enabled = execute (readLine file)
                
                sp_tx_padding.value = (readLine file) as integer
                sp_tx_padding.enabled = execute (readLine file)
                cb_tx_resize.checked = execute (readLine file)
                cb_tx_resize.enabled = execute (readLine file)
            )--if.. else..
        )--on ro_tag open do
        
        on ro_tag  close do
        (
            if file != undefined then
            (
                close file
            )--if

            deleteFile filename
            file = createFile filename
            
            format "%\n" cb_do_undo.checked to:file
            format "%\n" cb_do_messages.checked to:file
            format "%\n" cb_do_auto_resume.checked to:file
            
            format "%\n" cb_ob_slicing.checked to:file
            format "%\n" cb_ob_breakall.checked to:file
            format "%\n" cb_ob_breakall.enabled to:file
            
            format "%\n" sp_ob_map_channel.value to:file
            
            format "%\n" cb_ta_create.checked to:file
            format "%\n" cb_ta_force_padding.checked to:file
            format "%\n" cb_ta_force_padding.enabled to:file
            format "%\n" et_ta_filename.text to:file
            format "%\n" et_ta_filename.enabled to:file
            format "%\n" bn_ta_filename.enabled to:file
            
            format "%\n" sp_tx_padding.value to:file
            format "%\n" sp_tx_padding.enabled to:file
            format "%\n" cb_tx_resize.checked to:file
            format "%\n" cb_tx_resize.enabled to:file
            
            close file
        )--on ro_tag  close do
        
        -- @brief   event handler when "Test" button pressed
        -- @date    jintaeks on ¿ÀÈÄ 4:09 2013-11-13
        on bnTest pressed do
        (
            m_atlasInfo = KAtlasInfo()
            local strData
            try
            (
                strData = getclipboardText()
            )
            catch
            (
                strData = undefined
            )--try.. catch..

            if strData != undefined then
            (
                local initializeResult = m_atlasInfo.Initialize strData
                if initializeResult == true then
                (
                    local iNumMtrlInAtlas = m_atlasInfo.GetNumMaterial()
                    if iNumMtrlInAtlas >= 1 then
                    (
                        m_atlasInfo.Print()
                        --messageBox strData
                    )--if
                )
                else
                (
                    messageBox "invalid texture location info"
                )--if.. else..
            )
            else
            (
                messageBox "invalid clipboard data"
            )--if.. else..
        )--on bnTest pressed do
    )--rollout ro_tag "TexAtlasGen 1.0.5"
    
    -- on isEnabled Do
    -- (
        -- selection.count == 1
    -- )--on isEnabled Do

    on execute do
    (
        --createDialog ro_tag 300 446
        theNewFloater = newRolloutFloater "Texture Atlas Generator v1.0.5" 400 640
        addRollout ro_tag theNewFloater rolledUp:false
    )--on execute do
)--macroScript TexAtlasGen2
