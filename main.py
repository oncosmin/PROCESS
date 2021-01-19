################################################################################
##
## BY: ONCESCU IONUT-COSMIN
## PROJECT MADE WITH: Qt Designer, PySide2 and SQLite
## DATE: 15.01.2021
## V: 1.0.0
## WITH THANKS TO: WANDERSON M.PIMENTA WHO DEVELOPED THE GUI BASE
## FOR THIS @APPLICATION
##
################################################################################

import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# GUI FILE
from app_modules import *

class MainWindow(QMainWindow):
    
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
                
        # MOVE WINDOW
        def moveWindow(event):
        
            # RESTORE BEFORE MOVE    
            if UIFunctions.returnStatus() == 1:
                UIFunctions.maximize_restore(self)
                
            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
                
        # SET TITLE BAR
        self.ui.Top_Frame.mouseMoveEvent = moveWindow


        # SET UI DEFINITIONS
        ########################################################################
        UIFunctions.uiDefinitions(self)

        # TOGGLE MENU
        ########################################################################
        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))
        # ==>> END
        
        
        ## PAGES LINK
        ########################################################################
        
        # PAGE 1 = HOME
        self.ui.Btn_Home_Menu.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.Home_Widget))
        self.ui.Btn_Home_Menu.clicked.connect(lambda: UIFunctions.labelPage(self,'Home'))

        # PAGE 2 = OPEN FILES
        self.ui.Btn_OpenFiles_Menu.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.OpenFile_Widget))
        self.ui.Btn_OpenFiles_Menu.clicked.connect(lambda: UIFunctions.labelPage(self,'Open Files'))

        # PAGE 3 = GROUP ELEMENTS
        self.ui.Btn_GroupElm_Menu.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.GroupElm_Widget))
        self.ui.Btn_GroupElm_Menu.clicked.connect(lambda: UIFunctions.labelPage(self,'Group Elements'))
        
        # PAGE 4 = COMPOSITE MATERIALS
        self.ui.Btn_Composite_Menu.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.Composite_Widget))
        self.ui.Btn_Composite_Menu.clicked.connect(lambda: UIFunctions.labelPage(self,'Composite Materials'))
        
        # PAGE 5 = METALLIC MATERIALS
        self.ui.Btn_Metallic_Menu.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.Metallic_Widget))
        self.ui.Btn_Metallic_Menu.clicked.connect(lambda: UIFunctions.labelPage(self,'Metallic Materials'))
        
        # PAGE 6 = RUN
        self.ui.Btn_Run_Menu.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.Run_Widget))
        self.ui.Btn_Run_Menu.clicked.connect(lambda: UIFunctions.labelPage(self,'Run Analysis'))
        
        ## ==>> END        

        ## BROWSE BUTTONS CLICKED
        ########################################################################

        # BROWSE PROCESS INPUT FILE
        self.ui.Browse_Process_File_Btn.clicked.connect(lambda: UIFunctions.browseACTION(self, self.ui.Process_Input_LineEdit, 'PROCESS'))

        # BROWSE BDF
        self.ui.Browse_BDF_File_Btn.clicked.connect(lambda: UIFunctions.browseACTION(self, self.ui.BDF_Input_LineEdit, 'BDF'))

        # BROWSE PCH
        self.ui.Browse_PCH_File_Btn.clicked.connect(lambda: UIFunctions.browseACTION(self, self.ui.PCH_Input_LineEdit, 'PCH'))
        
        # BROWSE F06.
        self.ui.Browse_F06_File_Btn.clicked.connect(lambda: UIFunctions.browseACTION(self, self.ui.F06_Input_LineEdit, 'F06'))

        ## ==>> END

    ########################################################################
    ## APP EVENTS
    ########################################################################
    def mousePressEvent(self,event):
        self.dragPos = event.globalPos()
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())