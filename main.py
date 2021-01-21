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
    
    ########################################################################
    ## MAIN WINDOW DEFINITION
    ########################################################################
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
        # ==>> END

        # TOGGLE MENU
        ########################################################################
        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))
        # ==>> END
        
        
        ## PAGES LINK / MENU BUTTONS CLICKED
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
        
        ##-----------------------------------------------------------------------
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
        
        ##-----------------------------------------------------------------------
        ## ==>> END
        
        
        ## ADD BUTTONS CLICKED
        ########################################################################
        
        # ADD GROUP ELEMENTS TO TABLE
        self.ui.AddGroup_Btn.clicked.connect(lambda: UIFunctions.addActionGroup(self,self.ui.GroupName_LineEdit.text(),\
            self.ui.GroupElms_LineEdit.text(),self.ui.GroupElm_TableWidget,['Group Name','Elements']))
        
                
        # ADD COMPOSITE MATERIAL FACING VALUES TO TABLE
        self.ui.CompFacing_Add_Btn.clicked.connect(lambda: UIFunctions.addActionCompositeFacing(self, self.ui.CompFacing_MatID_LineEdit.text(),\
            self.ui.CompFacing_FOSu_LineEdit.text(),self.ui.Material_Facing_TableWidget,['Composite Material Facing ID','FOSu']))
        
        # ADD COMPOSITE MATERIAL CORE VALUES TO TABLE
        self.ui.CompCore_Add_Btn.clicked.connect(lambda: UIFunctions.addActionCompositeCore(self,self.ui.CompCore_MatID_LineEdit.text(),\
            self.ui.CompCore_FsL_LineEdit.text(),self.ui.CompCore_FsW_LineEdit.text(),self.ui.CompCore_FOSu_LineEdit.text(),\
                self.ui.CompCore_TableWidget,['Composite Material Core ID', 'FsL','FsW','FOSu']))
        
        # ADD METALLIC MATERIAL VALUES TO TABLE
        self.ui.Metallic_Add_Btn.clicked.connect(lambda: UIFunctions.addActionMetallic(self, self.ui.Metallic_MatID_LineEdit.text(),\
            self.ui.Metallic_FOSy_LineEdit.text(),self.ui.Metallic_FOSu_LineEdit.text(),\
                self.ui.Metallic_TableWidget,['Metallic Material ID','FOSy','FOSu']))       
        
        ## DELETE BUTTONS CLICKED
        ########################################################################
        
        # DELETE GROUP ELEMENTS TABLE ROW
        self.ui.DelGroup_Btn.clicked.connect(lambda: UIFunctions.delActionButton(self,self.ui.GroupElm_TableWidget))
        
        # DELETE COMPOSITE MATERIAL FACING TABLE ROW
        self.ui.CompFacing_Del_Btn.clicked.connect(lambda: UIFunctions.delActionButton(self,self.ui.Material_Facing_TableWidget))
        
        # DELETE COMPOSITE MATERIAL CORE TABLE ROW
        self.ui.CompCore_Del_Btn.clicked.connect(lambda: UIFunctions.delActionButton(self,self.ui.CompCore_TableWidget))
        
        # DELETE METALLIC MATERIAL TABLE ROW
        self.ui.Metallic_Del_Btn.clicked.connect(lambda: UIFunctions.delActionButton(self,self.ui.Metallic_TableWidget))
        
        ##-----------------------------------------------------------------------
        ## ==>> END
        
        ## SAVE PROCESS BUTTON CLICKED
        ########################################################################
        self.ui.Save_Input_File_Btn.clicked.connect(lambda: UIFunctions.SaveFunction(self,self.ui.Save_Input_File_LineEdit.text(),\
            self.ui.BDF_Input_LineEdit.text(),self.ui.F06_Input_LineEdit.text(),self.ui.PCH_Input_LineEdit.text(),self.ui.GroupElm_TableWidget,\
                self.ui.Material_Facing_TableWidget,self.ui.CompCore_TableWidget,self.ui.Metallic_TableWidget))
        
        
        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##
    
    
    ########################################################################
    ## EVENTS
    ########################################################################
    def mousePressEvent(self,event):
        self.dragPos = event.globalPos()
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    #window.show()
    sys.exit(app.exec_())