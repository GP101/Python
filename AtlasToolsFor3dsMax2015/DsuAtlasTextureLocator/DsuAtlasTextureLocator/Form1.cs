using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
//using System.Linq;
using System.Text;
using System.Windows.Forms;
// jintaeks on 2013-11-04, 11:58
using System.Collections;
using System.IO;
using System.Threading;
using System.Diagnostics;
using FreeImageAPI; // to manipulate .dds files. jintaeks on 2013-11-04, 16:45

////////////////////////////////////////////////////////////////////////////////////////////////////
/** @brief  Dsu texture atlas texture locator.
    @date   jintaeks on 2013-11-04, 13:34 */
namespace DsuAtlasTextureLocator
{
    ////////////////////////////////////////////////////////////////////////////////////////////////////
    /** @class  FormAtlasMain
        @date   jintaeks on 2013-11-04, 13:36 */
    public partial class FormAtlasMain : Form
    {
        private enum ETextureLocatingMode
        {
            NONE,
            TEXTURE,
            ATLAS,
        }//private enum ETextureLocatingMode

        // material related members. jintaeks on 2013-11-04, 12:25
        //

        private ArrayList //<KStdMaterialInfo>
                        m_alistMaterials; // original material list.
        private string  m_strOdmFileName; // .odm file path. jintaeks on 2013-11-04, 20:45
        private ETextureType
                        m_eCurrentTextureType; // current material texture type. jintaeks on 2013-11-04, 20:45
        private int     m_iSelectedMaterialIndex;

        // atlas related members.
        //

        /** .odma file version history.
            1.0.0   - first version.
                    - atals creation failure when same texture exists in different material
            1.0.1   - revised version on jintaeks on 2013-11-18, 17:26 */
        private string  m_strOdmaFileVersion = "1.0.1";
        private int     m_iSelectedAtlasTextureIndex;
        private KTextureAtlasInfo
                        m_textureAtlasInfo; // texture atlas info constructed from 'm_alistMaterials'
        private ETextureLocatingMode
                        m_eIsTextureLocatingMode;
        private Point   m_pntPickMouseOffset; // mouse offset from left, top of selected texture.
        private float   m_fAtlasZoomRatio; // atlas texture zoom ratio from 0 to 1
        //Bitmap          m_bitmapTextureCanvas;
        private Point   m_pntAtlasLeftTop;

        ////////////////////////////////////////////////////////////////////////////////////////////////////
        // function members
        //
        public FormAtlasMain()
        {
            InitializeComponent();

            m_alistMaterials = null;// new ArrayList();
            m_strOdmFileName = "";
            m_eCurrentTextureType = ETextureType.DIFFUSE;
            m_iSelectedMaterialIndex = -1;

            m_iSelectedAtlasTextureIndex = -1;
            m_textureAtlasInfo = null;
            m_eIsTextureLocatingMode = ETextureLocatingMode.NONE;
            //m_pntPickMouseOffset;
            m_fAtlasZoomRatio = 1.0f;
            m_pntAtlasLeftTop.X = 0;
            m_pntAtlasLeftTop.Y = 0;
        }//FormAtlasMain

        private void exitToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }//exitToolStripMenuItem1_Click

        private void openToolStripMenuItem_Click(object sender, EventArgs e)
        {
            OpenOdmFile();
        }//openToolStripMenuItem_Click

        private void OpenOdmFile()
        {
            // select file to open.
            openFileDialog1.Filter = "Dsu Material Files|*.odm";
            DialogResult dResult = openFileDialog1.ShowDialog();
            if( dResult == DialogResult.Cancel )
            {
                return;
            }//if

            // load .odm file.
            bool bIsOpenOdmFile = _LoadOdmFile( openFileDialog1.FileName );
            Debug.Assert( bIsOpenOdmFile == true );
        }//OpenOdmFile()

