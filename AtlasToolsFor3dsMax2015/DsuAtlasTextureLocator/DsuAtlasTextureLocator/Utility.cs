using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
//using System.Linq;
using System.Text;
// jintaeks on 2013-11-05, 14:12
using System.Windows.Forms;
using System.Collections;
using System.IO;
using System.Threading;
using System.Diagnostics;
using FreeImageAPI; // to manipulate .dds files. jintaeks on 2013-11-04, 16:45
using System.Drawing.Imaging; // jintaeks on 2013-11-22, 20:08


namespace DsuAtlasTextureLocator
{
    /** @enum   texture types of standard material
        @date   jintaeks on 2013-11-04, 12:19 */
    public enum ETextureType
    {
        DIFFUSE,
        BUMP,
        SPECULAR,
        GLOSSINESS
    }//enum ETextureType

    /** @struct KStdMaterialInfo
        @date   jintaeks on 2013-11-04, 11:56 */
    public struct KStdMaterialInfo
    {
        public string   m_strMaterialName; // 3dsMax material name
        public string   m_strDiffuseTextureName; // diffuse texture full path filename
        public string   m_strBumpTextureName; // bump texture full path filename
        public string   m_strSpecularTextureName; // specular level texture full path filename
        public string   m_strGlossinessTextureName; // glossiness texture full path filename
        public Image    m_image;

        public KStdMaterialInfo( string strMaterialName_
            , string strDiffuseTextureName_
            , string strBumpTextureName_
            , string strSpecularTextureName_
            , string strReflectionTextureName_ )
        {
            m_strMaterialName = strMaterialName_;
            m_strDiffuseTextureName = strDiffuseTextureName_;
            m_strBumpTextureName = strBumpTextureName_;
            m_strSpecularTextureName = strSpecularTextureName_;
            m_strGlossinessTextureName = strReflectionTextureName_;
            m_image = null;
        }//KStdMaterialInfo()

        public string GetTextureFileName( ETextureType eTextureType_ )
        {
            switch( eTextureType_ )
            {
                case ETextureType.DIFFUSE:
                    return m_strDiffuseTextureName;
                case ETextureType.BUMP:
                    return m_strBumpTextureName;
                case ETextureType.SPECULAR:
                    return m_strSpecularTextureName;
                case ETextureType.GLOSSINESS:
                    return m_strGlossinessTextureName;
            }//switch

            return "";
        }//GetTextureFileName()
    }//struct KStdMaterialInfo

