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
        
        # PAGE 2 = OPEN FILES
        self.ui.Btn_OpenFiles_Menu.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.OpenFile_Widget))
        
        # PAGE 3 = GROUP ELEMENTS
        self.ui.Btn_GroupElm_Menu.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.GroupElm_Widget))
        
        # PAGE 4 = COMPOSITE MATERIALS
        self.ui.Btn_Composite_Menu.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.Composite_Widget))
        
        # PAGE 5 = METALLIC MATERIALS
        self.ui.Btn_Metallic_Menu.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.Metallic_Widget))
        
        # PAGE 6 = RUN
        self.ui.Btn_Run_Menu.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.Run_Widget))
        ## ==>> END        


        ## ADD CUSTOM MENUS
        ########################################################################
        self.ui.Pages_Widget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "HOME", "btn_home", "url(:/16x16/icons/16x16/cil-home.png)")
        UIFunctions.addNewMenu(self, "Add User", "btn_new_user", "url(:/16x16/icons/16x16/cil-user-follow.png)")
        UIFunctions.addNewMenu(self, "Custom Widgets", "btn_widgets", "url(:/16x16/icons/16x16/cil-equalizer.png)")
        ## ==> END ##


    ########################################################################
    ## APP EVENTS
    ########################################################################
    def mousePressEvent(self,event):
        self.dragPos = event.globalPos()
    

    ########################################################################
    ## MENUS ==> DYNAMIC MENUS FUNCTIONS
    ########################################################################
    def Button(self):
        # GET BT CLICKED
        btnWidget = self.sender()

        # PAGE HOME
        if btnWidget.objectName() == "Btn_Home":
            self.ui.Pages_Widget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "Btn_Home")
            UIFunctions.labelPage(self, "Home")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE NEW USER
        if btnWidget.objectName() == "btn_new_user":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_new_user")
            UIFunctions.labelPage(self, "New User")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE WIDGETS
        if btnWidget.objectName() == "btn_widgets":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_widgets)
            UIFunctions.resetStyle(self, "btn_widgets")
            UIFunctions.labelPage(self, "Custom Widgets")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

    ## ==> END ##
                   

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())