        private bool _LoadOdmFile( string strOdmFilename_ )
        {
            // load .odm file. jintaeks on 2013-11-04, 21:04
            //
            ArrayList alistMaterials = new ArrayList();
            bool bIsReadMaterialInfo = Utility.LoadDsuMaterialInfo( ref alistMaterials, strOdmFilename_ );
            if( bIsReadMaterialInfo == true )
            {
                // step1. update material list. jintaeks on 2013-11-04, 20:40
                //
                m_alistMaterials = alistMaterials;
                m_strOdmFileName = strOdmFilename_;
                m_fAtlasZoomRatio = 1.0f;

                // update radio button state. jintaeks on 2013-11-05, 14:53
                _UpdateRadioButtonState();

                // update material list. jintaeks on 2013-11-04, 20:40
                _UpdateMaterialListbox();

                // load material textures. jintaeks on 2013-11-04, 20:41
                string strAlternativePath = Path.GetDirectoryName( m_strOdmFileName );

                // initialize texture filename.
                // jintaeks 2017-06-13_21-20
                {
                    bool bIsDiffuseTextureExist = _IsTextureTypeExistInMaterialList( ETextureType.DIFFUSE );
                    if( bIsDiffuseTextureExist )
                        Utility.LoadMaterialTextures( ref m_alistMaterials, ETextureType.DIFFUSE, strAlternativePath, false );
                    bool bIsBumpTextureExist = _IsTextureTypeExistInMaterialList( ETextureType.BUMP );
                    if( bIsBumpTextureExist )
                        Utility.LoadMaterialTextures( ref m_alistMaterials, ETextureType.BUMP, strAlternativePath, false );
                    bool bIsSpecularTextureExist = _IsTextureTypeExistInMaterialList( ETextureType.SPECULAR );
                    if( bIsSpecularTextureExist )
                        Utility.LoadMaterialTextures( ref m_alistMaterials, ETextureType.SPECULAR, strAlternativePath, false );
                    bool bIsReflectionTextureExist = _IsTextureTypeExistInMaterialList( ETextureType.GLOSSINESS );
                    if( bIsReflectionTextureExist )
                        Utility.LoadMaterialTextures( ref m_alistMaterials, ETextureType.GLOSSINESS, strAlternativePath, false );
                }

                // load material textures. jintaeks on 2013-11-04, 20:41
                Utility.LoadMaterialTextures( ref m_alistMaterials, m_eCurrentTextureType, strAlternativePath, true );

                bool bIsCreateAtlas = Utility.CreateTextureAtlasInfo( ref m_textureAtlasInfo, m_eCurrentTextureType, m_alistMaterials );

                // load existing atlas info when .odm.a file exist.
                string strOdmaFilePath = m_strOdmFileName + ".a";
                if( System.IO.File.Exists( strOdmaFilePath ) == true )
                {
                    Utility.LoadExistingAtlasInfo( ref m_textureAtlasInfo, strOdmaFilePath );
                }//if

                // update texture info. jintaeks on 2013-11-04, 20:46
                listBoxMaterials.SetSelected( 0, true ); // update default selection.
                m_iSelectedMaterialIndex = 0;
                _UpdateMaterialTextureInfo();

                m_textureAtlasInfo.AutoAdjustAtlasSize();

                //if( m_textureAtlasInfo != null )
                //{
                //    m_bitmapTextureCanvas = new Bitmap( m_textureAtlasInfo.m_iAtlasWidth, m_textureAtlasInfo.m_iAtlasHeight );
                //}//if
                _InvalidateTextureCanvas();

                return true;
            }//if

            return false;
        }//_LoadOdmFile()

        private void _UpdateRadioButtonState()
        {
            bool bIsDiffuseTextureExist = _IsTextureTypeExistInMaterialList( ETextureType.DIFFUSE );
            radioButtonDiffuseTexture.Enabled = bIsDiffuseTextureExist;
            bool bIsBumpTextureExist = _IsTextureTypeExistInMaterialList( ETextureType.BUMP );
            radioButtonBumpTexture.Enabled = bIsBumpTextureExist;
            bool bIsSpecularTextureExist = _IsTextureTypeExistInMaterialList( ETextureType.SPECULAR );
            radioButtonSpecularTexture.Enabled = bIsSpecularTextureExist;
            bool bIsReflectionTextureExist = _IsTextureTypeExistInMaterialList( ETextureType.GLOSSINESS );
            radioButtonGlossinessTexture.Enabled = bIsReflectionTextureExist;
        }//_UpdateRadioButtonState()

        private void _UpdateMaterialListbox()
        {
            // clear Object properties pane. jintaeks on 2013-11-04, 13:38
            listBoxMaterials.Items.Clear();

            // set Object properties. jintaeks on 2013-11-04, 13:38
            foreach (KStdMaterialInfo stdMtrlInfo in m_alistMaterials)
            {
                listBoxMaterials.Items.Add(stdMtrlInfo.m_strMaterialName);
            }//foreach
            m_iSelectedMaterialIndex = -1;
        }//_UpdateMaterialListbox()

        private void listBoxMaterials_SelectedIndexChanged(object sender, EventArgs e)
        {
            _UpdateMaterialTextureInfo();
        }//listBoxMaterials_SelectedIndexChanged()

        private bool _UpdateMaterialTextureInfo()
        {
            m_iSelectedMaterialIndex = listBoxMaterials.SelectedIndex;

            if( m_iSelectedMaterialIndex == -1 )
            {
                return false; // return false when selected material index is invalid. jintaeks on 2013-11-04, 20:49
            }//if

            if( m_textureAtlasInfo == null )
            {
                return false; // invalid texture atlas info. jintaeks on 2013-11-06, 14:18
            }//if

            KTextureInfo textrInfo = new KTextureInfo();
            bool bIsGetTextrInfo = m_textureAtlasInfo.GetTextureInfo( ref textrInfo, m_iSelectedMaterialIndex );
            if( bIsGetTextrInfo == false )
            {
                return false; // can't get texture info.
            }//if

            textBoxTextureFilename.Text = textrInfo.m_strTextureFileName;
            numericUpDownTextureWidth.Value = textrInfo.m_iWidth;
            numericUpDownTextureHeight.Value = textrInfo.m_iHeight;
            checkTextureRotate.Checked = textrInfo.m_bIsRotateCcw; // jintaeks on 2013-11-18, 17:32

            string strAlternativePath = Path.GetDirectoryName( m_strOdmFileName );
            _UpdateMaterialPictureBox( m_iSelectedMaterialIndex );
            _InvalidateTextureCanvas();

            return true;
        }//_UpdateMaterialTextureInfo()