    ////////////////////////////////////////////////////////////////////////////////////////////////////
    /** @class  Utility
        @date   jintaeks on 2013-11-05, 14:14 */
    public class Utility
    {
        /// <summary>
        /// load .odm(Dsu material) file
        /// jintaeks on 2013-11-07, 15:13
        /// </summary>
        /// <param name="alistMaterials_"></param>
        /// <param name="strOdmFilePath_"> .odm file path </param>
        /// <returns></returns>
        public static bool LoadDsuMaterialInfo( ref ArrayList alistMaterials_, string strOdmFilePath_ )
        {
            if( System.IO.File.Exists( strOdmFilePath_ ) == false )
            {
                MessageBox.Show( "파일이 존재하지 않습니다. \nPath : " + strOdmFilePath_ );
                return false;
            }//if

            KStdMaterialInfo stdMaterialInfo;
            {
                stdMaterialInfo.m_strMaterialName = "";
                stdMaterialInfo.m_strDiffuseTextureName = "";
                stdMaterialInfo.m_strBumpTextureName = "";
                stdMaterialInfo.m_strSpecularTextureName = "";
                stdMaterialInfo.m_strGlossinessTextureName = "";
                stdMaterialInfo.m_image = null;
            }//block

            bool bIsNewStdMaterial = false;
            int iParseMode = 0;
            string strLine;
            // you must set 'Encoding.Default' to read Korean Hangul text from file.
            // - jintaeks on 2013-11-04, 14:48
            StreamReader file = new StreamReader( strOdmFilePath_, Encoding.Default );
            while( ( strLine = file.ReadLine() ) != null )
            {
                strLine.Trim();
                //if (strLine == "[InvalidSymbolList]")
                //{
                //    iParseMode = 1; // "InvalidSymbolList" parsing mode
                //    continue;
                //}
                //else if (strLine == "[Projects]")
                //{
                //    iParseMode = 2; // "Projects" parsing mode
                //    continue;
                //}//if.. else if..

                if( strLine.Length <= 0 )
                {
                    continue;
                }//if

                if( iParseMode == 0 )
                {
                    int iStrLength = strLine.Length;
                    int iEqualSignIndex = strLine.IndexOf( "=" );
                    string strMaterialType = strLine.Substring( 0, iEqualSignIndex );
                    strMaterialType = strMaterialType.Trim();
                    strMaterialType = strMaterialType.ToLower();

                    int iRemainedTextLenght = iStrLength - iEqualSignIndex - 1;
                    // 'strTextureFile' is material name or texture filename.
                    string strTextureFile = strLine.Substring( iEqualSignIndex + 1, iRemainedTextLenght );
                    strTextureFile = strTextureFile.Trim();

                    if( strMaterialType == "material" )
                    {
                        if( bIsNewStdMaterial == true )
                        {
                            alistMaterials_.Add( stdMaterialInfo );
                        }//if
                        bIsNewStdMaterial = false; // reset standard material existence flag. jintaeks on 2013-11-04, 12:01

                        // set standard material name. jintaeks on 2013-11-04, 12:02
                        if( strTextureFile.Length >= 1 )
                        {
                            bIsNewStdMaterial = true;
                            stdMaterialInfo.m_strMaterialName = strTextureFile; // 'strTextureFile' is material name.
                            stdMaterialInfo.m_strDiffuseTextureName = "";
                            stdMaterialInfo.m_strBumpTextureName = "";
                            stdMaterialInfo.m_strSpecularTextureName = "";
                            stdMaterialInfo.m_strGlossinessTextureName = "";
                        }//if
                    }
                    else if( strMaterialType == "diffuse" )
                    {
                        stdMaterialInfo.m_strDiffuseTextureName = strTextureFile;
                    }
                    else if( strMaterialType == "bump" )
                    {
                        stdMaterialInfo.m_strBumpTextureName = strTextureFile;
                    }
                    else if( strMaterialType == "specularlevel" )
                    {
                        stdMaterialInfo.m_strSpecularTextureName = strTextureFile;
                    }
                    else if( strMaterialType == "glossiness" )
                    {
                        stdMaterialInfo.m_strGlossinessTextureName = strTextureFile;
                    }//if.. else if..

                    //m_dicFileSymbols.Add(strFilename, astrSymbols);
                }//if
            }//while

            // add yet added standard material. jintaeks on 2013-11-04, 12:24
            if( bIsNewStdMaterial == true )
            {
                alistMaterials_.Add( stdMaterialInfo );
                bIsNewStdMaterial = false;
            }//if

            file.Close();

            return true;
        }//LoadDsuMaterialInfo()

