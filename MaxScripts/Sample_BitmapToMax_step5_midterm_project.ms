rollout BitmapBoxDlg "BitmapBox"
(
    editText        editBoxSize "MaxHeight"
    spinner         spinBoxSize "Box Size" range:[1,100,1] type:#integer
    button          btnLoadImage "Load"
    bitmap          image
    button          btnCreate "Create"
    progressbar     doitProgress color:red
    
    on btnLoadImage pressed do
    (
        local bmpFilename = getOpenFileName caption:"Select Texture" filename:"*.png"
        if bmpFilename != undefined do
        (
            image.bitmap = openBitmap bmpFilename
            local ss = stringStream ""
            format "width = %, height = %\n" image.bitmap.width image.bitmap.height to:ss
            messageBox ( ss as string )
        )
    )
    
    on btnCreate pressed Do
    (
        --local boxSize = editBoxSize.text as integer
        local boxSize = spinBoxSize.value as integer
        
        if boxSize < 1 do boxSize = 1
        local bitmapSource = image.bitmap
        if bitmapSource != undefined then
        (
            for iHeight = 1 to bitmapSource.height Do
            (
                doitProgress.value = 100. * iHeight / bitmapSource.height
                windows.processPostedMessages()
                for iWidth = 1 to bitmapSource.width do
                (
                    local pixels = getPixels bitmapSource [iWidth-1, iHeight-1] 1
                    local pixel = pixels[1]
                    --format "width = %, height = % r = % g = % b = %" iWidth iHeight pixel.r pixel.g pixel.b
					length = (pixel.r + pixel.g + pixel.b ) / 3 / 255
					length = length * (editBoxsize.text as integer)
                    (
                        local x = iWidth
                        local y = bitmapSource.height - iHeight + 1
                        x *= boxSize
                        y *= boxSize
                        local b = box width:boxSize height:length length:boxSize
                        b.pos = [x, y, 0]
                        b.wirecolor = [pixel.r, pixel.g, pixel.b]
                    )--if
                )--for
                redrawViews()
            )--for
        )--if
    )--on btnHello pressed Do
)

CreateDialog BitmapBoxDlg