        private bool _UpdateAtlasTexturesFromMaterialList()
        {
            if( m_textureAtlasInfo == null || m_textureAtlasInfo.m_alistTextureInfo == null
                || m_alistMaterials == null )
            {
                return false;
            }//if

            if( m_textureAtlasInfo.m_alistTextureInfo.Count == m_alistMaterials.Count )
            {
                int iTextrCount = m_alistMaterials.Count;
                for( int iTextr = 0; iTextr < iTextrCount; iTextr += 1 )
                {
                    KStdMaterialInfo stdMtrlInfo = ( KStdMaterialInfo )m_alistMaterials[iTextr];
                    KTextureInfo textrInfo = ( KTextureInfo )m_textureAtlasInfo.m_alistTextureInfo[iTextr];

                    textrInfo.m_image = stdMtrlInfo.m_image;
                    if( textrInfo.m_image != null && textrInfo.m_bIsRotateCcw == true )
                    {
                        textrInfo.RotateImage( 90 );
                        //textrInfo.SwapWidthHeight();
                    }//if

                    m_textureAtlasInfo.m_alistTextureInfo[iTextr] = textrInfo;
                }//for
            }//if

            return true;
        }//_UpdateAtlasTexturesFromMaterialList()

        /// @brief  find material from material list.
        /// @date   jintaeks on 2013-11-05, 20:38
        private bool _FindStdMaterialInfo( ref KStdMaterialInfo stdMtrlInfo_, string strMaterialName_ )
        {
            strMaterialName_ = strMaterialName_.ToLower();
            foreach (KStdMaterialInfo stdMtrlInfo in m_alistMaterials)
            {
                string strMtrlName = stdMtrlInfo.m_strMaterialName.ToLower();
                if (strMtrlName == strMaterialName_)
                {
                    // set [out] parameter. jintaeks on 2013-11-04, 13:59
                    stdMtrlInfo_ = stdMtrlInfo;
                    return true;
                }//if
            }//foreach

            return false;
        }//_FindStdMaterialInfo()

        private bool _IsTextureTypeExistInMaterialList( ETextureType eTextureType_ )
        {
            foreach( KStdMaterialInfo stdMtrlInfo in m_alistMaterials )
            {
                switch( eTextureType_ )
                {
                    case ETextureType.DIFFUSE:
                        if( stdMtrlInfo.m_strDiffuseTextureName.Length >= 1 )
                        {
                            return true;
                        }//if
                        break;
                    case ETextureType.BUMP:
                        if( stdMtrlInfo.m_strBumpTextureName.Length >= 1 )
                        {
                            return true;
                        }//if
                        break;
                    case ETextureType.SPECULAR:
                        if( stdMtrlInfo.m_strSpecularTextureName.Length >= 1 )
                        {
                            return true;
                        }//if
                        break;
                    case ETextureType.GLOSSINESS:
                        if( stdMtrlInfo.m_strGlossinessTextureName.Length >= 1 )
                        {
                            return true;
                        }//if
                        break;
                }//switch
            }//foreach

            return false;
        }//_IsTextureTypeExistInMaterialList()

        private void toolStripButtonOpen_Click( object sender, EventArgs e )
        {
            OpenOdmFile();
        }//toolStripButtonOpen_Click()

