using System;
using System.Collections.Generic;
//using System.Linq;
using System.Windows.Forms;

namespace DsuAtlasTextureLocator
{
    /// <summary>
    /// jintaeks on 2013-11-13, 16:51
    /// </summary>
    public class KMyPanel : Panel
    {
        public KMyPanel()
        {
            this.DoubleBuffered = true;
        }//KMyPanel()
    }//class KMyPanel

    static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new FormAtlasMain());
        }
    }
}
