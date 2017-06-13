using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Collections;
using System.IO;
using System.Threading;
using System.Diagnostics;
using FreeImageAPI; // to manipulate .dds files. jintaeks on 2013-11-04, 16:45

namespace DsuAtlasTextureLocator
{
    /** @struct KTextureInfo
        @date   jintaeks on 2013-11-05, 15:40 */
    public struct KTextureInfo
    {
        public string   m_strMtrlName;
        public string   m_strTextureFileName;
        public int      m_iLeft;
        public int      m_iTop;
        public int      m_iWidth;
        public int      m_iHeight;
        public Image    m_image;
        public bool     m_bIsRotateCcw; ///< rotate by counter clockwise. jintaeks on 2013-11-18, 16:29

        public KTextureInfo( string strTextureFileName_ )
        {
            m_strMtrlName = "";
            m_strTextureFileName = strTextureFileName_;
            m_iLeft = 0;
            m_iTop = 0;
            m_iWidth = 0;
            m_iHeight = 0;
            m_image = null;
            m_bIsRotateCcw = false;
        }//KTextureInfo

        public bool IsPointIn( int x_, int y_ )
        {
            int iRight = m_iLeft + m_iWidth - 1;
            int iBottom = m_iTop + m_iHeight - 1;
            return ( x_ >= m_iLeft && x_ <= iRight && y_ >= m_iTop && y_ <= iBottom );
        }//IsPointIn()

        /// <summary>
        /// rotate image by dAngleDegree_
        /// </summary>
        /// <param name="dAngle_"> rotatio angle in degree </param>
        /// <returns></returns>
        public bool RotateImage( double dAngleDegree_ )
        {
            if( m_image != null )
            {
                FIBITMAP newFiBitmap = FreeImage.CreateFromBitmap( ( Bitmap )m_image );
                newFiBitmap = FreeImage.Rotate( newFiBitmap, dAngleDegree_ ); // rotate by Ccw
                m_image = FreeImage.GetBitmap( newFiBitmap );

                return true;
            }//if

            return false;
        }//RotateImageCcw()

        public void SwapWidthHeight()
        {
            int iTemp = m_iWidth;
            m_iWidth = m_iHeight;
            m_iHeight = iTemp;
        }//SwapWidthHeight()
    }//struct KTextureInfo

    /** @class  KTextureAtlasInfo
        @date   jintaeks on 2013-11-05, 15:40 */
    public class KTextureAtlasInfo
    {
        public ETextureType
                        m_eTextureType;
        public int      m_iAtlasWidth;
        public int      m_iAtlasHeight;
        public ArrayList
                        m_alistTextureInfo; // <KTextureInfo>

        public KTextureAtlasInfo()
        {
            m_eTextureType = ETextureType.DIFFUSE;
            m_iAtlasWidth = 0;
            m_iAtlasHeight = 0;
        }//KTextureAtlasInfo()

