rollout BitmapBoxDlg "BitmapBox"
(
    editText        editBoxSize "BoxSize"
    button          btnLoadImage "Load"
    bitmap          image
    
    on btnLoadImage pressed do
    (
        local bmpFilename = getOpenFileName caption:"Select Texture" filename:"*.png"
        if bmpFilename != undefined do
        (
            image.bitmap = openBitmap bmpFilename
            local ss = stringStream ""
            format "width = %, height = %\n" image.width image.height to:ss
            messageBox ( ss as string )
        )
    )
)

CreateDialog BitmapBoxDlg