        private void panelTextureCanvas_Paint( object sender, PaintEventArgs e )
        {
            // draw current atlas textures. jintaeks on 2013-11-05, 20:36
            if( IsValidAtlasTextureIndex( 0 ) == true )
            {
                int iAtlasLeft = m_pntAtlasLeftTop.X;
                int iAtlasTop = m_pntAtlasLeftTop.Y;

                //Graphics g = Graphics.FromImage( m_bitmapTextureCanvas );
                Graphics g = e.Graphics;

                int iWidth = Convert.ToInt32( m_textureAtlasInfo.m_iAtlasWidth * m_fAtlasZoomRatio );
                int iHeight = Convert.ToInt32( m_textureAtlasInfo.m_iAtlasHeight * m_fAtlasZoomRatio );
                g.FillRectangle( Brushes.LightGray, iAtlasLeft, iAtlasTop, iWidth, iHeight );
                g.DrawRectangle( Pens.White, iAtlasLeft, iAtlasTop, iWidth, iHeight );

                foreach( KTextureInfo textrInfo in m_textureAtlasInfo.m_alistTextureInfo )
                {
                    int iLeft = Convert.ToInt32( textrInfo.m_iLeft * m_fAtlasZoomRatio ) + iAtlasLeft;
                    int iTop = Convert.ToInt32( textrInfo.m_iTop * m_fAtlasZoomRatio ) + iAtlasTop;
                    iWidth = Convert.ToInt32( textrInfo.m_iWidth * m_fAtlasZoomRatio );
                    iHeight = Convert.ToInt32( textrInfo.m_iHeight * m_fAtlasZoomRatio );

                    if( textrInfo.m_image != null )
                    {
                        g.DrawImage( textrInfo.m_image, iLeft, iTop, iWidth, iHeight );
                    }
                }//foreach

                int iTextrCount = m_textureAtlasInfo.m_alistTextureInfo.Count;
                for( int iTextr = 0; iTextr < iTextrCount; iTextr += 1 )
                {
                    KTextureInfo textrInfo = ( KTextureInfo )m_textureAtlasInfo.m_alistTextureInfo[iTextr];

                    int iLeft = Convert.ToInt32( textrInfo.m_iLeft * m_fAtlasZoomRatio ) + iAtlasLeft;
                    int iTop = Convert.ToInt32( textrInfo.m_iTop * m_fAtlasZoomRatio ) + iAtlasTop;
                    iWidth = Convert.ToInt32( textrInfo.m_iWidth * m_fAtlasZoomRatio );
                    iHeight = Convert.ToInt32( textrInfo.m_iHeight * m_fAtlasZoomRatio );

                    g.DrawRectangle( Pens.Magenta, iLeft, iTop, iWidth, iHeight );
                }//for

                //if( IsValidAtlasTextureIndex( m_iSelectedAtlasTextureIndex ) == true )
                //{
                //    KTextureInfo textrInfo = ( KTextureInfo )m_textureAtlasInfo.m_alistTextureInfo[m_iSelectedAtlasTextureIndex];
                //    int iLeft = Convert.ToInt32( textrInfo.m_iLeft * m_fAtlasZoomRatio );
                //    int iTop = Convert.ToInt32( textrInfo.m_iTop * m_fAtlasZoomRatio );
                //    iWidth = Convert.ToInt32( textrInfo.m_iWidth * m_fAtlasZoomRatio );
                //    iHeight = Convert.ToInt32( textrInfo.m_iHeight * m_fAtlasZoomRatio );

                //    Pen pen = new Pen( Brushes.Magenta, 2 );
                //    g.DrawRectangle( pen, iLeft, iTop, iWidth, iHeight );
                //}//if

                if( IsValidAtlasTextureIndex( m_iSelectedMaterialIndex ) == true )
                {
                    KTextureInfo textrInfo = ( KTextureInfo )m_textureAtlasInfo.m_alistTextureInfo[m_iSelectedMaterialIndex];
                    int iLeft = Convert.ToInt32( textrInfo.m_iLeft * m_fAtlasZoomRatio ) + iAtlasLeft;
                    int iTop = Convert.ToInt32( textrInfo.m_iTop * m_fAtlasZoomRatio ) + iAtlasTop;
                    iWidth = Convert.ToInt32( textrInfo.m_iWidth * m_fAtlasZoomRatio );
                    iHeight = Convert.ToInt32( textrInfo.m_iHeight * m_fAtlasZoomRatio );

                    Pen pen = new Pen( Brushes.Yellow, 2 );
                    g.DrawRectangle( pen, iLeft, iTop, iWidth, iHeight );
                }//if
            }//if
        }//panelTextureCanvas_Paint()

        private void panelTextureCanvas_Invalidated( object sender, InvalidateEventArgs e )
        {
            //if( m_bitmapTextureCanvas != null )
            //{
            //    panelTextureCanvas.BackgroundImage = m_bitmapTextureCanvas;
            //}//if
        }//panelTextureCanvas_Invalidated()

        private void _UpdateMaterialPictureBox( int iMtrl_ )
        {
            if( iMtrl_ != -1 && iMtrl_ < m_alistMaterials.Count )
            {
                KStdMaterialInfo stdMtrl = ( KStdMaterialInfo )m_alistMaterials[iMtrl_];
                //pictureBoxCurrentTexture.Image = stdMtrl.m_image;

                int iWidth = pictureBoxCurrentTexture.Width;
                int iHeight = pictureBoxCurrentTexture.Height;

                if( stdMtrl.m_image != null )
                {
                    pictureBoxCurrentTexture.Image = new Bitmap( iWidth, iHeight );
                    Graphics.FromImage( pictureBoxCurrentTexture.Image ).DrawImage( stdMtrl.m_image, 0, 0, iWidth, iHeight );
                }//if
            }//if
        }//_UpdateMaterialPictureBox()

        private void radioButtonDiffuseTexture_CheckedChanged( object sender, EventArgs e )
        {
            if( m_eCurrentTextureType != ETextureType.DIFFUSE )
            {
                m_eCurrentTextureType = ETextureType.DIFFUSE;
                _UpdateWhenTextureTypeChanged();
            }//if
        }

        private void radioButtonBumpTexture_CheckedChanged( object sender, EventArgs e )
        {
            if( m_eCurrentTextureType != ETextureType.BUMP )
            {
                m_eCurrentTextureType = ETextureType.BUMP;
                _UpdateWhenTextureTypeChanged();
            }//if
        }

        private void radioButtonSpecularTexture_CheckedChanged( object sender, EventArgs e )
        {
            if( m_eCurrentTextureType != ETextureType.SPECULAR )
            {
                m_eCurrentTextureType = ETextureType.SPECULAR;
                _UpdateWhenTextureTypeChanged();
            }//if
        }

        private void radioButtonReflectionTexture_CheckedChanged( object sender, EventArgs e )
        {
            if( m_eCurrentTextureType != ETextureType.GLOSSINESS )
            {
                m_eCurrentTextureType = ETextureType.GLOSSINESS;
                _UpdateWhenTextureTypeChanged();
            }//if
        }

        private void _UpdateWhenTextureTypeChanged()
        {
            if( m_textureAtlasInfo != null )
            {
                string strAlternativePath = Path.GetDirectoryName( m_strOdmFileName );
                Utility.LoadMaterialTextures( ref m_alistMaterials, m_eCurrentTextureType, strAlternativePath, true );
                _UpdateAtlasTexturesFromMaterialList();
                _UpdateMaterialTextureInfo();
                _InvalidateTextureCanvas();
            }//if
        }//_UpdateWhenTextureTypeChanged();

