global strMaxRootPath = GetDir #maxroot -- "C:\Program Files\Autodesk\3ds Max 2011\"
global strUserMacrosPath = GetDir #userMacros
strUserMacrosPath += "\\"
global strUserScripts = GetDir #userScripts
strUserScripts += "\\"
global strThisScriptFilePath = getThisScriptFilename()
global strSrcPath = getFilenamePath strThisScriptFilePath

global msg = "copying from "  + (strSrcPath as string ) + " to " + ( strMaxRootPath as string )
messageBox msg

-- delete existing files. jintaeks on 오후 4:40 2013-11-19
deleteFile (strMaxRootPath as string + "FreeImageNET.dll" )
deleteFile (strMaxRootPath as string + "FreeImage.dll" )
deleteFile (strMaxRootPath as string + "DsuAtlasTextureLocator.exe" )
deleteFile ( strUserScripts as string + "startup\\DsuTextureAtlasGenerator_startup.ms" )

-- copy new files. jintaeks on 오후 4:41 2013-11-19
copyFile ( strSrcPath as string + "FreeImageNET.dll" ) (strMaxRootPath as string + "FreeImageNET.dll" )
copyFile ( strSrcPath as string + "FreeImage.dll" ) (strMaxRootPath as string + "FreeImage.dll" )
copyFile ( strSrcPath as string + "DsuAtlasTextureLocator.exe" ) (strMaxRootPath as string + "DsuAtlasTextureLocator.exe" )
copyfile ( strSrcPath as string + "DsuTextureAtlasGenerator_startup.ms" ) ( strUserScripts as string + "startup\\DsuTextureAtlasGenerator_startup.ms" )

--copyfile ( strSrcPath as string + "DsuTextureAtlasGenerator.mcr" ) "$userScripts\\DsuTextureAtlasGenerator.mcr"
--copyfile ( strSrcPath as string + "KAtlasInfo.ms" ) "$userScripts\\KAtlasInfo.ms"

deleteFile ( strUserMacrosPath as string + "Dsu-TexAtlasGen.mcr" )
deleteFile ( strUserMacrosPath as string + "Dsu-TexAtlasGen2.mcr" )

--filein "$userScripts\\startup\\DsuTextureAtlasGenerator_startup.ms"
filein ( strSrcPath as string + "DsuTextureAtlasGenerator.mcr" )
filein ( strSrcPath as string + "DsuInvalidFaceBreaker.mcr" )