        public static void LoadMaterialTextures( ref ArrayList alistMaterials_, ETextureType eTextureType_, string strAlternativePath_, bool bLoadTexture_ )
        {
            for( int iMtrl = 0; iMtrl < alistMaterials_.Count; ++iMtrl )
            {
                KStdMaterialInfo stdMtrl = new KStdMaterialInfo();
                stdMtrl = ( KStdMaterialInfo )alistMaterials_[iMtrl];
                //KStdMaterialInfo stdMtrl = ( KStdMaterialInfo )alistMaterials_[iMtrl];
                string strTextureFileName = "";
                bool bIsFileExist = false;
                switch( eTextureType_ )
                {
                    case ETextureType.DIFFUSE:
                        strTextureFileName = stdMtrl.m_strDiffuseTextureName;
                        break;
                    case ETextureType.BUMP:
                        strTextureFileName = stdMtrl.m_strBumpTextureName;
                        break;
                    case ETextureType.SPECULAR:
                        strTextureFileName = stdMtrl.m_strSpecularTextureName;
                        break;
                    case ETextureType.GLOSSINESS:
                        strTextureFileName = stdMtrl.m_strGlossinessTextureName;
                        break;
                }//switch

                // check file existence in original path.
                if( System.IO.File.Exists( strTextureFileName ) == false )
                {
                    // when texture file is not exist in original path
                    // try to load alternative path which is program was executed.
                    // - jintaeks on 2013-11-04, 21:09
                    string strFileName = Path.GetFileName( strTextureFileName );
                    string strFilePath = strAlternativePath_ + "\\" + strFileName;
                    if( System.IO.File.Exists( strFilePath ) == true )
                    {
                        strTextureFileName = strFilePath;
                        switch( eTextureType_ )
                        {
                            case ETextureType.DIFFUSE:
                                stdMtrl.m_strDiffuseTextureName = strTextureFileName;
                                break;
                            case ETextureType.BUMP:
                                stdMtrl.m_strBumpTextureName = strTextureFileName;
                                break;
                            case ETextureType.SPECULAR:
                                stdMtrl.m_strSpecularTextureName = strTextureFileName;
                                break;
                            case ETextureType.GLOSSINESS:
                                stdMtrl.m_strGlossinessTextureName = strTextureFileName;
                                break;
                        }//switch
                        bIsFileExist = true;
                    }//if
                }
                else
                {
                    bIsFileExist = true;
                }//if.. else..

                if( bIsFileExist == true && bLoadTexture_ == true )
                {
                    // test original Image control. jintaeks on 2013-11-04, 20:28
                    //strTextureFileName = @"F:\techsupport\source\DsuAtlasMaxPlugin\Build001_Test01_Dif01.jpg"; // test
                    //stdMtrl.m_image = Image.FromFile( strTextureFileName );

                    FIBITMAP fiBitmap = FreeImage.LoadEx( strTextureFileName );
                    //FreeImage.SetTransparent( fiBitmap, false );
                    //stdMtrl.m_image = FreeImage.GetBitmap( fiBitmap );
                    Image img = FreeImage.GetBitmap( fiBitmap );
                    //img = Utility.SetImageOpacity( img, 1 );
                    stdMtrl.m_image = img;
                }
                else
                {
                    stdMtrl.m_image = null;
                }//if.. else..

                // update material info. jintaeks on 2013-11-04, 21:09
                alistMaterials_[iMtrl] = stdMtrl;
            }//foreach
        }//LoadMaterialTextures()

        public static int GetRecommendedAtlasSize( int iTotalWidth_ )
        {
            if( iTotalWidth_ >= 2048 )
            {
                return 2048;
            }
            else if( iTotalWidth_ > 1024 )
            {
                return 2048;
            }
            else if( iTotalWidth_ > 512 )
            {
                return 1024;
            }
            else if( iTotalWidth_ > 256 )
            {
                return 512;
            }
            else if( iTotalWidth_ > 128 )
            {
                return 256;
            }
            else if( iTotalWidth_ > 64 )
            {
                return 128;
            }
            else
            {
                return 64;
            }//if.. else if.. else..
        }//GetRecommendedAtlasSize()

        public static void GetRecommendedAtlasWidthHeight( ref int iAtlasWidth_, ref int iAtlasHeight_, int iTotalWidth_, int iTotalHeight_ )
        {
            iAtlasWidth_ = GetRecommendedAtlasSize( iTotalWidth_ );
            iAtlasHeight_ = GetRecommendedAtlasSize( iTotalHeight_ );
        }//GetRecommendedAtlasWidthHeight()