        private bool IsValidAtlasTextureIndex( int iMtrlIndex_ )
        {
            if( m_textureAtlasInfo != null && m_textureAtlasInfo.m_alistTextureInfo != null )
            {
                if( iMtrlIndex_ >= 0 && iMtrlIndex_ < m_textureAtlasInfo.m_alistTextureInfo.Count )
                {
                    return true;
                }//if
            }//if

            return false;
        }//IsValidAtlasTextureIndex()

        private bool _PickTextureOnCanvas( ref int iOutTextureIndex_, int x_, int y_ )
        {
            if( IsValidAtlasTextureIndex( 0 ) == false )
            {
                return false;
            }//if

            int iTextrCount = m_textureAtlasInfo.m_alistTextureInfo.Count;
            for( int iTextr = 0; iTextr < iTextrCount; iTextr += 1 )
            {
                KTextureInfo textrInfo = ( KTextureInfo )m_textureAtlasInfo.m_alistTextureInfo[iTextr];
                bool bIsPointIn = textrInfo.IsPointIn( x_, y_ );
                if( bIsPointIn == true )
                {
                    iOutTextureIndex_ = iTextr;
                    return true;
                }//if
            }//for

            return false;
        }//_PickTextureOnCanvas()

        private void panelTextureCanvas_MouseDown( object sender, MouseEventArgs e )
        {
            radioButtonDiffuseTexture.Focus();

            // move texture in atlas
            if( e.Button == MouseButtons.Left )
            {
                int iPickedTextr = -1;
                bool bIsPickTexture = _PickTextureOnCanvas( ref iPickedTextr
                    , ( int )( ( e.X - m_pntAtlasLeftTop.X ) / m_fAtlasZoomRatio )
                    , ( int )( ( e.Y - m_pntAtlasLeftTop.Y ) / m_fAtlasZoomRatio ) );
                if( bIsPickTexture == true )
                {
                    KTextureInfo textrInfo = new KTextureInfo();
                    bool bIsGetTextureInfo = m_textureAtlasInfo.GetTextureInfo( ref textrInfo, iPickedTextr );
                    Debug.Assert( bIsGetTextureInfo == true );
                    if( bIsGetTextureInfo == true )
                    {
                        m_pntPickMouseOffset.X = ( int )( e.X - textrInfo.m_iLeft * m_fAtlasZoomRatio ) - 1;
                        m_pntPickMouseOffset.Y = ( int )( e.Y - textrInfo.m_iTop * m_fAtlasZoomRatio ) - 1;

                        m_iSelectedAtlasTextureIndex = iPickedTextr;
                        m_eIsTextureLocatingMode = ETextureLocatingMode.TEXTURE;
                    }//if

                    // sync to material index
                    if( m_iSelectedAtlasTextureIndex != m_iSelectedMaterialIndex )
                    {
                        m_iSelectedMaterialIndex = m_iSelectedAtlasTextureIndex;
                        listBoxMaterials.SetSelected( m_iSelectedMaterialIndex, true );
                        _UpdateMaterialTextureInfo();
                    }//if
                }//if
            }
            // move atlas itself.
            else if( e.Button == MouseButtons.Right )
            {
                m_pntPickMouseOffset.X = ( int )( e.X - m_pntAtlasLeftTop.X );
                m_pntPickMouseOffset.Y = ( int )( e.Y - m_pntAtlasLeftTop.Y );
                m_eIsTextureLocatingMode = ETextureLocatingMode.ATLAS;
            }//if.. else if..
        }//panelTextureCanvas_MouseDown()

        private void panelTextureCanvas_MouseUp( object sender, MouseEventArgs e )
        {
            double fMouseX = e.X;// + cfSnapSize / 2.0;
            double fMouseY = e.Y;// +cfSnapSize / 2.0;

            bool bIsValidMtrlIndex = IsValidAtlasTextureIndex( m_iSelectedAtlasTextureIndex );
            if( bIsValidMtrlIndex == true && m_eIsTextureLocatingMode == ETextureLocatingMode.TEXTURE )
            {
                double cfSnapSize = 32;

                // apply 32*32 virtual snap to grid. jintaeks on 2013-11-06, 10:40
                KTextureInfo textrInfo = ( KTextureInfo )m_textureAtlasInfo.m_alistTextureInfo[m_iSelectedAtlasTextureIndex];
                int iSnapXIndex = ( int )( ( fMouseX - m_pntPickMouseOffset.X ) / m_fAtlasZoomRatio / cfSnapSize );
                int iSnapYIndex = ( int )( ( fMouseY - m_pntPickMouseOffset.Y ) / m_fAtlasZoomRatio / cfSnapSize );
                textrInfo.m_iLeft = ( int )( iSnapXIndex * cfSnapSize );
                textrInfo.m_iTop = ( int )( iSnapYIndex * cfSnapSize );
                m_textureAtlasInfo.SetTextureInfo( m_iSelectedAtlasTextureIndex, textrInfo );
                m_textureAtlasInfo.AutoAdjustAtlasSize();
                _InvalidateTextureCanvas();

                m_eIsTextureLocatingMode = ETextureLocatingMode.NONE;
                m_iSelectedAtlasTextureIndex = -1;
            }
            else if( m_eIsTextureLocatingMode == ETextureLocatingMode.ATLAS )
            {
                double cfSnapSize = 32;
                int iSnapXIndex = ( int )( ( fMouseX - m_pntPickMouseOffset.X ) / cfSnapSize );
                int iSnapYIndex = ( int )( ( fMouseY - m_pntPickMouseOffset.Y ) / cfSnapSize );
                m_pntAtlasLeftTop.X = ( int )( iSnapXIndex * cfSnapSize );
                m_pntAtlasLeftTop.Y = ( int )( iSnapYIndex * cfSnapSize );
                _InvalidateTextureCanvas();

                m_eIsTextureLocatingMode = ETextureLocatingMode.NONE;
            }//if.. else if..
        }