        /// <summary>
        /// automatically adjust texture positions when atlas size is fixed.
        /// jintaeks on 2013-11-06, 17:18
        /// </summary>
        /// <returns></returns>
        public bool AutoAdjustTexturePosition()
        {
            if( m_iAtlasWidth <= 0 || m_iAtlasHeight <= 0 )
            {
                return false;
            }//if

            int iNumTextures = m_alistTextureInfo.Count;
            int iNumRowTextures = ( int )Math.Log( iNumTextures, 2 );
            if( iNumRowTextures <= 0 )
            {
                return false;
            }//if

            int iWidthStep = m_iAtlasWidth / iNumRowTextures;
            int iHeightStep = m_iAtlasHeight / iNumRowTextures;

            int iTextrCounter = 0;
            int iTextrLeft = 0;
            int iTextrLeftNext = 0;
            int iTextrTop = 0;
            int iTextrHeightMaxSoFar = 0;

            for( int iTextr = 0; iTextr < iNumTextures; ++iTextr )
            {
                KTextureInfo textrInfo = ( KTextureInfo )m_alistTextureInfo[iTextr];

                iTextrLeftNext = iTextrLeft + Math.Min( iWidthStep, textrInfo.m_iWidth );
                iTextrCounter += 1;
                if( iTextrLeftNext > m_iAtlasWidth )
                {
                    iTextrLeft = 0;
                    iTextrLeftNext = Math.Min( iWidthStep, textrInfo.m_iWidth );
                    iTextrTop += iTextrHeightMaxSoFar;
                    iTextrHeightMaxSoFar = 0;
                }//if
                textrInfo.m_iLeft = iTextrLeft;
                textrInfo.m_iTop = iTextrTop;
                iTextrLeft = iTextrLeftNext;

                iTextrHeightMaxSoFar = Math.Max( iTextrHeightMaxSoFar, textrInfo.m_iHeight );

                // update modified texture info.
                m_alistTextureInfo[iTextr] = textrInfo;
            }//for

            return true;
        }//AutoAdjustTexturePosition()

        public void AutoAdjustAtlasSize()
        {
            int iMaxWidthSoFar = 0;
            int iMaxHeightSoFar = 0;
            foreach( KTextureInfo textrInfo in m_alistTextureInfo )
            {
                int iRight = textrInfo.m_iLeft + textrInfo.m_iWidth;
                iMaxWidthSoFar = Math.Max( iMaxWidthSoFar, iRight );
                int iBottom = textrInfo.m_iTop + textrInfo.m_iHeight;
                iMaxHeightSoFar = Math.Max( iMaxHeightSoFar, iBottom );
            }//foreach

            m_iAtlasWidth = Utility.GetRecommendedAtlasSize( iMaxWidthSoFar );
            m_iAtlasHeight = Utility.GetRecommendedAtlasSize( iMaxHeightSoFar );
        }//AutoAdjustAtlasSize()

        /// <summary>
        /// get texture info at specified texture index.
        /// jintaeks on 2013-11-06, 17:19
        /// </summary>
        /// <param name="textrInfo_"></param>
        /// <param name="iTextrIndex_"></param>
        /// <returns></returns>
        public bool GetTextureInfo( ref KTextureInfo textrInfo_, int iTextrIndex_ )
        {
            if( m_alistTextureInfo == null )
            {
                return false;
            }//if

            if( iTextrIndex_ >= 0 && iTextrIndex_ < m_alistTextureInfo.Count )
            {
                // set [out] parameter.
                textrInfo_ = ( KTextureInfo )m_alistTextureInfo[iTextrIndex_];
                return true;
            }//if

            return false;
        }//GetTextureInfo()

        public bool SetTextureInfo( int iTextrIndex_, KTextureInfo textrInfo_ )
        {
            if( m_alistTextureInfo == null )
            {
                return false;
            }//if

            if( iTextrIndex_ >= 0 && iTextrIndex_ < m_alistTextureInfo.Count )
            {
                m_alistTextureInfo[iTextrIndex_] = textrInfo_;
                return true;
            }//if

            return false;
        }//SetTextureInfo()

        public bool FindTextureInfo( ref int iTextrInfo_, string strMtrlName_ )
        {
            if( m_alistTextureInfo == null )
            {
                return false; // invalid texture info list.
            }//if

            int iNumTextures = m_alistTextureInfo.Count;
            for( int iTextr = 0; iTextr < iNumTextures; ++iTextr )
            {
                KTextureInfo textrInfo = ( KTextureInfo )m_alistTextureInfo[iTextr];
                if( textrInfo.m_strMtrlName == strMtrlName_ )
                {
                    iTextrInfo_ = iTextr;
                    return true;
                }//if
            }//for

            return false;
        }//FindTextureInfo()
    }//struct KTextureAtlasInfo
}//namespace DsuAtlasTextureLocator