        public static bool CreateTextureAtlasInfo( ref KTextureAtlasInfo textureAtlasInfo_, ETextureType eTextureType_, ArrayList alistStdMtrlInfo_ )
        {
            // create new texture atlas info.
            //
            textureAtlasInfo_ = new KTextureAtlasInfo();
            textureAtlasInfo_.m_alistTextureInfo = new ArrayList();

            int iTotalWidth = 0;
            int iTotalHeight = 0;

            // set atlas texture info.
            //
            foreach (KStdMaterialInfo stdMtrlInfo in alistStdMtrlInfo_)
            {
                KTextureInfo textrInfo;
                {
                    textrInfo.m_strMtrlName = "";
                    textrInfo.m_strTextureFileName = "";
                    textrInfo.m_iLeft = 0;
                    textrInfo.m_iTop = 0;
                    textrInfo.m_iWidth = 0;
                    textrInfo.m_iHeight = 0;
                    textrInfo.m_image = null;
                    textrInfo.m_bIsRotateCcw = false;
                }//block

                textrInfo.m_strMtrlName = stdMtrlInfo.m_strMaterialName;
                textrInfo.m_strTextureFileName = stdMtrlInfo.GetTextureFileName( eTextureType_ );
                Debug.Assert( stdMtrlInfo.m_image != null );
                //if( stdMtrlInfo.m_image == null )
                //{
                //    //return false;
                //    continue;
                //}//if

                textrInfo.m_image = stdMtrlInfo.m_image;
                if( stdMtrlInfo.m_image != null )
                {
                    textrInfo.m_iWidth = stdMtrlInfo.m_image.Width;
                    textrInfo.m_iHeight = stdMtrlInfo.m_image.Height;
                    textrInfo.m_iLeft = 0;
                    textrInfo.m_iTop = 0;

                    iTotalWidth += textrInfo.m_iWidth;
                    iTotalHeight += textrInfo.m_iHeight;
                }//if

                textureAtlasInfo_.m_alistTextureInfo.Add( textrInfo );
            }//foreach

            // set texture type, atlas width, and atlas height.
            //
            textureAtlasInfo_.m_eTextureType = eTextureType_;
            GetRecommendedAtlasWidthHeight( ref textureAtlasInfo_.m_iAtlasWidth, ref textureAtlasInfo_.m_iAtlasHeight
                , iTotalWidth / 2, iTotalHeight / 2 );

            textureAtlasInfo_.AutoAdjustTexturePosition();

            return true;
        }//CreateTextureAtlasInfo()

