################################################################################
##
## BY: ONCESCU IONUT-COSMIN
## PROJECT MADE WITH: Qt Designer, PySide2 and SQLite
## DATE: 15.01.2021
## V: 1.0.0
## WITH THANKS TO: WANDERSON M.PIMENTA
##
################################################################################

### GUI FILE
from main import *

## ==>> GLOBALS
GLOBAL_STATE = 0
GLOBAL_TITLE_BAR = True

## ==>> COUNT INITIAL MENU
count = 1

class UIFunctions(MainWindow):
    
    
    ########################################
    # MAXIMIZE RESTORE FUNCTION
    ########################################
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        
        # IF NOT MAXIMIZED
        if status == 0:
            self.showMaximized()
            
            # SET GLOBAL TO 1
            GLOBAL_STATE = 1
            
            #IF MAXIMIZED REMOVE MARGINS
            self.ui.centralwidget.setContentsMargins(0,0,0,0)
            #self.ui.centralwidget.setStyleSheet("")
            self.ui.Btn_Maximize.setToolTip("Restore")
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.centralwidget.setContentsMargins(0,0,0,0)
            self.ui.Btn_Maximize.setToolTip("Maximize")    
        
    ########################################
    # UI DEFINITIONS
    ########################################
    def uiDefinitions(self):
        
        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        
        def doubleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QtCore.QEvent.MouseButtonDblClick:
                QtCore.QTimer.singleShot(250, lambda: UIFunctions.maximize_restore(self))
        
        # MAXIMIZE / RESTORE
        self.ui.Btn_Maximize.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        self.ui.Top_Btns_Frame.mouseDoubleClickEvent = doubleClickMaximizeRestore
        
        # MINIMIZE
        self.ui.Btn_Minimize.clicked.connect(lambda: self.showMinimized())
        
        # CLOSE APPLICATION
        self.ui.Btn_Close.clicked.connect(lambda: self.close())
        self.ui.Btn_Close.setToolTip('Close')
        
        ## ==>> CREATE SIZE GRIP TO RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.SizeGrip_Frame)
        self.sizegrip.setStyleSheet("QSizeGrip {width: 20px; height: 20px; border-radius:10px} QSizeGrip:hover {background-color: rgb(124, 138, 162)}")
        self.sizegrip.setToolTip("Resize Window")
        
    ## RETURN STATUS IF WINDOW IS MAXIMIZED OR RESTORED
    def returnStatus():
        return GLOBAL_STATE
    
    ## CHANGE PAGE LABEL TEXT
    def labelPage(self, text):
        newText = '| ' + text.upper() + '  '
        self.ui.label.setText(newText)
              
    ########################################
    # TOGGLE MENU ANIMATION
    ########################################
    
    def toggleMenu(self, maxWidth, enable):
        
        if enable:
            # GET WIDTH
            width = self.ui.Menu_Left_Frame.width()
            maxExtend = maxWidth
            # Standard width variable from qt (80px)
            standard = 80
            
            # SET MAX WIDTH
            if width == 80:
                widthExtend = maxExtend
            else:
                widthExtend = standard
            
            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.Menu_Left_Frame, b"minimumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtend)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()
            
            # ADD TEXT TO BUTTONS
            if widthExtend == maxExtend:
                UIFunctions.toggleClick(self, self.ui.Btn_Home_Menu, "url(:/24x24/icons/24x24/cil-home.png)", 'Home')
                UIFunctions.toggleClick(self, self.ui.Btn_OpenFiles_Menu, "url(:/24x24/icons/24x24/cil-folder-open.png)", 'Open Files')
                UIFunctions.toggleClick(self, self.ui.Btn_GroupElm_Menu, "url(:/24x24/icons/24x24/mesh.png)", 'Group Elements')
                UIFunctions.toggleClick(self, self.ui.Btn_Composite_Menu, "url(:/24x24/icons/24x24/composite.png)", 'Composite Materials')
                UIFunctions.toggleClick(self, self.ui.Btn_Metallic_Menu, "url(:/24x24/icons/24x24/cil-settings.png)", 'Metallic Materials')
                UIFunctions.toggleClick(self, self.ui.Btn_Run_Menu, "url(:/24x24/icons/24x24/cil-media-play.png)", 'Run Analysis')
                
            else:
                self.ui.Btn_Home_Menu.setText('')
                self.ui.Btn_OpenFiles_Menu.setText('')
                self.ui.Btn_GroupElm_Menu.setText('')
                self.ui.Btn_Composite_Menu.setText('')
                self.ui.Btn_Metallic_Menu.setText('')
                self.ui.Btn_Run_Menu.setText('')
    
    # FUNCTION TO UPDATE BUTTON WHEN EXPANDED
    def toggleClick(self, buttonUpdate, icon, nameUpdate):
        buttonUpdate.setStyleSheet(Style.style_bt_standard.replace('ICON_REPLACE', icon))
        buttonUpdate.setText(nameUpdate)
         
    ########################################
    # BROWSE FUNCTIONS
    ########################################
    
    def browseACTION(self,lineEditName,fileName):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select "+ fileName +" file", "", fileName+" Files (*."+fileName.lower()+")")
        if fileName:
            lineEditName.clear()
            lineEditName.setText(fileName)