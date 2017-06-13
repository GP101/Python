namespace DsuAtlasTextureLocator
{
    partial class FormAtlasMain
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(FormAtlasMain));
            this.menuStripAtlasMain = new System.Windows.Forms.MenuStrip();
            this.fileToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.openToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.saveToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.saveasToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.exitToolStripMenuItem = new System.Windows.Forms.ToolStripSeparator();
            this.applyAndExitToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.exitToolStripMenuItem1 = new System.Windows.Forms.ToolStripMenuItem();
            this.helpToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.aboutToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripAtlasMain = new System.Windows.Forms.ToolStrip();
            this.toolStripButtonOpen = new System.Windows.Forms.ToolStripButton();
            this.toolStripButtonSave = new System.Windows.Forms.ToolStripButton();
            this.toolStripButtonApplyAndExit = new System.Windows.Forms.ToolStripButton();
            this.statusStripAtlasMain = new System.Windows.Forms.StatusStrip();
            this.toolStripStatusLabelAtlasSize = new System.Windows.Forms.ToolStripStatusLabel();
            this.toolStripDropDownButton1 = new System.Windows.Forms.ToolStripDropDownButton();
            this.toolStripDropDownButton2 = new System.Windows.Forms.ToolStripDropDownButton();
            this.panelObjectProperties = new System.Windows.Forms.Panel();
            this.labelVersion = new System.Windows.Forms.Label();
            this.labelCopyright = new System.Windows.Forms.Label();
            this.groupBoxMaterialInfo = new System.Windows.Forms.GroupBox();
            this.checkTextureRotate = new System.Windows.Forms.CheckBox();
            this.numericUpDownTextureHeight = new System.Windows.Forms.NumericUpDown();
            this.numericUpDownTextureWidth = new System.Windows.Forms.NumericUpDown();
            this.pictureBoxCurrentTexture = new System.Windows.Forms.PictureBox();
            this.labelTextureHeight = new System.Windows.Forms.Label();
            this.labelTextureWidth = new System.Windows.Forms.Label();
            this.textBoxTextureFilename = new System.Windows.Forms.TextBox();
            this.labelFilename = new System.Windows.Forms.Label();
            this.listBoxMaterials = new System.Windows.Forms.ListBox();
            this.groupBoxTextureType = new System.Windows.Forms.GroupBox();
            this.radioButtonGlossinessTexture = new System.Windows.Forms.RadioButton();
            this.radioButtonSpecularTexture = new System.Windows.Forms.RadioButton();
            this.radioButtonBumpTexture = new System.Windows.Forms.RadioButton();
            this.radioButtonDiffuseTexture = new System.Windows.Forms.RadioButton();
            this.labelObjectName = new System.Windows.Forms.Label();
            this.splitterObjectProperties = new System.Windows.Forms.Splitter();
            this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            this.saveFileDialog1 = new System.Windows.Forms.SaveFileDialog();
            this.panelTextureCanvas = new DsuAtlasTextureLocator.KMyPanel();
            this.menuStripAtlasMain.SuspendLayout();
            this.toolStripAtlasMain.SuspendLayout();
            this.statusStripAtlasMain.SuspendLayout();
            this.panelObjectProperties.SuspendLayout();
            this.groupBoxMaterialInfo.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownTextureHeight)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownTextureWidth)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBoxCurrentTexture)).BeginInit();
            this.groupBoxTextureType.SuspendLayout();
            this.SuspendLayout();
            // 
            // menuStripAtlasMain
            // 
            this.menuStripAtlasMain.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.fileToolStripMenuItem,
            this.helpToolStripMenuItem});
            this.menuStripAtlasMain.Location = new System.Drawing.Point(0, 0);
            this.menuStripAtlasMain.Name = "menuStripAtlasMain";
            this.menuStripAtlasMain.Size = new System.Drawing.Size(1090, 24);
            this.menuStripAtlasMain.TabIndex = 0;
            this.menuStripAtlasMain.Text = "menuStrip1";
            // 
            // fileToolStripMenuItem
            // 
            this.fileToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.openToolStripMenuItem,
            this.saveToolStripMenuItem,
            this.saveasToolStripMenuItem,
            this.exitToolStripMenuItem,
            this.applyAndExitToolStripMenuItem,
            this.exitToolStripMenuItem1});
            this.fileToolStripMenuItem.Name = "fileToolStripMenuItem";
            this.fileToolStripMenuItem.Size = new System.Drawing.Size(37, 20);
            this.fileToolStripMenuItem.Text = "&File";
            // 
            // openToolStripMenuItem
            // 
            this.openToolStripMenuItem.Image = global::DsuAtlasTextureLocator.Properties.Resources.directory_open;
            this.openToolStripMenuItem.Name = "openToolStripMenuItem";
            this.openToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.openToolStripMenuItem.Text = "&Open...";
            this.openToolStripMenuItem.Click += new System.EventHandler(this.openToolStripMenuItem_Click);
            // 
            // saveToolStripMenuItem
            // 
            this.saveToolStripMenuItem.Image = global::DsuAtlasTextureLocator.Properties.Resources.floppy_35inch_black;
            this.saveToolStripMenuItem.Name = "saveToolStripMenuItem";
            this.saveToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.saveToolStripMenuItem.Text = "&Save";
            // 
            // saveasToolStripMenuItem
            // 
            this.saveasToolStripMenuItem.Name = "saveasToolStripMenuItem";
            this.saveasToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.saveasToolStripMenuItem.Text = "Save &as...";
            // 
            // exitToolStripMenuItem
            // 
            this.exitToolStripMenuItem.Name = "exitToolStripMenuItem";
            this.exitToolStripMenuItem.Size = new System.Drawing.Size(149, 6);
            // 
            // applyAndExitToolStripMenuItem
            // 
            this.applyAndExitToolStripMenuItem.Image = global::DsuAtlasTextureLocator.Properties.Resources.yes;
            this.applyAndExitToolStripMenuItem.Name = "applyAndExitToolStripMenuItem";
            this.applyAndExitToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.applyAndExitToolStripMenuItem.Text = "Apply and Exit";
            this.applyAndExitToolStripMenuItem.Click += new System.EventHandler(this.applyAndExitToolStripMenuItem_Click);
            // 
            // exitToolStripMenuItem1
            // 
            this.exitToolStripMenuItem1.Name = "exitToolStripMenuItem1";
            this.exitToolStripMenuItem1.Size = new System.Drawing.Size(152, 22);
            this.exitToolStripMenuItem1.Text = "E&xit";
            this.exitToolStripMenuItem1.Click += new System.EventHandler(this.exitToolStripMenuItem1_Click);
            // 
            // helpToolStripMenuItem
            // 
            this.helpToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.aboutToolStripMenuItem});
            this.helpToolStripMenuItem.Name = "helpToolStripMenuItem";
            this.helpToolStripMenuItem.Size = new System.Drawing.Size(44, 20);
            this.helpToolStripMenuItem.Text = "&Help";
            // 
            // aboutToolStripMenuItem
            // 
            this.aboutToolStripMenuItem.Image = global::DsuAtlasTextureLocator.Properties.Resources.info;
            this.aboutToolStripMenuItem.Name = "aboutToolStripMenuItem";
            this.aboutToolStripMenuItem.Size = new System.Drawing.Size(116, 22);
            this.aboutToolStripMenuItem.Text = "&About...";
            // 
            // toolStripAtlasMain
            // 
            this.toolStripAtlasMain.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.toolStripButtonOpen,
            this.toolStripButtonSave,
            this.toolStripButtonApplyAndExit});
            this.toolStripAtlasMain.Location = new System.Drawing.Point(0, 24);
            this.toolStripAtlasMain.Name = "toolStripAtlasMain";
            this.toolStripAtlasMain.Size = new System.Drawing.Size(1090, 25);
            this.toolStripAtlasMain.TabIndex = 1;
            this.toolStripAtlasMain.Text = "toolStripAtlasMain";
            // 
            // toolStripButtonOpen
            // 
            this.toolStripButtonOpen.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolStripButtonOpen.Image = global::DsuAtlasTextureLocator.Properties.Resources.directory_open;
            this.toolStripButtonOpen.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.toolStripButtonOpen.Name = "toolStripButtonOpen";
            this.toolStripButtonOpen.Size = new System.Drawing.Size(23, 22);
            this.toolStripButtonOpen.Text = "Open";
            this.toolStripButtonOpen.Click += new System.EventHandler(this.toolStripButtonOpen_Click);
            // 
            // toolStripButtonSave
            // 
            this.toolStripButtonSave.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolStripButtonSave.Image = global::DsuAtlasTextureLocator.Properties.Resources.floppy_35inch_black;
            this.toolStripButtonSave.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.toolStripButtonSave.Name = "toolStripButtonSave";
            this.toolStripButtonSave.Size = new System.Drawing.Size(23, 22);
            this.toolStripButtonSave.Text = "Save";
            // 
            // toolStripButtonApplyAndExit
            // 
            this.toolStripButtonApplyAndExit.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolStripButtonApplyAndExit.Image = global::DsuAtlasTextureLocator.Properties.Resources.yes;
            this.toolStripButtonApplyAndExit.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.toolStripButtonApplyAndExit.Name = "toolStripButtonApplyAndExit";
            this.toolStripButtonApplyAndExit.Size = new System.Drawing.Size(23, 22);
            this.toolStripButtonApplyAndExit.Text = "Apply and Exit";
            this.toolStripButtonApplyAndExit.Click += new System.EventHandler(this.toolStripButtonApplyAndExit_Click);
            // 
            // statusStripAtlasMain
            // 
            this.statusStripAtlasMain.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.toolStripStatusLabelAtlasSize,
            this.toolStripDropDownButton1,
            this.toolStripDropDownButton2});
            this.statusStripAtlasMain.Location = new System.Drawing.Point(0, 762);
            this.statusStripAtlasMain.Name = "statusStripAtlasMain";
            this.statusStripAtlasMain.Size = new System.Drawing.Size(1090, 22);
            this.statusStripAtlasMain.TabIndex = 2;
            this.statusStripAtlasMain.Text = "statusStrip1";
            // 
            // toolStripStatusLabelAtlasSize
            // 
            this.toolStripStatusLabelAtlasSize.Name = "toolStripStatusLabelAtlasSize";
            this.toolStripStatusLabelAtlasSize.Size = new System.Drawing.Size(121, 17);
            this.toolStripStatusLabelAtlasSize.Text = "toolStripStatusLabel1";
            // 
            // toolStripDropDownButton1
            // 
            this.toolStripDropDownButton1.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolStripDropDownButton1.Image = global::DsuAtlasTextureLocator.Properties.Resources.magnifier_minus_blue;
            this.toolStripDropDownButton1.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.toolStripDropDownButton1.Name = "toolStripDropDownButton1";
            this.toolStripDropDownButton1.Size = new System.Drawing.Size(29, 20);
            this.toolStripDropDownButton1.Text = "toolStripDropDownButton1";
            this.toolStripDropDownButton1.Click += new System.EventHandler(this.toolStripDropDownButton1_Click);
            // 
            // toolStripDropDownButton2
            // 
            this.toolStripDropDownButton2.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolStripDropDownButton2.Image = global::DsuAtlasTextureLocator.Properties.Resources.magnifier_plus_blue;
            this.toolStripDropDownButton2.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.toolStripDropDownButton2.Name = "toolStripDropDownButton2";
            this.toolStripDropDownButton2.Size = new System.Drawing.Size(29, 20);
            this.toolStripDropDownButton2.Text = "toolStripDropDownButton2";
            this.toolStripDropDownButton2.Click += new System.EventHandler(this.toolStripDropDownButton2_Click);
            // 
            // panelObjectProperties
            // 
            this.panelObjectProperties.Controls.Add(this.labelVersion);
            this.panelObjectProperties.Controls.Add(this.labelCopyright);
            this.panelObjectProperties.Controls.Add(this.groupBoxMaterialInfo);
            this.panelObjectProperties.Controls.Add(this.listBoxMaterials);
            this.panelObjectProperties.Controls.Add(this.groupBoxTextureType);
            this.panelObjectProperties.Controls.Add(this.labelObjectName);
            this.panelObjectProperties.Controls.Add(this.splitterObjectProperties);
            this.panelObjectProperties.Dock = System.Windows.Forms.DockStyle.Right;
            this.panelObjectProperties.Location = new System.Drawing.Point(770, 49);
            this.panelObjectProperties.Name = "panelObjectProperties";
            this.panelObjectProperties.Size = new System.Drawing.Size(320, 713);
            this.panelObjectProperties.TabIndex = 4;
            // 
            // labelVersion
            // 
            this.labelVersion.Location = new System.Drawing.Point(11, 544);
            this.labelVersion.Name = "labelVersion";
            this.labelVersion.Size = new System.Drawing.Size(297, 24);
            this.labelVersion.TabIndex = 6;
            this.labelVersion.Text = "Version 1.0.2";
            this.labelVersion.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // labelCopyright
            // 
            this.labelCopyright.Location = new System.Drawing.Point(9, 568);
            this.labelCopyright.Name = "labelCopyright";
            this.labelCopyright.Size = new System.Drawing.Size(299, 26);
            this.labelCopyright.TabIndex = 5;
            this.labelCopyright.Text = "(C) 2017, Dicon DSU";
            this.labelCopyright.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // groupBoxMaterialInfo
            // 
            this.groupBoxMaterialInfo.Controls.Add(this.checkTextureRotate);
            this.groupBoxMaterialInfo.Controls.Add(this.numericUpDownTextureHeight);
            this.groupBoxMaterialInfo.Controls.Add(this.numericUpDownTextureWidth);
            this.groupBoxMaterialInfo.Controls.Add(this.pictureBoxCurrentTexture);
            this.groupBoxMaterialInfo.Controls.Add(this.labelTextureHeight);
            this.groupBoxMaterialInfo.Controls.Add(this.labelTextureWidth);
            this.groupBoxMaterialInfo.Controls.Add(this.textBoxTextureFilename);
            this.groupBoxMaterialInfo.Controls.Add(this.labelFilename);
            this.groupBoxMaterialInfo.Location = new System.Drawing.Point(11, 312);
            this.groupBoxMaterialInfo.Name = "groupBoxMaterialInfo";
            this.groupBoxMaterialInfo.Size = new System.Drawing.Size(297, 229);
            this.groupBoxMaterialInfo.TabIndex = 4;
            this.groupBoxMaterialInfo.TabStop = false;
            this.groupBoxMaterialInfo.Text = "Texture Info";
            // 
            // checkTextureRotate
            // 
            this.checkTextureRotate.AutoSize = true;
            this.checkTextureRotate.Location = new System.Drawing.Point(9, 146);
            this.checkTextureRotate.Name = "checkTextureRotate";
            this.checkTextureRotate.Size = new System.Drawing.Size(91, 16);
            this.checkTextureRotate.TabIndex = 9;
            this.checkTextureRotate.Text = "Rotate CCW";
            this.checkTextureRotate.UseVisualStyleBackColor = true;
            this.checkTextureRotate.CheckedChanged += new System.EventHandler(this.checkTextureRotate_CheckedChanged);
            // 
            // numericUpDownTextureHeight
            // 
            this.numericUpDownTextureHeight.Increment = new decimal(new int[] {
            0,
            0,
            0,
            0});
            this.numericUpDownTextureHeight.Location = new System.Drawing.Point(9, 119);
            this.numericUpDownTextureHeight.Maximum = new decimal(new int[] {
            2048,
            0,
            0,
            0});
            this.numericUpDownTextureHeight.Name = "numericUpDownTextureHeight";
            this.numericUpDownTextureHeight.Size = new System.Drawing.Size(97, 21);
            this.numericUpDownTextureHeight.TabIndex = 8;
            this.numericUpDownTextureHeight.Enter += new System.EventHandler(this.numericUpDownTextureHeight_Enter);
            this.numericUpDownTextureHeight.KeyDown += new System.Windows.Forms.KeyEventHandler(this.numericUpDownTextureHeight_KeyDown);
            this.numericUpDownTextureHeight.MouseWheel += new System.Windows.Forms.MouseEventHandler(this.numericUpDownTextureHeight_MouseWheel);
            // 
            // numericUpDownTextureWidth
            // 
            this.numericUpDownTextureWidth.Increment = new decimal(new int[] {
            0,
            0,
            0,
            0});
            this.numericUpDownTextureWidth.Location = new System.Drawing.Point(9, 92);
            this.numericUpDownTextureWidth.Maximum = new decimal(new int[] {
            2048,
            0,
            0,
            0});
            this.numericUpDownTextureWidth.Name = "numericUpDownTextureWidth";
            this.numericUpDownTextureWidth.Size = new System.Drawing.Size(97, 21);
            this.numericUpDownTextureWidth.TabIndex = 7;
            this.numericUpDownTextureWidth.Enter += new System.EventHandler(this.numericUpDownTextureWidth_Enter);
            this.numericUpDownTextureWidth.KeyDown += new System.Windows.Forms.KeyEventHandler(this.numericUpDownTextureWidth_KeyDown);
            this.numericUpDownTextureWidth.MouseWheel += new System.Windows.Forms.MouseEventHandler(this.numericUpDownTextureWidth_MouseWheel);
            // 
            // pictureBoxCurrentTexture
            // 
            this.pictureBoxCurrentTexture.BackColor = System.Drawing.SystemColors.ControlDark;
            this.pictureBoxCurrentTexture.Location = new System.Drawing.Point(160, 92);
            this.pictureBoxCurrentTexture.Name = "pictureBoxCurrentTexture";
            this.pictureBoxCurrentTexture.Size = new System.Drawing.Size(128, 128);
            this.pictureBoxCurrentTexture.TabIndex = 6;
            this.pictureBoxCurrentTexture.TabStop = false;
            // 
            // labelTextureHeight
            // 
            this.labelTextureHeight.AutoSize = true;
            this.labelTextureHeight.Location = new System.Drawing.Point(112, 121);
            this.labelTextureHeight.Name = "labelTextureHeight";
            this.labelTextureHeight.Size = new System.Drawing.Size(40, 12);
            this.labelTextureHeight.TabIndex = 4;
            this.labelTextureHeight.Text = "Height";
            // 
            // labelTextureWidth
            // 
            this.labelTextureWidth.AutoSize = true;
            this.labelTextureWidth.Location = new System.Drawing.Point(112, 94);
            this.labelTextureWidth.Name = "labelTextureWidth";
            this.labelTextureWidth.Size = new System.Drawing.Size(35, 12);
            this.labelTextureWidth.TabIndex = 2;
            this.labelTextureWidth.Text = "Width";
            // 
            // textBoxTextureFilename
            // 
            this.textBoxTextureFilename.Location = new System.Drawing.Point(9, 37);
            this.textBoxTextureFilename.Multiline = true;
            this.textBoxTextureFilename.Name = "textBoxTextureFilename";
            this.textBoxTextureFilename.ReadOnly = true;
            this.textBoxTextureFilename.Size = new System.Drawing.Size(282, 47);
            this.textBoxTextureFilename.TabIndex = 1;
            // 
            // labelFilename
            // 
            this.labelFilename.AutoSize = true;
            this.labelFilename.Location = new System.Drawing.Point(7, 21);
            this.labelFilename.Name = "labelFilename";
            this.labelFilename.Size = new System.Drawing.Size(57, 12);
            this.labelFilename.TabIndex = 0;
            this.labelFilename.Text = "Filename";
            // 
            // listBoxMaterials
            // 
            this.listBoxMaterials.FormattingEnabled = true;
            this.listBoxMaterials.ItemHeight = 12;
            this.listBoxMaterials.Location = new System.Drawing.Point(11, 157);
            this.listBoxMaterials.Name = "listBoxMaterials";
            this.listBoxMaterials.Size = new System.Drawing.Size(297, 148);
            this.listBoxMaterials.TabIndex = 3;
            this.listBoxMaterials.SelectedIndexChanged += new System.EventHandler(this.listBoxMaterials_SelectedIndexChanged);
            // 
            // groupBoxTextureType
            // 
            this.groupBoxTextureType.Controls.Add(this.radioButtonGlossinessTexture);
            this.groupBoxTextureType.Controls.Add(this.radioButtonSpecularTexture);
            this.groupBoxTextureType.Controls.Add(this.radioButtonBumpTexture);
            this.groupBoxTextureType.Controls.Add(this.radioButtonDiffuseTexture);
            this.groupBoxTextureType.Location = new System.Drawing.Point(11, 33);
            this.groupBoxTextureType.Name = "groupBoxTextureType";
            this.groupBoxTextureType.Size = new System.Drawing.Size(297, 117);
            this.groupBoxTextureType.TabIndex = 2;
            this.groupBoxTextureType.TabStop = false;
            this.groupBoxTextureType.Text = "Texture Type";
            // 
            // radioButtonGlossinessTexture
            // 
            this.radioButtonGlossinessTexture.AutoSize = true;
            this.radioButtonGlossinessTexture.Location = new System.Drawing.Point(7, 90);
            this.radioButtonGlossinessTexture.Name = "radioButtonGlossinessTexture";
            this.radioButtonGlossinessTexture.Size = new System.Drawing.Size(134, 16);
            this.radioButtonGlossinessTexture.TabIndex = 3;
            this.radioButtonGlossinessTexture.TabStop = true;
            this.radioButtonGlossinessTexture.Text = "Glossiness Texture";
            this.radioButtonGlossinessTexture.UseVisualStyleBackColor = true;
            this.radioButtonGlossinessTexture.CheckedChanged += new System.EventHandler(this.radioButtonReflectionTexture_CheckedChanged);
            // 
            // radioButtonSpecularTexture
            // 
            this.radioButtonSpecularTexture.AutoSize = true;
            this.radioButtonSpecularTexture.Location = new System.Drawing.Point(7, 67);
            this.radioButtonSpecularTexture.Name = "radioButtonSpecularTexture";
            this.radioButtonSpecularTexture.Size = new System.Drawing.Size(150, 16);
            this.radioButtonSpecularTexture.TabIndex = 2;
            this.radioButtonSpecularTexture.TabStop = true;
            this.radioButtonSpecularTexture.Text = "SpecularLevel Texture";
            this.radioButtonSpecularTexture.UseVisualStyleBackColor = true;
            this.radioButtonSpecularTexture.CheckedChanged += new System.EventHandler(this.radioButtonSpecularTexture_CheckedChanged);
            // 
            // radioButtonBumpTexture
            // 
            this.radioButtonBumpTexture.AutoSize = true;
            this.radioButtonBumpTexture.Location = new System.Drawing.Point(7, 44);
            this.radioButtonBumpTexture.Name = "radioButtonBumpTexture";
            this.radioButtonBumpTexture.Size = new System.Drawing.Size(103, 16);
            this.radioButtonBumpTexture.TabIndex = 1;
            this.radioButtonBumpTexture.TabStop = true;
            this.radioButtonBumpTexture.Text = "Bump Texture";
            this.radioButtonBumpTexture.UseVisualStyleBackColor = true;
            this.radioButtonBumpTexture.CheckedChanged += new System.EventHandler(this.radioButtonBumpTexture_CheckedChanged);
            // 
            // radioButtonDiffuseTexture
            // 
            this.radioButtonDiffuseTexture.AutoSize = true;
            this.radioButtonDiffuseTexture.Location = new System.Drawing.Point(7, 21);
            this.radioButtonDiffuseTexture.Name = "radioButtonDiffuseTexture";
            this.radioButtonDiffuseTexture.Size = new System.Drawing.Size(108, 16);
            this.radioButtonDiffuseTexture.TabIndex = 0;
            this.radioButtonDiffuseTexture.TabStop = true;
            this.radioButtonDiffuseTexture.Text = "Diffuse Texture";
            this.radioButtonDiffuseTexture.UseVisualStyleBackColor = true;
            this.radioButtonDiffuseTexture.CheckedChanged += new System.EventHandler(this.radioButtonDiffuseTexture_CheckedChanged);
            // 
            // labelObjectName
            // 
            this.labelObjectName.AutoSize = true;
            this.labelObjectName.Location = new System.Drawing.Point(9, 12);
            this.labelObjectName.Name = "labelObjectName";
            this.labelObjectName.Size = new System.Drawing.Size(120, 12);
            this.labelObjectName.TabIndex = 1;
            this.labelObjectName.Text = "Object Name here...";
            // 
            // splitterObjectProperties
            // 
            this.splitterObjectProperties.Location = new System.Drawing.Point(0, 0);
            this.splitterObjectProperties.Name = "splitterObjectProperties";
            this.splitterObjectProperties.Size = new System.Drawing.Size(3, 713);
            this.splitterObjectProperties.TabIndex = 0;
            this.splitterObjectProperties.TabStop = false;
            // 
            // openFileDialog1
            // 
            this.openFileDialog1.FileName = "openFileDialog1";
            // 
            // panelTextureCanvas
            // 
            this.panelTextureCanvas.BackColor = System.Drawing.SystemColors.ControlDark;
            this.panelTextureCanvas.Dock = System.Windows.Forms.DockStyle.Fill;
            this.panelTextureCanvas.Location = new System.Drawing.Point(0, 49);
            this.panelTextureCanvas.Name = "panelTextureCanvas";
            this.panelTextureCanvas.Size = new System.Drawing.Size(1090, 713);
            this.panelTextureCanvas.TabIndex = 3;
            this.panelTextureCanvas.Invalidated += new System.Windows.Forms.InvalidateEventHandler(this.panelTextureCanvas_Invalidated);
            this.panelTextureCanvas.Paint += new System.Windows.Forms.PaintEventHandler(this.panelTextureCanvas_Paint);
            this.panelTextureCanvas.MouseDown += new System.Windows.Forms.MouseEventHandler(this.panelTextureCanvas_MouseDown);
            this.panelTextureCanvas.MouseMove += new System.Windows.Forms.MouseEventHandler(this.panelTextureCanvas_MouseMove);
            this.panelTextureCanvas.MouseUp += new System.Windows.Forms.MouseEventHandler(this.panelTextureCanvas_MouseUp);
            // 
            // FormAtlasMain
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.AutoSize = true;
            this.ClientSize = new System.Drawing.Size(1090, 784);
            this.Controls.Add(this.panelObjectProperties);
            this.Controls.Add(this.panelTextureCanvas);
            this.Controls.Add(this.statusStripAtlasMain);
            this.Controls.Add(this.toolStripAtlasMain);
            this.Controls.Add(this.menuStripAtlasMain);
            this.DoubleBuffered = true;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MainMenuStrip = this.menuStripAtlasMain;
            this.Name = "FormAtlasMain";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterParent;
            this.Text = "Dsu Atlas Texture Locator";
            this.Shown += new System.EventHandler(this.FormAtlasMain_Shown);
            this.MouseWheel += new System.Windows.Forms.MouseEventHandler(this.FormAtlasMain_MouseWheel);
            this.menuStripAtlasMain.ResumeLayout(false);
            this.menuStripAtlasMain.PerformLayout();
            this.toolStripAtlasMain.ResumeLayout(false);
            this.toolStripAtlasMain.PerformLayout();
            this.statusStripAtlasMain.ResumeLayout(false);
            this.statusStripAtlasMain.PerformLayout();
            this.panelObjectProperties.ResumeLayout(false);
            this.panelObjectProperties.PerformLayout();
            this.groupBoxMaterialInfo.ResumeLayout(false);
            this.groupBoxMaterialInfo.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownTextureHeight)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownTextureWidth)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBoxCurrentTexture)).EndInit();
            this.groupBoxTextureType.ResumeLayout(false);
            this.groupBoxTextureType.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MenuStrip menuStripAtlasMain;
        private System.Windows.Forms.ToolStripMenuItem fileToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem openToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem saveToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem saveasToolStripMenuItem;
        private System.Windows.Forms.ToolStripSeparator exitToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem exitToolStripMenuItem1;
        private System.Windows.Forms.ToolStripMenuItem helpToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem aboutToolStripMenuItem;
        private System.Windows.Forms.ToolStrip toolStripAtlasMain;
        private System.Windows.Forms.ToolStripButton toolStripButtonOpen;
        private System.Windows.Forms.ToolStripButton toolStripButtonSave;
        private System.Windows.Forms.StatusStrip statusStripAtlasMain;
        private DsuAtlasTextureLocator.KMyPanel panelTextureCanvas;
        private System.Windows.Forms.Panel panelObjectProperties;
        private System.Windows.Forms.Splitter splitterObjectProperties;
        private System.Windows.Forms.GroupBox groupBoxMaterialInfo;
        private System.Windows.Forms.ListBox listBoxMaterials;
        private System.Windows.Forms.GroupBox groupBoxTextureType;
        private System.Windows.Forms.RadioButton radioButtonGlossinessTexture;
        private System.Windows.Forms.RadioButton radioButtonSpecularTexture;
        private System.Windows.Forms.RadioButton radioButtonBumpTexture;
        private System.Windows.Forms.RadioButton radioButtonDiffuseTexture;
        private System.Windows.Forms.Label labelObjectName;
        private System.Windows.Forms.Label labelCopyright;
        private System.Windows.Forms.Label labelTextureHeight;
        private System.Windows.Forms.Label labelTextureWidth;
        private System.Windows.Forms.TextBox textBoxTextureFilename;
        private System.Windows.Forms.Label labelFilename;
        private System.Windows.Forms.OpenFileDialog openFileDialog1;
        private System.Windows.Forms.SaveFileDialog saveFileDialog1;
        private System.Windows.Forms.PictureBox pictureBoxCurrentTexture;
        private System.Windows.Forms.ToolStripMenuItem applyAndExitToolStripMenuItem;
        private System.Windows.Forms.ToolStripButton toolStripButtonApplyAndExit;
        private System.Windows.Forms.NumericUpDown numericUpDownTextureHeight;
        private System.Windows.Forms.NumericUpDown numericUpDownTextureWidth;
        private System.Windows.Forms.ToolStripStatusLabel toolStripStatusLabelAtlasSize;
        private System.Windows.Forms.CheckBox checkTextureRotate;
        private System.Windows.Forms.Label labelVersion;
        private System.Windows.Forms.ToolStripDropDownButton toolStripDropDownButton1;
        private System.Windows.Forms.ToolStripDropDownButton toolStripDropDownButton2;
    }
}