        /// <summary>
        /// load .odm.a file
        /// jintaeks on 2013-11-12, 17:19
        /// </summary>
        /// <param name="textureAtlasInfo_"></param>
        /// <param name="strOdmaFilePath_"></param>
        /// <returns></returns>
        public static bool LoadExistingAtlasInfo( ref KTextureAtlasInfo textureAtlasInfo_, string strOdmaFilePath_ )
        {
            if( textureAtlasInfo_ == null )
            {
                return false; // invalid atlas info.
            }//if

            if( System.IO.File.Exists( strOdmaFilePath_ ) == false )
            {
                MessageBox.Show( "파일이 존재하지 않습니다. \nPath : " + strOdmaFilePath_ );
                return false;
            }//if

            int iParseMode = 0;
            string strLine = "";
            // you must set 'Encoding.Default' to read Korean Hangul text from file. jintaeks on 2013-11-04, 14:48
            StreamReader file = new StreamReader( strOdmaFilePath_, Encoding.Default );
            while( ( strLine = file.ReadLine() ) != null )
            {
                strLine.Trim();

                if( strLine.Length <= 0 )
                {
                    continue;
                }//if

                if( iParseMode == 0 )
                {
                    int iStrLength = strLine.Length;
                    int iEqualSignIndex = strLine.IndexOf( "=" );
                    string strName = strLine.Substring( 0, iEqualSignIndex );
                    strName = strName.Trim();
                    strName = strName.ToLower();

                    int iRemainedTextLenght = iStrLength - iEqualSignIndex - 1;
                    string strData = strLine.Substring( iEqualSignIndex + 1, iRemainedTextLenght );

                    if( strName == "width" )
                    {
                        textureAtlasInfo_.m_iAtlasWidth = Convert.ToInt32( strData );
                    }
                    else if( strName == "height" )
                    {
                        textureAtlasInfo_.m_iAtlasHeight = Convert.ToInt32( strData );
                    }
                    else if( strName == "material" )
                    {
                        string[] astrMtrlInfo = strData.Split( new char[] { ',' } );

                        if( astrMtrlInfo.Length == 6 )
                        {
                            for( int iDataIndex = 0; iDataIndex < 6; iDataIndex += 1 )
                            {
                                astrMtrlInfo[iDataIndex] = astrMtrlInfo[iDataIndex].Trim();
                            }//for

                            int iTextrInfoIndex = 0;
                            bool bIsFindTextrInfo = textureAtlasInfo_.FindTextureInfo( ref iTextrInfoIndex, astrMtrlInfo[0] );
                            Debug.Assert( bIsFindTextrInfo == true );
                            if( bIsFindTextrInfo == true )
                            {
                                KTextureInfo textrInfo = new KTextureInfo();
                                bool bIsGetTextureInfo = textureAtlasInfo_.GetTextureInfo( ref textrInfo, iTextrInfoIndex );
                                if( bIsGetTextureInfo == true )
                                {
                                    textrInfo.m_iLeft = Convert.ToInt32( astrMtrlInfo[1] );
                                    textrInfo.m_iTop = Convert.ToInt32( astrMtrlInfo[2] );
                                    textrInfo.m_iWidth = Convert.ToInt32( astrMtrlInfo[3] );
                                    textrInfo.m_iHeight = Convert.ToInt32( astrMtrlInfo[4] );
                                    astrMtrlInfo[5] = astrMtrlInfo[5].ToLower();
                                    textrInfo.m_bIsRotateCcw = String.Compare( astrMtrlInfo[5], "true" ) == 0;

                                    if( textrInfo.m_bIsRotateCcw == true )
                                    {
                                        textrInfo.RotateImage( 90 );
                                    }//if

                                    textureAtlasInfo_.SetTextureInfo( iTextrInfoIndex, textrInfo );
                                }//if
                            }//if
                        }
                    }//if.. else if..
                }//if
            }//while

            file.Close();

            return true;
        }//LoadExistingAtlasInfo()

        /// <summary>  
        /// method for changing the opacity of an image  
        /// </summary>  
        /// <param name="image">image to set opacity on</param>  
        /// <param name="opacity">percentage of opacity</param>  
        /// <returns></returns>  
        public static Image SetImageOpacity( Image image, float opacity )
        {
            try
            {
                //create a Bitmap the size of the image provided  
                Bitmap bmp = new Bitmap( image.Width, image.Height );

                //create a graphics object from the image  
                using( Graphics gfx = Graphics.FromImage( bmp ) )
                {

                    //create a color matrix object  
                    ColorMatrix matrix = new ColorMatrix();

                    //set the opacity  
                    matrix.Matrix33 = opacity;

                    //create image attributes  
                    ImageAttributes attributes = new ImageAttributes();

                    //set the color(opacity) of the image  
                    attributes.SetColorMatrix( matrix, ColorMatrixFlag.Default, ColorAdjustType.Bitmap );

                    //now draw the image  
                    gfx.DrawImage( image, new Rectangle( 0, 0, bmp.Width, bmp.Height ), 0, 0, image.Width, image.Height, GraphicsUnit.Pixel, attributes );
                }
                return bmp;
            }
            catch( Exception ex )
            {
                MessageBox.Show( ex.Message );
                return null;
            }//try.. catch..
        }//SetImageOpacity()

    }//class Utility
}//namespace DsuAtlasTextureLocator