        private void panelTextureCanvas_MouseMove( object sender, MouseEventArgs e )
        {
            double fMouseX = e.X;// + cfSnapSize / 2.0;
            double fMouseY = e.Y;// +cfSnapSize / 2.0;

            bool bIsValidMtrlIndex = IsValidAtlasTextureIndex( m_iSelectedAtlasTextureIndex );

            if( bIsValidMtrlIndex == true && m_eIsTextureLocatingMode  == ETextureLocatingMode.TEXTURE )
            {
                KTextureInfo textrInfo = ( KTextureInfo )m_textureAtlasInfo.m_alistTextureInfo[m_iSelectedAtlasTextureIndex];
                textrInfo.m_iLeft = ( int )( ( fMouseX - m_pntPickMouseOffset.X ) / m_fAtlasZoomRatio );
                textrInfo.m_iTop = ( int )( ( fMouseY - m_pntPickMouseOffset.Y ) / m_fAtlasZoomRatio );
                m_textureAtlasInfo.m_alistTextureInfo[m_iSelectedAtlasTextureIndex] = textrInfo;
                _InvalidateTextureCanvas();
            }
            else if( m_eIsTextureLocatingMode == ETextureLocatingMode.ATLAS )
            {
                int iSnapXIndex = ( int )( ( fMouseX - m_pntPickMouseOffset.X ) );
                int iSnapYIndex = ( int )( ( fMouseY - m_pntPickMouseOffset.Y ) );
                m_pntAtlasLeftTop.X = iSnapXIndex;
                m_pntAtlasLeftTop.Y = iSnapYIndex;
                _InvalidateTextureCanvas();
            }//if.. else if..
        }

        private void FormAtlasMain_MouseWheel( object sender, MouseEventArgs e )
        {
            //Debug.Print( "form " + e.Delta.ToString() );

            float fOldZoomRatio = m_fAtlasZoomRatio;

            if( e.Button == MouseButtons.None )
            {
                if( e.Delta > 0 )
                {
                    m_fAtlasZoomRatio += 0.1f;
                    if( m_fAtlasZoomRatio > 1.0f )
                    {
                        m_fAtlasZoomRatio = 1.0f;
                    }//if
                }
                else
                {
                    m_fAtlasZoomRatio -= 0.1f;
                    if( m_fAtlasZoomRatio < 0.2f )
                    {
                        m_fAtlasZoomRatio = 0.2f;
                    }//if
                }//if.. else..
            }//if

            if( fOldZoomRatio != m_fAtlasZoomRatio )
            {
                _InvalidateTextureCanvas();
            }//if
        }//FormAtlasMain_MouseWheel()

        private void _InvalidateTextureCanvas()
        {
            panelTextureCanvas.Invalidate();
            toolStripStatusLabelAtlasSize.Text = String.Format( "Atlas({0}*{1})", m_textureAtlasInfo.m_iAtlasWidth, m_textureAtlasInfo.m_iAtlasHeight );
        }//_InvalidateTextureCanvas()

        private void numericUpDownTextureWidth_KeyDown( object sender, KeyEventArgs e )
        {
            if( e.KeyCode == Keys.Enter )
            {
                _UpdateAtlasTextureWidth();
            }//if
        }

        private void numericUpDownTextureWidth_MouseWheel( object sender, MouseEventArgs e )
        {
            //Debug.Print( "numericUpDownTextureWidth_MouseWheel" + e.Delta );

            if( m_textureAtlasInfo != null )
            {
                int iNewAtlasWidth = m_textureAtlasInfo.m_iAtlasWidth;
                if( e.Delta > 0 )
                {
                    iNewAtlasWidth = Convert.ToInt32( Utility.GetRecommendedAtlasSize( ( int )numericUpDownTextureWidth.Value * 2 ) );
                }
                else
                {
                    iNewAtlasWidth = Convert.ToInt32( Utility.GetRecommendedAtlasSize( ( int )numericUpDownTextureWidth.Value / 2 ) );
                }//if.. else..

                numericUpDownTextureWidth.Value = iNewAtlasWidth;
                _UpdateAtlasTextureWidth();
            }//if
        }

