rollout testRollout "Test" width:162 height:300
(
    button btnHello "Hello" pos:[21,24] width:111 height:24
    progressbar doitProgress color:red
    
    on btnHello pressed Do
    (
        local new_bmp = getOpenFileName caption:"Select Texture" filename:"*.png"
        if new_bmp != undefined then
        (
            local bitmapSource = openBitmap new_bmp
            local ss = stringStream ""
            format "width = %, height = %\n" bitmapSource.width bitmapSource.height to:ss
            messageBox ( ss as string )
            for iHeight = 1 to bitmapSource.height Do
            (
                doitProgress.value = 100. * iHeight / bitmapSource.height
                --windows.processPostedMessages()
                for iWidth = 1 to bitmapSource.width do
                (
                    local pixels = getPixels bitmapSource [iWidth-1, iHeight-1] 1
                    local pixel = pixels[1]
                    format "width = %, height = % r = % g = % b = %" iWidth iHeight pixel.r pixel.g pixel.b
                    if pixel.r < 255 then
                    (
                        local x = iWidth
                        local y = bitmapSource.height - iHeight + 1
                        local b = box width:1 height:1 length:1
                        b.pos = [x, y, 0]
                        b.wirecolor = [pixel.r, pixel.g, pixel.b]
                    )--if
                )--for
            )--for
        )--if
    )--on btnHello pressed Do
)

CreateDialog testRollout