        private void _UpdateAtlasTextureWidth()
        {
            if( IsValidAtlasTextureIndex(0) == true )
            {
                KTextureInfo textrInfo = new KTextureInfo();
                bool bIsGetTextrInfo = m_textureAtlasInfo.GetTextureInfo( ref textrInfo, m_iSelectedMaterialIndex );
                if( bIsGetTextrInfo == true )
                {
                    int iWidth = Convert.ToInt32( numericUpDownTextureWidth.Value );
                    iWidth = Math.Min( 2048, Math.Max( 32, iWidth ) );
                    numericUpDownTextureWidth.Value = iWidth;

                    textrInfo.m_iWidth = iWidth;
                    m_textureAtlasInfo.SetTextureInfo( m_iSelectedMaterialIndex, textrInfo );
                    m_textureAtlasInfo.AutoAdjustAtlasSize();
                    _InvalidateTextureCanvas();
                }//if
            }//if
        }//_UpdateAtlasTextureWidth()

        private void _UpdateAtlasTextureHeight()
        {
            if( IsValidAtlasTextureIndex(0) == true )
            {
                KTextureInfo textrInfo = new KTextureInfo();
                bool bIsGetTextrInfo = m_textureAtlasInfo.GetTextureInfo( ref textrInfo, m_iSelectedMaterialIndex );
                if( bIsGetTextrInfo == true )
                {
                    int iHeight = Convert.ToInt32( numericUpDownTextureHeight.Value );
                    iHeight = Math.Min( 2048, Math.Max( 32, iHeight ) );
                    numericUpDownTextureHeight.Value = iHeight;

                    textrInfo.m_iHeight = iHeight;
                    m_textureAtlasInfo.SetTextureInfo( m_iSelectedMaterialIndex, textrInfo );
                    m_textureAtlasInfo.AutoAdjustAtlasSize();
                    _InvalidateTextureCanvas();
                }//if
            }//if
        }//_UpdateAtlasTextureHeight()

        private void numericUpDownTextureHeight_KeyDown( object sender, KeyEventArgs e )
        {
            if( e.KeyCode == Keys.Enter )
            {
                _UpdateAtlasTextureHeight();
            }//if
        }

        private void numericUpDownTextureHeight_MouseWheel( object sender, MouseEventArgs e )
        {
            if( m_textureAtlasInfo != null )
            {
                int iNewAtlasHeight = m_textureAtlasInfo.m_iAtlasHeight;
                if( e.Delta > 0 )
                {
                    iNewAtlasHeight = Convert.ToInt32( Utility.GetRecommendedAtlasSize( ( int )numericUpDownTextureHeight.Value * 2 ) );
                }
                else
                {
                    iNewAtlasHeight = Convert.ToInt32( Utility.GetRecommendedAtlasSize( ( int )numericUpDownTextureHeight.Value / 2 ) );
                }//if.. else..

                numericUpDownTextureHeight.Value = iNewAtlasHeight;
                _UpdateAtlasTextureHeight();
            }//if
        }

        private bool _ApplyAtlasInfo()
        {
            // step 1. write atlas info to file.
            //
            string strObjectName = Path.GetFileNameWithoutExtension( m_strOdmFileName );
            // construct "odm.a" filename.
            string strAtlasFileName = m_strOdmFileName;
            strAtlasFileName += ".a";

            StreamWriter sw = new StreamWriter( strAtlasFileName, false, Encoding.Default );
            string strData;
            string strOutput = "";

            strData = String.Format( "Version = {0}\r\n", m_strOdmaFileVersion );
            strOutput += strData;
            strData = String.Format( "Object = {0}\r\n", strObjectName );
            strOutput += strData;
            strData = String.Format( "Width = {0}\r\n", m_textureAtlasInfo.m_iAtlasWidth );
            strOutput += strData;
            strData = String.Format( "Height = {0}\r\n", m_textureAtlasInfo.m_iAtlasHeight );
            strOutput += strData;

            int iTextrCount = m_alistMaterials.Count;
            Debug.Assert( m_alistMaterials.Count == m_textureAtlasInfo.m_alistTextureInfo.Count );
            if( m_alistMaterials.Count != m_textureAtlasInfo.m_alistTextureInfo.Count )
            {
                Clipboard.SetText( "DsuAtlasTextureLocator : material error" );
                MessageBox.Show( "DsuAtlasTextureLocator : material error" );
                return false;
            }//if

            for( int iTextr = 0; iTextr < iTextrCount; iTextr += 1 )
            {
                KStdMaterialInfo stdMtrlInfo = ( KStdMaterialInfo )m_alistMaterials[iTextr];
                KTextureInfo textrInfo = ( KTextureInfo )m_textureAtlasInfo.m_alistTextureInfo[iTextr];

                strData = String.Format( "Material = {0}, {1}, {2}, {3}, {4}, {5}\r\n"
                    , textrInfo.m_strMtrlName
                    , textrInfo.m_iLeft
                    , textrInfo.m_iTop
                    , textrInfo.m_iWidth
                    , textrInfo.m_iHeight
                    , textrInfo.m_bIsRotateCcw == true ? "true" : "false" );
                strOutput += strData;

                if( stdMtrlInfo.m_strDiffuseTextureName.Length >= 1 )
                {
                    strData = String.Format( "Diffuse = {0}\r\n", stdMtrlInfo.m_strDiffuseTextureName );
                    strOutput += strData;
                }//if

                if( stdMtrlInfo.m_strBumpTextureName.Length >= 1 )
                {
                    strData = String.Format( "Bump = {0}\r\n", stdMtrlInfo.m_strBumpTextureName );
                    strOutput += strData;
                }//if

                if( stdMtrlInfo.m_strSpecularTextureName.Length >= 1 )
                {
                    strData = String.Format( "SpecularLevel = {0}\r\n", stdMtrlInfo.m_strSpecularTextureName );
                    strOutput += strData;
                }//if

                if( stdMtrlInfo.m_strGlossinessTextureName.Length >= 1 )
                {
                    strData = String.Format( "Glossiness = {0}\r\n", stdMtrlInfo.m_strGlossinessTextureName );
                    strOutput += strData;
                }//if
            }//foreach

            sw.Write( strOutput );
            sw.Close();

            // step 2. copy atlas data to clipboard.
            //
            Clipboard.SetText( strOutput );

            return true;
        }//_ApplyAtlasInfo()

        private void applyAndExitToolStripMenuItem_Click( object sender, EventArgs e )
        {
            _ApplyAtlasInfo();
            Application.Exit();
        }

        private void toolStripButtonApplyAndExit_Click( object sender, EventArgs e )
        {
            _ApplyAtlasInfo();
            Application.Exit();
        }

        private void FormAtlasMain_Shown( object sender, EventArgs e )
        {
            string[] astrArgs = Environment.GetCommandLineArgs();
            if( astrArgs.Length >= 2 )
            {
                string strOdmFileName = astrArgs[1];
                if( System.IO.File.Exists( strOdmFileName ) == true )
                {
                    _LoadOdmFile( strOdmFileName );
                }//if
            }//if
        }

        private void _UpdateAtlasTextureRotate( bool bRotateCcw_ )
        {
            if( IsValidAtlasTextureIndex( 0 ) == true )
            {
                KTextureInfo textrInfo = new KTextureInfo();
                bool bIsGetTextrInfo = m_textureAtlasInfo.GetTextureInfo( ref textrInfo, m_iSelectedMaterialIndex );
                if( bIsGetTextrInfo == true )
                {
                    if( bRotateCcw_ == true )
                    {
                        // rotate by Ccw. jintaeks on 2013-11-18, 17:08
                        if( textrInfo.m_bIsRotateCcw == false )
                        {
                            textrInfo.RotateImage( 90 ); // rotate by Ccw
                            textrInfo.SwapWidthHeight();
                            textrInfo.m_bIsRotateCcw = bRotateCcw_;
                        }//if
                    }
                    else // when ( bRotateCcw_ == false )
                    {
                        // restore rotated image. rotate by Cw. jintaeks on 2013-11-18, 17:08
                        if( textrInfo.m_bIsRotateCcw == true )
                        {
                            textrInfo.RotateImage( -90 ); // rotate by Ccw
                            textrInfo.SwapWidthHeight();
                            textrInfo.m_bIsRotateCcw = bRotateCcw_;
                        }//if
                    }//if.. else..

                    m_textureAtlasInfo.SetTextureInfo( m_iSelectedMaterialIndex, textrInfo );
                    m_textureAtlasInfo.AutoAdjustAtlasSize();
                    _InvalidateTextureCanvas();
                }//if
            }//if
        }//_UpdateAtlasTextureRotate()

        private void checkTextureRotate_CheckedChanged( object sender, EventArgs e )
        {
            _UpdateAtlasTextureRotate( checkTextureRotate.Checked );
        }

        private void numericUpDownTextureHeight_Enter( object sender, EventArgs e )
        {
            string strValue = numericUpDownTextureHeight.Value.ToString();
            numericUpDownTextureHeight.Select( 0, strValue.Length );
        }

        private void numericUpDownTextureWidth_Enter( object sender, EventArgs e )
        {
            string strValue = numericUpDownTextureWidth.Value.ToString();
            numericUpDownTextureWidth.Select( 0, strValue.Length );
        }

        void _ResizeAllTexturesInAtlas( double dResizeRatio_ )
        {
            int iTextrCount = m_alistMaterials.Count;
            for( int iTextr = 0; iTextr < iTextrCount; iTextr += 1 )
            {
                KTextureInfo textrInfo = ( KTextureInfo )m_textureAtlasInfo.m_alistTextureInfo[iTextr];

                textrInfo.m_iLeft = ( int )( textrInfo.m_iLeft * dResizeRatio_ );
                textrInfo.m_iTop = ( int )( textrInfo.m_iTop * dResizeRatio_ );
                textrInfo.m_iWidth = ( int )( textrInfo.m_iWidth * dResizeRatio_ );
                textrInfo.m_iHeight = ( int )( textrInfo.m_iHeight * dResizeRatio_ );

                m_textureAtlasInfo.m_alistTextureInfo[iTextr] = textrInfo;
            }//foreach
        }//_ResizeAllTexturesInAtlas()

        private void toolStripDropDownButton1_Click( object sender, EventArgs e )
        {
            _ResizeAllTexturesInAtlas( 0.5 );
            m_textureAtlasInfo.AutoAdjustAtlasSize();
            _InvalidateTextureCanvas();
        }

        private void toolStripDropDownButton2_Click( object sender, EventArgs e )
        {
            _ResizeAllTexturesInAtlas( 2.0 );
            m_textureAtlasInfo.AutoAdjustAtlasSize();
            _InvalidateTextureCanvas();
        }
    }//class FormAtlasMain : Form
}//namespace DsuAtlasTextureLocator
