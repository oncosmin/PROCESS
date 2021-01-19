# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui_styles import Style

import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 650)
        MainWindow.setMinimumSize(QSize(1000, 650))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"background-color: rgb(43, 45, 66);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1000, 650))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Frame = QFrame(self.centralwidget)
        self.Top_Frame.setObjectName(u"Top_Frame")
        self.Top_Frame.setMaximumSize(QSize(16777215, 60))
        self.Top_Frame.setStyleSheet(u"background-color: rgb(35, 35, 45);")
        self.Top_Frame.setFrameShape(QFrame.NoFrame)
        self.Top_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Toggle_Frame = QFrame(self.Top_Frame)
        self.Toggle_Frame.setObjectName(u"Toggle_Frame")
        self.Toggle_Frame.setMaximumSize(QSize(80, 60))
        self.Toggle_Frame.setFrameShape(QFrame.NoFrame)
        self.Toggle_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Toggle_Frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QPushButton(self.Toggle_Frame)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        self.Btn_Toggle.setFocusPolicy(Qt.NoFocus)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(35, 35, 45);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(43, 45, 66);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(239, 35, 60);\n"
"}")

        self.verticalLayout_2.addWidget(self.Btn_Toggle)


        self.horizontalLayout.addWidget(self.Toggle_Frame)

        self.Top_Right_Frame = QFrame(self.Top_Frame)
        self.Top_Right_Frame.setObjectName(u"Top_Right_Frame")
        self.Top_Right_Frame.setMaximumSize(QSize(16777215, 60))
        self.Top_Right_Frame.setFrameShape(QFrame.NoFrame)
        self.Top_Right_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.Top_Right_Frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Top_Btns_Frame = QFrame(self.Top_Right_Frame)
        self.Top_Btns_Frame.setObjectName(u"Top_Btns_Frame")
        self.Top_Btns_Frame.setMinimumSize(QSize(0, 40))
        self.Top_Btns_Frame.setFrameShape(QFrame.NoFrame)
        self.Top_Btns_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.Top_Btns_Frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Window_Text_Fram = QFrame(self.Top_Btns_Frame)
        self.Window_Text_Fram.setObjectName(u"Window_Text_Fram")
        self.Window_Text_Fram.setFrameShape(QFrame.StyledPanel)
        self.Window_Text_Fram.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.Window_Text_Fram)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Icon_Frame = QFrame(self.Window_Text_Fram)
        self.Icon_Frame.setObjectName(u"Icon_Frame")
        self.Icon_Frame.setMinimumSize(QSize(40, 40))
        self.Icon_Frame.setMaximumSize(QSize(40, 40))
        self.Icon_Frame.setStyleSheet(u"background: transparent;\n"
"background-image: url(:/20x20/icons/20x20/cil-3d.png);\n"
"/*background-image: url(:/20x20/icons/20x20/cil-credit-card.png);*/\n"
"\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.Icon_Frame.setFrameShape(QFrame.StyledPanel)
        self.Icon_Frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.Icon_Frame)

        self.App_Name_Label = QLabel(self.Window_Text_Fram)
        self.App_Name_Label.setObjectName(u"App_Name_Label")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.App_Name_Label.setFont(font)
        self.App_Name_Label.setStyleSheet(u"color: rgb(225, 225, 225);")
        self.App_Name_Label.setMidLineWidth(0)

        self.horizontalLayout_6.addWidget(self.App_Name_Label)


        self.horizontalLayout_4.addWidget(self.Window_Text_Fram)

        self.Window_Btns_Frame = QFrame(self.Top_Btns_Frame)
        self.Window_Btns_Frame.setObjectName(u"Window_Btns_Frame")
        self.Window_Btns_Frame.setMinimumSize(QSize(0, 0))
        self.Window_Btns_Frame.setMaximumSize(QSize(120, 16777215))
        self.Window_Btns_Frame.setFrameShape(QFrame.NoFrame)
        self.Window_Btns_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.Window_Btns_Frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Btn_Minimize = QPushButton(self.Window_Btns_Frame)
        self.Btn_Minimize.setObjectName(u"Btn_Minimize")
        self.Btn_Minimize.setFocusPolicy(Qt.NoFocus)
        self.Btn_Minimize.setMinimumSize(QSize(40, 0))
        self.Btn_Minimize.setMaximumSize(QSize(40, 16777215))
        self.Btn_Minimize.setStyleSheet(u"QPushButton {\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(35, 35, 45);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(43, 45, 66);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(217, 4, 41);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_Minimize.setIcon(icon)
        self.Btn_Minimize.setIconSize(QSize(40, 40))

        self.horizontalLayout_5.addWidget(self.Btn_Minimize)

        self.Btn_Maximize = QPushButton(self.Window_Btns_Frame)
        self.Btn_Maximize.setObjectName(u"Btn_Maximize")
        self.Btn_Maximize.setFocusPolicy(Qt.NoFocus)
        self.Btn_Maximize.setStyleSheet(u"QPushButton {\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(35, 35, 45);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(43, 45, 66);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(217, 4, 41);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_Maximize.setIcon(icon1)
        self.Btn_Maximize.setIconSize(QSize(40, 40))

        self.horizontalLayout_5.addWidget(self.Btn_Maximize)

        self.Btn_Close = QPushButton(self.Window_Btns_Frame)
        self.Btn_Close.setObjectName(u"Btn_Close")
        self.Btn_Close.setFocusPolicy(Qt.NoFocus)
        self.Btn_Close.setStyleSheet(u"QPushButton {\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(35, 35, 45);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(43, 45, 66);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(217, 4, 41);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_Close.setIcon(icon2)
        self.Btn_Close.setIconSize(QSize(40, 40))

        self.horizontalLayout_5.addWidget(self.Btn_Close)


        self.horizontalLayout_4.addWidget(self.Window_Btns_Frame)


        self.verticalLayout_6.addWidget(self.Top_Btns_Frame)

        self.Top_Info_Frame = QFrame(self.Top_Right_Frame)
        self.Top_Info_Frame.setObjectName(u"Top_Info_Frame")
        self.Top_Info_Frame.setMinimumSize(QSize(0, 20))
        self.Top_Info_Frame.setStyleSheet(u"background-color: rgb(40, 42, 62);")
        self.Top_Info_Frame.setFrameShape(QFrame.NoFrame)
        self.Top_Info_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.Top_Info_Frame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.Top_Info_Frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(141, 153, 174);")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_7.addWidget(self.label)


        self.verticalLayout_6.addWidget(self.Top_Info_Frame)


        self.horizontalLayout.addWidget(self.Top_Right_Frame)


        self.verticalLayout.addWidget(self.Top_Frame)

        self.Content_Frame = QFrame(self.centralwidget)
        self.Content_Frame.setObjectName(u"Content_Frame")
        self.Content_Frame.setFrameShape(QFrame.NoFrame)
        self.Content_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content_Frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Menu_Left_Frame = QFrame(self.Content_Frame)
        self.Menu_Left_Frame.setObjectName(u"Menu_Left_Frame")
        self.Menu_Left_Frame.setMinimumSize(QSize(80, 0))
        self.Menu_Left_Frame.setMaximumSize(QSize(80, 16777215))
        self.Menu_Left_Frame.setStyleSheet(u"background-color: rgb(35, 35, 45);")
        self.Menu_Left_Frame.setFrameShape(QFrame.NoFrame)
        self.Menu_Left_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.Menu_Left_Frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Top_Menus_Frame = QFrame(self.Menu_Left_Frame)
        self.Top_Menus_Frame.setObjectName(u"Top_Menus_Frame")
        self.Top_Menus_Frame.setMinimumSize(QSize(80, 0))
        self.Top_Menus_Frame.setFrameShape(QFrame.NoFrame)
        self.Top_Menus_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.Top_Menus_Frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Btn_Home_Menu = QPushButton(self.Top_Menus_Frame)
        self.Btn_Home_Menu.setObjectName(u"Btn_Home_Menu")
        self.Btn_Home_Menu.setFocusPolicy(Qt.NoFocus)
        self.Btn_Home_Menu.setMinimumSize(QSize(0, 70))
        self.Btn_Home_Menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-home.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(35, 35, 45);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(43, 45, 66);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(239, 35, 60);\n"
"}")

        self.verticalLayout_4.addWidget(self.Btn_Home_Menu)

        self.Btn_OpenFiles_Menu = QPushButton(self.Top_Menus_Frame)
        self.Btn_OpenFiles_Menu.setObjectName(u"Btn_OpenFiles_Menu")
        self.Btn_OpenFiles_Menu.setFocusPolicy(Qt.NoFocus)
        self.Btn_OpenFiles_Menu.setMinimumSize(QSize(0, 70))
        self.Btn_OpenFiles_Menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-folder-open.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(35, 35, 45);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(43, 45, 66);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(239, 35, 60);\n"
"}")

        self.verticalLayout_4.addWidget(self.Btn_OpenFiles_Menu)

        self.Btn_GroupElm_Menu = QPushButton(self.Top_Menus_Frame)
        self.Btn_GroupElm_Menu.setObjectName(u"Btn_GroupElm_Menu")
        self.Btn_GroupElm_Menu.setFocusPolicy(Qt.NoFocus)
        self.Btn_GroupElm_Menu.setMinimumSize(QSize(0, 70))
        self.Btn_GroupElm_Menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/mesh.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(35, 35, 45);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(43, 45, 66);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(239, 35, 60);\n"
"}")

        self.verticalLayout_4.addWidget(self.Btn_GroupElm_Menu)

        self.Btn_Composite_Menu = QPushButton(self.Top_Menus_Frame)
        self.Btn_Composite_Menu.setObjectName(u"Btn_Composite_Menu")
        self.Btn_Composite_Menu.setFocusPolicy(Qt.NoFocus)
        self.Btn_Composite_Menu.setMinimumSize(QSize(0, 70))
        self.Btn_Composite_Menu.setStyleSheet(u"QPushButton {\n"
"	\n"
"	background-image: url(:/24x24/icons/24x24/composite.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(35, 35, 45);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(43, 45, 66);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(239, 35, 60);\n"
"}")

        self.verticalLayout_4.addWidget(self.Btn_Composite_Menu)

        self.Btn_Metallic_Menu = QPushButton(self.Top_Menus_Frame)
        self.Btn_Metallic_Menu.setObjectName(u"Btn_Metallic_Menu")
        self.Btn_Metallic_Menu.setFocusPolicy(Qt.NoFocus)
        self.Btn_Metallic_Menu.setMinimumSize(QSize(0, 70))
        self.Btn_Metallic_Menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-settings.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(35, 35, 45);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(43, 45, 66);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(239, 35, 60);\n"
"}")

        self.verticalLayout_4.addWidget(self.Btn_Metallic_Menu)

        self.Btn_Run_Menu = QPushButton(self.Top_Menus_Frame)
        self.Btn_Run_Menu.setObjectName(u"Btn_Run_Menu")
        self.Btn_Run_Menu.setFocusPolicy(Qt.NoFocus)
        self.Btn_Run_Menu.setMinimumSize(QSize(0, 70))
        self.Btn_Run_Menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-media-play.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(35, 35, 45);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(43, 45, 66);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(239, 35, 60);\n"
"}")

        self.verticalLayout_4.addWidget(self.Btn_Run_Menu)


        self.verticalLayout_3.addWidget(self.Top_Menus_Frame, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.Menu_Left_Frame)

        self.Pages_Frame = QFrame(self.Content_Frame)
        self.Pages_Frame.setObjectName(u"Pages_Frame")
        self.Pages_Frame.setStyleSheet(u"")
        self.Pages_Frame.setFrameShape(QFrame.NoFrame)
        self.Pages_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.Pages_Frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Pages_Widget = QStackedWidget(self.Pages_Frame)
        self.Pages_Widget.setObjectName(u"Pages_Widget")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        self.Pages_Widget.setFont(font1)
        self.Pages_Widget.setStyleSheet(u"color: rgb(237, 242, 244);\n"
"")
        self.Pages_Widget.setLocale(QLocale(QLocale.English, QLocale.Kenya))
        self.Home_Widget = QWidget()
        self.Home_Widget.setObjectName(u"Home_Widget")
        self.Home_Widget.setMinimumSize(QSize(0, 0))
        self.Home_Widget.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.Home_Widget)
        self.verticalLayout_8.setSpacing(15)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(15, 15, 15, 15)
        self.Home_Label = QLabel(self.Home_Widget)
        self.Home_Label.setObjectName(u"Home_Label")
        self.Home_Label.setMaximumSize(QSize(16777215, 80))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(23)
        font2.setBold(True)
        font2.setWeight(75)
        self.Home_Label.setFont(font2)
        self.Home_Label.setStyleSheet(u"background-color: rgb(40, 42, 62);\n"
"border-radius:10px;\n"
"")
        self.Home_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.Home_Label)

        self.AppDescription_Label = QLabel(self.Home_Widget)
        self.AppDescription_Label.setObjectName(u"AppDescription_Label")
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(12)
        self.AppDescription_Label.setFont(font3)
        self.AppDescription_Label.setStyleSheet(u"background-color: rgb(40, 42, 62);\n"
"border-radius:10px;\n"
"")
        self.AppDescription_Label.setFrameShape(QFrame.Box)
        self.AppDescription_Label.setAlignment(Qt.AlignCenter)
        self.AppDescription_Label.setMargin(4)

        self.verticalLayout_8.addWidget(self.AppDescription_Label)

        self.Copyright_Label = QLabel(self.Home_Widget)
        self.Copyright_Label.setObjectName(u"Copyright_Label")
        self.Copyright_Label.setMinimumSize(QSize(0, 80))
        self.Copyright_Label.setMaximumSize(QSize(16777215, 80))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(8)
        self.Copyright_Label.setFont(font4)
        self.Copyright_Label.setStyleSheet(u"background-color: rgb(40, 42, 62);\n"
"border-radius:10px;\n"
"color: rgb(141, 153, 174);\n"
"")
        self.Copyright_Label.setFrameShape(QFrame.NoFrame)
        self.Copyright_Label.setTextFormat(Qt.AutoText)
        self.Copyright_Label.setScaledContents(False)
        self.Copyright_Label.setAlignment(Qt.AlignJustify|Qt.AlignTop)
        self.Copyright_Label.setWordWrap(True)
        self.Copyright_Label.setMargin(7)
        self.Copyright_Label.setIndent(0)

        self.verticalLayout_8.addWidget(self.Copyright_Label)

        self.Pages_Widget.addWidget(self.Home_Widget)
        self.OpenFile_Widget = QWidget()
        self.OpenFile_Widget.setObjectName(u"OpenFile_Widget")
        self.OpenFile_Widget.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_9 = QVBoxLayout(self.OpenFile_Widget)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(15, 15, 15, 180)
        self.OpenInput_Frame = QFrame(self.OpenFile_Widget)
        self.OpenInput_Frame.setObjectName(u"OpenInput_Frame")
        self.OpenInput_Frame.setMaximumSize(QSize(16777215, 125))
        self.OpenInput_Frame.setStyleSheet(u"background-color: rgb(40, 42, 62);\n"
"border-radius:10px;\n"
"")
        self.OpenInput_Frame.setFrameShape(QFrame.StyledPanel)
        self.OpenInput_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.OpenInput_Frame)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.Process_File_Frame = QFrame(self.OpenInput_Frame)
        self.Process_File_Frame.setObjectName(u"Process_File_Frame")
        self.Process_File_Frame.setMaximumSize(QSize(16777215, 28))
        self.Process_File_Frame.setFrameShape(QFrame.StyledPanel)
        self.Process_File_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.Process_File_Frame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 0, 5, 0)
        self.Process_File_Label = QLabel(self.Process_File_Frame)
        self.Process_File_Label.setObjectName(u"Process_File_Label")
        self.Process_File_Label.setFont(font)
        self.Process_File_Label.setStyleSheet(u"color: rgb(214, 214, 214);")
        self.Process_File_Label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Process_File_Label.setMargin(5)

        self.horizontalLayout_7.addWidget(self.Process_File_Label)


        self.verticalLayout_10.addWidget(self.Process_File_Frame)

        self.Process_Input_Btn_Frame = QFrame(self.OpenInput_Frame)
        self.Process_Input_Btn_Frame.setObjectName(u"Process_Input_Btn_Frame")
        self.Process_Input_Btn_Frame.setFrameShape(QFrame.StyledPanel)
        self.Process_Input_Btn_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.Process_Input_Btn_Frame)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(5, 0, 5, 0)
        self.Process_Input_LineEdit = QLineEdit(self.Process_Input_Btn_Frame)
        self.Process_Input_LineEdit.setObjectName(u"Process_Input_LineEdit")
        self.Process_Input_LineEdit.setMinimumSize(QSize(0, 30))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(9)
        self.Process_Input_LineEdit.setFont(font5)
        self.Process_Input_LineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(35, 35, 45);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(35, 35, 45);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_8.addWidget(self.Process_Input_LineEdit)

        self.Browse_Process_File_Btn = QPushButton(self.Process_Input_Btn_Frame)
        self.Browse_Process_File_Btn.setObjectName(u"Browse_Process_File_Btn")
        self.Browse_Process_File_Btn.setFocusPolicy(Qt.NoFocus)
        self.Browse_Process_File_Btn.setMinimumSize(QSize(200, 30))
        self.Browse_Process_File_Btn.setMaximumSize(QSize(200, 30))
        self.Browse_Process_File_Btn.setFont(font5)
        self.Browse_Process_File_Btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(217, 4, 41);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.On)
        self.Browse_Process_File_Btn.setIcon(icon3)
        self.Browse_Process_File_Btn.setIconSize(QSize(16, 16))

        self.horizontalLayout_8.addWidget(self.Browse_Process_File_Btn)


        self.verticalLayout_10.addWidget(self.Process_Input_Btn_Frame)

        self.Add_Input_File_Frame = QFrame(self.OpenInput_Frame)
        self.Add_Input_File_Frame.setObjectName(u"Add_Input_File_Frame")
        self.Add_Input_File_Frame.setFrameShape(QFrame.NoFrame)
        self.Add_Input_File_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.Add_Input_File_Frame)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(5, 0, 5, 0)
        self.Add_Input_File_Btn = QPushButton(self.Add_Input_File_Frame)
        self.Add_Input_File_Btn.setObjectName(u"Add_Input_File_Btn")
        self.Add_Input_File_Btn.setFocusPolicy(Qt.NoFocus)
        self.Add_Input_File_Btn.setMinimumSize(QSize(100, 20))
        self.Add_Input_File_Btn.setMaximumSize(QSize(100, 30))
        self.Add_Input_File_Btn.setFont(font5)
        self.Add_Input_File_Btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(217, 4, 41);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.horizontalLayout_12.addWidget(self.Add_Input_File_Btn)


        self.verticalLayout_10.addWidget(self.Add_Input_File_Frame, 0, Qt.AlignLeft)


        self.verticalLayout_9.addWidget(self.OpenInput_Frame)

        self.OpenResults_Frame = QFrame(self.OpenFile_Widget)
        self.OpenResults_Frame.setObjectName(u"OpenResults_Frame")
        self.OpenResults_Frame.setMaximumSize(QSize(16777215, 220))
        self.OpenResults_Frame.setStyleSheet(u"background-color: rgb(40, 42, 62);\n"
"border-radius:10px;\n"
"")
        self.OpenResults_Frame.setFrameShape(QFrame.StyledPanel)
        self.OpenResults_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.OpenResults_Frame)
        self.verticalLayout_11.setSpacing(4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.OPEN_Label_Frame = QFrame(self.OpenResults_Frame)
        self.OPEN_Label_Frame.setObjectName(u"OPEN_Label_Frame")
        self.OPEN_Label_Frame.setMaximumSize(QSize(16777215, 40))
        self.OPEN_Label_Frame.setFrameShape(QFrame.StyledPanel)
        self.OPEN_Label_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.OPEN_Label_Frame)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(5, 0, 5, 0)
        self.Open_Results_Label = QLabel(self.OPEN_Label_Frame)
        self.Open_Results_Label.setObjectName(u"Open_Results_Label")
        self.Open_Results_Label.setMaximumSize(QSize(16777215, 40))
        self.Open_Results_Label.setFont(font)
        self.Open_Results_Label.setStyleSheet(u"color: rgb(214, 214, 214);")
        self.Open_Results_Label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Open_Results_Label.setMargin(5)

        self.verticalLayout_12.addWidget(self.Open_Results_Label)


        self.verticalLayout_11.addWidget(self.OPEN_Label_Frame)

        self.BDF_Btns_Frame = QFrame(self.OpenResults_Frame)
        self.BDF_Btns_Frame.setObjectName(u"BDF_Btns_Frame")
        self.BDF_Btns_Frame.setMaximumSize(QSize(16777215, 40))
        self.BDF_Btns_Frame.setFrameShape(QFrame.StyledPanel)
        self.BDF_Btns_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.BDF_Btns_Frame)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(5, 0, 5, 0)
        self.BDF_Input_LineEdit = QLineEdit(self.BDF_Btns_Frame)
        self.BDF_Input_LineEdit.setObjectName(u"BDF_Input_LineEdit")
        self.BDF_Input_LineEdit.setMinimumSize(QSize(0, 30))
        self.BDF_Input_LineEdit.setFont(font5)
        self.BDF_Input_LineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(35, 35, 45);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(35, 35, 45);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_9.addWidget(self.BDF_Input_LineEdit)

        self.Browse_BDF_File_Btn = QPushButton(self.BDF_Btns_Frame)
        self.Browse_BDF_File_Btn.setObjectName(u"Browse_BDF_File_Btn")
        self.Browse_BDF_File_Btn.setFocusPolicy(Qt.NoFocus)
        self.Browse_BDF_File_Btn.setMinimumSize(QSize(200, 30))
        self.Browse_BDF_File_Btn.setMaximumSize(QSize(200, 30))
        self.Browse_BDF_File_Btn.setFont(font5)
        self.Browse_BDF_File_Btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(217, 4, 41);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.Browse_BDF_File_Btn.setIcon(icon3)
        self.Browse_BDF_File_Btn.setIconSize(QSize(16, 16))

        self.horizontalLayout_9.addWidget(self.Browse_BDF_File_Btn)


        self.verticalLayout_11.addWidget(self.BDF_Btns_Frame)

        self.F06_Btns_Frame = QFrame(self.OpenResults_Frame)
        self.F06_Btns_Frame.setObjectName(u"F06_Btns_Frame")
        self.F06_Btns_Frame.setMaximumSize(QSize(16777215, 40))
        self.F06_Btns_Frame.setFrameShape(QFrame.StyledPanel)
        self.F06_Btns_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.F06_Btns_Frame)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 5, 0)
        self.F06_Input_LineEdit = QLineEdit(self.F06_Btns_Frame)
        self.F06_Input_LineEdit.setObjectName(u"F06_Input_LineEdit")
        self.F06_Input_LineEdit.setMinimumSize(QSize(0, 30))
        self.F06_Input_LineEdit.setFont(font5)
        self.F06_Input_LineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(35, 35, 45);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(35, 35, 45);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_10.addWidget(self.F06_Input_LineEdit)

        self.Browse_F06_File_Btn = QPushButton(self.F06_Btns_Frame)
        self.Browse_F06_File_Btn.setObjectName(u"Browse_F06_File_Btn")
        self.Browse_F06_File_Btn.setFocusPolicy(Qt.NoFocus)
        self.Browse_F06_File_Btn.setMinimumSize(QSize(200, 30))
        self.Browse_F06_File_Btn.setMaximumSize(QSize(200, 30))
        self.Browse_F06_File_Btn.setFont(font5)
        self.Browse_F06_File_Btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(217, 4, 41);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.Browse_F06_File_Btn.setText(u"Browse .F06 File")
        self.Browse_F06_File_Btn.setIcon(icon3)
        self.Browse_F06_File_Btn.setIconSize(QSize(16, 16))

        self.horizontalLayout_10.addWidget(self.Browse_F06_File_Btn)


        self.verticalLayout_11.addWidget(self.F06_Btns_Frame)

        self.PCH_Btns_Frame = QFrame(self.OpenResults_Frame)
        self.PCH_Btns_Frame.setObjectName(u"PCH_Btns_Frame")
        self.PCH_Btns_Frame.setMaximumSize(QSize(16777215, 40))
        self.PCH_Btns_Frame.setFrameShape(QFrame.StyledPanel)
        self.PCH_Btns_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.PCH_Btns_Frame)
        self.horizontalLayout_11.setSpacing(5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(5, 0, 5, 0)
        self.PCH_Input_LineEdit = QLineEdit(self.PCH_Btns_Frame)
        self.PCH_Input_LineEdit.setObjectName(u"PCH_Input_LineEdit")
        self.PCH_Input_LineEdit.setMinimumSize(QSize(0, 30))
        self.PCH_Input_LineEdit.setFont(font5)
        self.PCH_Input_LineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(35, 35, 45);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(35, 35, 45);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_11.addWidget(self.PCH_Input_LineEdit)

        self.Browse_PCH_File_Btn = QPushButton(self.PCH_Btns_Frame)
        self.Browse_PCH_File_Btn.setObjectName(u"Browse_PCH_File_Btn")
        self.Browse_PCH_File_Btn.setFocusPolicy(Qt.NoFocus)
        self.Browse_PCH_File_Btn.setMinimumSize(QSize(200, 30))
        self.Browse_PCH_File_Btn.setMaximumSize(QSize(200, 30))
        self.Browse_PCH_File_Btn.setFont(font5)
        self.Browse_PCH_File_Btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(217, 4, 41);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.Browse_PCH_File_Btn.setIcon(icon3)
        self.Browse_PCH_File_Btn.setIconSize(QSize(16, 16))

        self.horizontalLayout_11.addWidget(self.Browse_PCH_File_Btn)


        self.verticalLayout_11.addWidget(self.PCH_Btns_Frame)


        self.verticalLayout_9.addWidget(self.OpenResults_Frame)

        self.Pages_Widget.addWidget(self.OpenFile_Widget)
        self.GroupElm_Widget = QWidget()
        self.GroupElm_Widget.setObjectName(u"GroupElm_Widget")
        self.verticalLayout_13 = QVBoxLayout(self.GroupElm_Widget)
        self.verticalLayout_13.setSpacing(15)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(15, 15, 15, 15)
        self.AddGroup_Frame = QFrame(self.GroupElm_Widget)
        self.AddGroup_Frame.setObjectName(u"AddGroup_Frame")
        self.AddGroup_Frame.setMinimumSize(QSize(0, 180))
        self.AddGroup_Frame.setMaximumSize(QSize(16777215, 270))
        self.AddGroup_Frame.setStyleSheet(u"background-color: rgb(40, 42, 62);\n"
"border-radius:10px;\n"
"")
        self.AddGroup_Frame.setFrameShape(QFrame.StyledPanel)
        self.AddGroup_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.AddGroup_Frame)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.GroupName_Frame = QFrame(self.AddGroup_Frame)
        self.GroupName_Frame.setObjectName(u"GroupName_Frame")
        self.GroupName_Frame.setFrameShape(QFrame.StyledPanel)
        self.GroupName_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.GroupName_Frame)
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(10, 0, 10, 0)
        self.GroupName_Label = QLabel(self.GroupName_Frame)
        self.GroupName_Label.setObjectName(u"GroupName_Label")
        self.GroupName_Label.setMinimumSize(QSize(150, 0))
        self.GroupName_Label.setMaximumSize(QSize(150, 16777215))
        self.GroupName_Label.setFont(font)
        self.GroupName_Label.setStyleSheet(u"color: rgb(214, 214, 214);")
        self.GroupName_Label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.GroupName_Label)

        self.GroupName_LineEdit = QLineEdit(self.GroupName_Frame)
        self.GroupName_LineEdit.setObjectName(u"GroupName_LineEdit")
        self.GroupName_LineEdit.setMinimumSize(QSize(0, 30))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(9)
        font6.setItalic(False)
        self.GroupName_LineEdit.setFont(font6)
        self.GroupName_LineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(35, 35, 45);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(35, 35, 45);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_14.addWidget(self.GroupName_LineEdit)


        self.verticalLayout_14.addWidget(self.GroupName_Frame)

        self.GroupElms_Frame = QFrame(self.AddGroup_Frame)
        self.GroupElms_Frame.setObjectName(u"GroupElms_Frame")
        self.GroupElms_Frame.setFrameShape(QFrame.StyledPanel)
        self.GroupElms_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.GroupElms_Frame)
        self.horizontalLayout_13.setSpacing(10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(10, 0, 10, 0)
        self.GroupElms_Label = QLabel(self.GroupElms_Frame)
        self.GroupElms_Label.setObjectName(u"GroupElms_Label")
        self.GroupElms_Label.setMinimumSize(QSize(150, 0))
        self.GroupElms_Label.setMaximumSize(QSize(150, 16777215))
        self.GroupElms_Label.setFont(font)
        self.GroupElms_Label.setStyleSheet(u"color: rgb(214, 214, 214);")
        self.GroupElms_Label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.GroupElms_Label)

        self.GroupElms_LineEdit = QLineEdit(self.GroupElms_Frame)
        self.GroupElms_LineEdit.setObjectName(u"GroupElms_LineEdit")
        self.GroupElms_LineEdit.setMinimumSize(QSize(0, 30))
        self.GroupElms_LineEdit.setFont(font5)
        self.GroupElms_LineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(35, 35, 45);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(35, 35, 45);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_13.addWidget(self.GroupElms_LineEdit)


        self.verticalLayout_14.addWidget(self.GroupElms_Frame)

        self.Add_Btns_Frame = QFrame(self.AddGroup_Frame)
        self.Add_Btns_Frame.setObjectName(u"Add_Btns_Frame")
        self.Add_Btns_Frame.setFrameShape(QFrame.StyledPanel)
        self.Add_Btns_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.Add_Btns_Frame)
        self.horizontalLayout_15.setSpacing(10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(200, 0, 200, 0)
        self.AddGroup_Btn = QPushButton(self.Add_Btns_Frame)
        self.AddGroup_Btn.setObjectName(u"AddGroup_Btn")
        self.AddGroup_Btn.setFocusPolicy(Qt.NoFocus)
        self.AddGroup_Btn.setMinimumSize(QSize(100, 30))
        self.AddGroup_Btn.setMaximumSize(QSize(100, 30))
        self.AddGroup_Btn.setFont(font5)
        self.AddGroup_Btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(217, 4, 41);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.horizontalLayout_15.addWidget(self.AddGroup_Btn)

        self.DelGroup_Btn = QPushButton(self.Add_Btns_Frame)
        self.DelGroup_Btn.setObjectName(u"DelGroup_Btn")
        self.DelGroup_Btn.setFocusPolicy(Qt.NoFocus)
        self.DelGroup_Btn.setMinimumSize(QSize(100, 30))
        self.DelGroup_Btn.setMaximumSize(QSize(100, 30))
        self.DelGroup_Btn.setFont(font5)
        self.DelGroup_Btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(217, 4, 41);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.horizontalLayout_15.addWidget(self.DelGroup_Btn)


        self.verticalLayout_14.addWidget(self.Add_Btns_Frame)


        self.verticalLayout_13.addWidget(self.AddGroup_Frame)

        self.GroupElm_Table_Frem = QFrame(self.GroupElm_Widget)
        self.GroupElm_Table_Frem.setObjectName(u"GroupElm_Table_Frem")
        self.GroupElm_Table_Frem.setStyleSheet(u"background-color: rgb(40, 42, 62);\n"
"\n"
"")
        self.GroupElm_Table_Frem.setFrameShape(QFrame.StyledPanel)
        self.GroupElm_Table_Frem.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.GroupElm_Table_Frem)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        
        ## GROUP ELMEMENTS TABLE WIDGET DEFINTION
        ##################################################################
        
        self.GroupElm_TableWidget = QTableWidget(self.GroupElm_Table_Frem)
        self.GroupElm_TableWidget.setObjectName(u"GroupElm_TableWidget")
        self.GroupElm_TableWidget.setStyleSheet(Style.style_table_standard)
        self.GroupElm_TableWidget.setFrameShape(QFrame.NoFrame)
        self.GroupElm_TableWidget.horizontalHeader().setVisible(True)
        self.GroupElm_TableWidget.horizontalHeader().setHighlightSections(True)
        self.GroupElm_TableWidget.verticalHeader().setVisible(False)
        self.GroupElm_TableWidget.setFocusPolicy(Qt.NoFocus)
        self.GroupElm_TableWidget.horizontalHeader().setStretchLastSection(True)
           
        self.verticalLayout_15.addWidget(self.GroupElm_TableWidget)
        self.verticalLayout_13.addWidget(self.GroupElm_Table_Frem)
       
        ##################################################################
        ## END TABLE DEFINITION

        self.Pages_Widget.addWidget(self.GroupElm_Widget)
        self.Composite_Widget = QWidget()
        self.Composite_Widget.setObjectName(u"Composite_Widget")
        self.verticalLayout_16 = QVBoxLayout(self.Composite_Widget)
        self.verticalLayout_16.setSpacing(15)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(15, 15, 15, 15)
        self.Material_Facing_Frame = QFrame(self.Composite_Widget)
        self.Material_Facing_Frame.setObjectName(u"Material_Facing_Frame")
        self.Material_Facing_Frame.setMaximumSize(QSize(16777215, 180))
        self.Material_Facing_Frame.setStyleSheet(u"background-color: rgb(40, 42, 62);\n"
"border-radius:10px;")
        self.Material_Facing_Frame.setFrameShape(QFrame.StyledPanel)
        self.Material_Facing_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.Material_Facing_Frame)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.Comp_Facing_Btns_Frame = QFrame(self.Material_Facing_Frame)
        self.Comp_Facing_Btns_Frame.setObjectName(u"Comp_Facing_Btns_Frame")
        self.Comp_Facing_Btns_Frame.setMinimumSize(QSize(430, 0))
        self.Comp_Facing_Btns_Frame.setMaximumSize(QSize(430, 16777215))
        self.Comp_Facing_Btns_Frame.setFrameShape(QFrame.NoFrame)
        self.Comp_Facing_Btns_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.Comp_Facing_Btns_Frame)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(10, 10, 10, 10)
        self.Comp_Facing_Label = QLabel(self.Comp_Facing_Btns_Frame)
        self.Comp_Facing_Label.setObjectName(u"Comp_Facing_Label")
        self.Comp_Facing_Label.setMaximumSize(QSize(400, 30))
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(11)
        font7.setBold(True)
        font7.setWeight(75)
        self.Comp_Facing_Label.setFont(font7)
        self.Comp_Facing_Label.setStyleSheet(u"color: rgb(214, 214, 214);")
        self.Comp_Facing_Label.setAlignment(Qt.AlignLeft)
        self.Comp_Facing_Label.setMargin(0)
        self.Comp_Facing_Label.setIndent(0)

        self.verticalLayout_17.addWidget(self.Comp_Facing_Label)

        self.Comp_Facing_MatID_Frame = QFrame(self.Comp_Facing_Btns_Frame)
        self.Comp_Facing_MatID_Frame.setObjectName(u"Comp_Facing_MatID_Frame")
        self.Comp_Facing_MatID_Frame.setMinimumSize(QSize(0, 50))
        self.Comp_Facing_MatID_Frame.setMaximumSize(QSize(400, 50))
        self.Comp_Facing_MatID_Frame.setStyleSheet(u"color: rgb(214, 214, 214);")
        self.Comp_Facing_MatID_Frame.setFrameShape(QFrame.StyledPanel)
        self.Comp_Facing_MatID_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.Comp_Facing_MatID_Frame)
        self.horizontalLayout_18.setSpacing(10)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.CompFacing_MatID_Label = QLabel(self.Comp_Facing_MatID_Frame)
        self.CompFacing_MatID_Label.setObjectName(u"CompFacing_MatID_Label")
        self.CompFacing_MatID_Label.setMinimumSize(QSize(50, 0))
        self.CompFacing_MatID_Label.setMaximumSize(QSize(80, 16777215))
        self.CompFacing_MatID_Label.setFont(font)
        self.CompFacing_MatID_Label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_18.addWidget(self.CompFacing_MatID_Label)

        self.CompFacing_MatID_LineEdit = QLineEdit(self.Comp_Facing_MatID_Frame)
        self.CompFacing_MatID_LineEdit.setObjectName(u"CompFacing_MatID_LineEdit")
        self.CompFacing_MatID_LineEdit.setMinimumSize(QSize(150, 30))
        self.CompFacing_MatID_LineEdit.setMaximumSize(QSize(150, 30))
        self.CompFacing_MatID_LineEdit.setFont(font5)
        self.CompFacing_MatID_LineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(35, 35, 45);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(35, 35, 45);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_18.addWidget(self.CompFacing_MatID_LineEdit)

        self.CompFacing_Add_Btn = QPushButton(self.Comp_Facing_MatID_Frame)
        self.CompFacing_Add_Btn.setObjectName(u"CompFacing_Add_Btn")
        self.CompFacing_Add_Btn.setFocusPolicy(Qt.NoFocus)
        self.CompFacing_Add_Btn.setMinimumSize(QSize(100, 30))
        self.CompFacing_Add_Btn.setMaximumSize(QSize(100, 30))
        self.CompFacing_Add_Btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(217, 4, 41);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.horizontalLayout_18.addWidget(self.CompFacing_Add_Btn)


        self.verticalLayout_17.addWidget(self.Comp_Facing_MatID_Frame)

        self.Comp_Facing_FOSu_Frame = QFrame(self.Comp_Facing_Btns_Frame)
        self.Comp_Facing_FOSu_Frame.setObjectName(u"Comp_Facing_FOSu_Frame")
        self.Comp_Facing_FOSu_Frame.setMinimumSize(QSize(0, 50))
        self.Comp_Facing_FOSu_Frame.setMaximumSize(QSize(400, 50))
        self.Comp_Facing_FOSu_Frame.setFrameShape(QFrame.StyledPanel)
        self.Comp_Facing_FOSu_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.Comp_Facing_FOSu_Frame)
        self.horizontalLayout_19.setSpacing(10)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.CompFacing_FOSu_Label = QLabel(self.Comp_Facing_FOSu_Frame)
        self.CompFacing_FOSu_Label.setObjectName(u"CompFacing_FOSu_Label")
        self.CompFacing_FOSu_Label.setMinimumSize(QSize(80, 0))
        self.CompFacing_FOSu_Label.setMaximumSize(QSize(50, 16777215))
        self.CompFacing_FOSu_Label.setFont(font)
        self.CompFacing_FOSu_Label.setStyleSheet(u"color: rgb(214, 214, 214);")
        self.CompFacing_FOSu_Label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_19.addWidget(self.CompFacing_FOSu_Label)

        self.CompFacing_FOSu_LineEdit = QLineEdit(self.Comp_Facing_FOSu_Frame)
        self.CompFacing_FOSu_LineEdit.setObjectName(u"CompFacing_FOSu_LineEdit")
        self.CompFacing_FOSu_LineEdit.setMinimumSize(QSize(150, 30))
        self.CompFacing_FOSu_LineEdit.setMaximumSize(QSize(150, 30))
        self.CompFacing_FOSu_LineEdit.setFont(font5)
        self.CompFacing_FOSu_LineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(35, 35, 45);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(35, 35, 45);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_19.addWidget(self.CompFacing_FOSu_LineEdit)

        self.CompFacing_Del_Btn = QPushButton(self.Comp_Facing_FOSu_Frame)
        self.CompFacing_Del_Btn.setObjectName(u"CompFacing_Del_Btn")
        self.CompFacing_Del_Btn.setFocusPolicy(Qt.NoFocus)
        self.CompFacing_Del_Btn.setMinimumSize(QSize(100, 30))
        self.CompFacing_Del_Btn.setMaximumSize(QSize(100, 30))
        self.CompFacing_Del_Btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(217, 4, 41);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.horizontalLayout_19.addWidget(self.CompFacing_Del_Btn)


        self.verticalLayout_17.addWidget(self.Comp_Facing_FOSu_Frame)


        self.horizontalLayout_16.addWidget(self.Comp_Facing_Btns_Frame, 0, Qt.AlignHCenter)

        self.Material_Facing_Table_Frame = QFrame(self.Material_Facing_Frame)
        self.Material_Facing_Table_Frame.setObjectName(u"Material_Facing_Table_Frame")
        self.Material_Facing_Table_Frame.setMaximumSize(QSize(16777215, 16777215))
        self.Material_Facing_Table_Frame.setFrameShape(QFrame.StyledPanel)
        self.Material_Facing_Table_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.Material_Facing_Table_Frame)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(10, 10, 10, 10)
        self.Material_Facing_TableWidget = QTableWidget(self.Material_Facing_Table_Frame)
        self.Material_Facing_TableWidget.setObjectName(u"Material_Facing_TableWidget")
        self.Material_Facing_TableWidget.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(40, 42, 62);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(141, 153, 174);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QT"
                        "ableView::horizontalHeader {	\n"
"	background-color: rgb(239, 35, 60);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.Material_Facing_TableWidget.setFrameShape(QFrame.NoFrame)
        self.Material_Facing_TableWidget.horizontalHeader().setVisible(False)
        self.Material_Facing_TableWidget.horizontalHeader().setHighlightSections(True)
        self.Material_Facing_TableWidget.verticalHeader().setVisible(False)

        self.horizontalLayout_17.addWidget(self.Material_Facing_TableWidget)


        self.horizontalLayout_16.addWidget(self.Material_Facing_Table_Frame)


        self.verticalLayout_16.addWidget(self.Material_Facing_Frame)

        self.Material_Core_Frame = QFrame(self.Composite_Widget)
        self.Material_Core_Frame.setObjectName(u"Material_Core_Frame")
        self.Material_Core_Frame.setStyleSheet(u"background-color: rgb(40, 42, 62);\n"
"border-radius:10px;")
        self.Material_Core_Frame.setFrameShape(QFrame.StyledPanel)
        self.Material_Core_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.Material_Core_Frame)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.Comp_Core_Frame = QFrame(self.Material_Core_Frame)
        self.Comp_Core_Frame.setObjectName(u"Comp_Core_Frame")
        self.Comp_Core_Frame.setMaximumSize(QSize(350, 350))
        self.Comp_Core_Frame.setFrameShape(QFrame.StyledPanel)
        self.Comp_Core_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.Comp_Core_Frame)
        self.verticalLayout_18.setSpacing(10)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(10, 10, 10, 10)
        self.Comp_Core_Label_Frame = QFrame(self.Comp_Core_Frame)
        self.Comp_Core_Label_Frame.setObjectName(u"Comp_Core_Label_Frame")
        self.Comp_Core_Label_Frame.setFrameShape(QFrame.StyledPanel)
        self.Comp_Core_Label_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.Comp_Core_Label_Frame)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, -1, 10, -1)
        self.CompCore_Label = QLabel(self.Comp_Core_Label_Frame)
        self.CompCore_Label.setObjectName(u"CompCore_Label")
        self.CompCore_Label.setMinimumSize(QSize(0, 30))
        self.CompCore_Label.setMaximumSize(QSize(400, 30))
        self.CompCore_Label.setFont(font7)
        self.CompCore_Label.setStyleSheet(u"color: rgb(214, 214, 214);")
        self.CompCore_Label.setAlignment(Qt.AlignLeft)

        self.verticalLayout_19.addWidget(self.CompCore_Label)


        self.verticalLayout_18.addWidget(self.Comp_Core_Label_Frame)

        self.Comp_Core_MatID_Frame = QFrame(self.Comp_Core_Frame)
        self.Comp_Core_MatID_Frame.setObjectName(u"Comp_Core_MatID_Frame")
        self.Comp_Core_MatID_Frame.setMaximumSize(QSize(16777215, 50))
        self.Comp_Core_MatID_Frame.setFrameShape(QFrame.StyledPanel)
        self.Comp_Core_MatID_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.Comp_Core_MatID_Frame)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.CompCore_MatID_Label = QLabel(self.Comp_Core_MatID_Frame)
        self.CompCore_MatID_Label.setObjectName(u"CompCore_MatID_Label")
        self.CompCore_MatID_Label.setMinimumSize(QSize(50, 0))
        self.CompCore_MatID_Label.setMaximumSize(QSize(80, 16777215))
        self.CompCore_MatID_Label.setFont(font)
        self.CompCore_MatID_Label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_21.addWidget(self.CompCore_MatID_Label)

        self.CompCore_MatID_LineEdit = QLineEdit(self.Comp_Core_MatID_Frame)
        self.CompCore_MatID_LineEdit.setObjectName(u"CompCore_MatID_LineEdit")
        self.CompCore_MatID_LineEdit.setMinimumSize(QSize(150, 30))
        self.CompCore_MatID_LineEdit.setMaximumSize(QSize(150, 30))
        self.CompCore_MatID_LineEdit.setFont(font5)
        self.CompCore_MatID_LineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(35, 35, 45);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(35, 35, 45);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_21.addWidget(self.CompCore_MatID_LineEdit)


        self.verticalLayout_18.addWidget(self.Comp_Core_MatID_Frame)

        self.Comp_Core_FsL_Frame = QFrame(self.Comp_Core_Frame)
        self.Comp_Core_FsL_Frame.setObjectName(u"Comp_Core_FsL_Frame")
        self.Comp_Core_FsL_Frame.setMaximumSize(QSize(16777215, 50))
        self.Comp_Core_FsL_Frame.setFrameShape(QFrame.StyledPanel)
        self.Comp_Core_FsL_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.Comp_Core_FsL_Frame)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.CompCore_FsL_Label = QLabel(self.Comp_Core_FsL_Frame)
        self.CompCore_FsL_Label.setObjectName(u"CompCore_FsL_Label")
        self.CompCore_FsL_Label.setMinimumSize(QSize(50, 0))
        self.CompCore_FsL_Label.setMaximumSize(QSize(80, 16777215))
        self.CompCore_FsL_Label.setFont(font)
        self.CompCore_FsL_Label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_22.addWidget(self.CompCore_FsL_Label)

        self.CompCore_FsL_LineEdit = QLineEdit(self.Comp_Core_FsL_Frame)
        self.CompCore_FsL_LineEdit.setObjectName(u"CompCore_FsL_LineEdit")
        self.CompCore_FsL_LineEdit.setMinimumSize(QSize(150, 30))
        self.CompCore_FsL_LineEdit.setMaximumSize(QSize(150, 30))
        self.CompCore_FsL_LineEdit.setFont(font5)
        self.CompCore_FsL_LineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(35, 35, 45);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(35, 35, 45);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_22.addWidget(self.CompCore_FsL_LineEdit)


        self.verticalLayout_18.addWidget(self.Comp_Core_FsL_Frame)

        self.Comp_Core_FsW_Frame = QFrame(self.Comp_Core_Frame)
        self.Comp_Core_FsW_Frame.setObjectName(u"Comp_Core_FsW_Frame")
        self.Comp_Core_FsW_Frame.setMaximumSize(QSize(16777215, 50))
        self.Comp_Core_FsW_Frame.setFrameShape(QFrame.StyledPanel)
        self.Comp_Core_FsW_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.Comp_Core_FsW_Frame)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.CompCore_FsW_Label = QLabel(self.Comp_Core_FsW_Frame)
        self.CompCore_FsW_Label.setObjectName(u"CompCore_FsW_Label")
        self.CompCore_FsW_Label.setMinimumSize(QSize(50, 0))
        self.CompCore_FsW_Label.setMaximumSize(QSize(80, 16777215))
        self.CompCore_FsW_Label.setFont(font)
        self.CompCore_FsW_Label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_23.addWidget(self.CompCore_FsW_Label)

        self.CompCore_FsW_LineEdit = QLineEdit(self.Comp_Core_FsW_Frame)
        self.CompCore_FsW_LineEdit.setObjectName(u"CompCore_FsW_LineEdit")
        self.CompCore_FsW_LineEdit.setMinimumSize(QSize(150, 30))
        self.CompCore_FsW_LineEdit.setMaximumSize(QSize(150, 30))
        self.CompCore_FsW_LineEdit.setFont(font5)
        self.CompCore_FsW_LineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(35, 35, 45);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(35, 35, 45);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_23.addWidget(self.CompCore_FsW_LineEdit)


        self.verticalLayout_18.addWidget(self.Comp_Core_FsW_Frame)

        self.Comp_Core_FOSu_Frame = QFrame(self.Comp_Core_Frame)
        self.Comp_Core_FOSu_Frame.setObjectName(u"Comp_Core_FOSu_Frame")
        self.Comp_Core_FOSu_Frame.setMaximumSize(QSize(16777215, 50))
        self.Comp_Core_FOSu_Frame.setFrameShape(QFrame.StyledPanel)
        self.Comp_Core_FOSu_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.Comp_Core_FOSu_Frame)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.CompCore_FOSu_Label = QLabel(self.Comp_Core_FOSu_Frame)
        self.CompCore_FOSu_Label.setObjectName(u"CompCore_FOSu_Label")
        self.CompCore_FOSu_Label.setMinimumSize(QSize(50, 0))
        self.CompCore_FOSu_Label.setMaximumSize(QSize(80, 16777215))
        self.CompCore_FOSu_Label.setFont(font)
        self.CompCore_FOSu_Label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_24.addWidget(self.CompCore_FOSu_Label)

        self.CompCore_FOSu_LineEdit = QLineEdit(self.Comp_Core_FOSu_Frame)
        self.CompCore_FOSu_LineEdit.setObjectName(u"CompCore_FOSu_LineEdit")
        self.CompCore_FOSu_LineEdit.setMinimumSize(QSize(150, 30))
        self.CompCore_FOSu_LineEdit.setMaximumSize(QSize(150, 30))
        self.CompCore_FOSu_LineEdit.setFont(font5)
        self.CompCore_FOSu_LineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(35, 35, 45);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(35, 35, 45);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_24.addWidget(self.CompCore_FOSu_LineEdit)


        self.verticalLayout_18.addWidget(self.Comp_Core_FOSu_Frame)

        self.Comp_Core_Btns_Frame = QFrame(self.Comp_Core_Frame)
        self.Comp_Core_Btns_Frame.setObjectName(u"Comp_Core_Btns_Frame")
        self.Comp_Core_Btns_Frame.setFrameShape(QFrame.StyledPanel)
        self.Comp_Core_Btns_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.Comp_Core_Btns_Frame)
        self.horizontalLayout_25.setSpacing(5)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(30, -1, 30, -1)
        self.CompCore_Add_Btn = QPushButton(self.Comp_Core_Btns_Frame)
        self.CompCore_Add_Btn.setObjectName(u"CompCore_Add_Btn")
        self.CompCore_Add_Btn.setFocusPolicy(Qt.NoFocus)
        self.CompCore_Add_Btn.setMinimumSize(QSize(100, 30))
        self.CompCore_Add_Btn.setMaximumSize(QSize(100, 30))
        self.CompCore_Add_Btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(217, 4, 41);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.horizontalLayout_25.addWidget(self.CompCore_Add_Btn)

        self.CompCore_Del_Btn = QPushButton(self.Comp_Core_Btns_Frame)
        self.CompCore_Del_Btn.setObjectName(u"CompCore_Del_Btn")
        self.CompCore_Del_Btn.setFocusPolicy(Qt.NoFocus)
        self.CompCore_Del_Btn.setMinimumSize(QSize(100, 30))
        self.CompCore_Del_Btn.setMaximumSize(QSize(100, 30))
        self.CompCore_Del_Btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(217, 4, 41);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.horizontalLayout_25.addWidget(self.CompCore_Del_Btn)


        self.verticalLayout_18.addWidget(self.Comp_Core_Btns_Frame)


        self.horizontalLayout_20.addWidget(self.Comp_Core_Frame)

        self.Comp_Core_Table_Frame = QFrame(self.Material_Core_Frame)
        self.Comp_Core_Table_Frame.setObjectName(u"Comp_Core_Table_Frame")
        self.Comp_Core_Table_Frame.setFrameShape(QFrame.StyledPanel)
        self.Comp_Core_Table_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.Comp_Core_Table_Frame)
        self.horizontalLayout_26.setSpacing(10)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(10, 10, 10, 10)
        self.CompCore_TableWidget = QTableWidget(self.Comp_Core_Table_Frame)
        self.CompCore_TableWidget.setObjectName(u"CompCore_TableWidget")
        self.CompCore_TableWidget.setFrameShape(QFrame.NoFrame)
        self.CompCore_TableWidget.horizontalHeader().setVisible(False)
        self.CompCore_TableWidget.horizontalHeader().setHighlightSections(True)
        self.CompCore_TableWidget.verticalHeader().setVisible(False)

        self.horizontalLayout_26.addWidget(self.CompCore_TableWidget)


        self.horizontalLayout_20.addWidget(self.Comp_Core_Table_Frame)


        self.verticalLayout_16.addWidget(self.Material_Core_Frame)

        self.Pages_Widget.addWidget(self.Composite_Widget)
        self.Metallic_Widget = QWidget()
        self.Metallic_Widget.setObjectName(u"Metallic_Widget")
        self.verticalLayout_20 = QVBoxLayout(self.Metallic_Widget)
        self.verticalLayout_20.setSpacing(15)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(15, 15, 15, 15)
        self.Metallic_Input_Frame = QFrame(self.Metallic_Widget)
        self.Metallic_Input_Frame.setObjectName(u"Metallic_Input_Frame")
        self.Metallic_Input_Frame.setMaximumSize(QSize(16777215, 200))
        self.Metallic_Input_Frame.setStyleSheet(u"background-color: rgb(40, 42, 62);\n"
"border-radius:10px;")
        self.Metallic_Input_Frame.setFrameShape(QFrame.StyledPanel)
        self.Metallic_Input_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.Metallic_Input_Frame)
        self.horizontalLayout_27.setSpacing(10)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(10, 10, 10, 10)
        self.Metallic_Input_Frame2 = QFrame(self.Metallic_Input_Frame)
        self.Metallic_Input_Frame2.setObjectName(u"Metallic_Input_Frame2")
        self.Metallic_Input_Frame2.setFrameShape(QFrame.StyledPanel)
        self.Metallic_Input_Frame2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.Metallic_Input_Frame2)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.Metallic_Input_Frame3 = QFrame(self.Metallic_Input_Frame2)
        self.Metallic_Input_Frame3.setObjectName(u"Metallic_Input_Frame3")
        self.Metallic_Input_Frame3.setMinimumSize(QSize(400, 0))
        self.Metallic_Input_Frame3.setMaximumSize(QSize(400, 16777215))
        self.Metallic_Input_Frame3.setFrameShape(QFrame.StyledPanel)
        self.Metallic_Input_Frame3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.Metallic_Input_Frame3)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, -1, -1, 9)
        self.Comp_Facing_Label_2 = QLabel(self.Metallic_Input_Frame3)
        self.Comp_Facing_Label_2.setObjectName(u"Comp_Facing_Label_2")
        self.Comp_Facing_Label_2.setMinimumSize(QSize(18, 30))
        self.Comp_Facing_Label_2.setMaximumSize(QSize(400, 30))
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(11)
        font8.setBold(True)
        font8.setUnderline(False)
        font8.setWeight(75)
        self.Comp_Facing_Label_2.setFont(font8)
        self.Comp_Facing_Label_2.setStyleSheet(u"color: rgb(214, 214, 214);")
        self.Comp_Facing_Label_2.setFrameShape(QFrame.NoFrame)
        self.Comp_Facing_Label_2.setFrameShadow(QFrame.Plain)
        self.Comp_Facing_Label_2.setLineWidth(1)
        self.Comp_Facing_Label_2.setMidLineWidth(0)
        self.Comp_Facing_Label_2.setAlignment(Qt.AlignLeft)
        self.Comp_Facing_Label_2.setMargin(0)
        self.Comp_Facing_Label_2.setIndent(0)

        self.verticalLayout_21.addWidget(self.Comp_Facing_Label_2)

        self.Metallic_MatID_Frame = QFrame(self.Metallic_Input_Frame3)
        self.Metallic_MatID_Frame.setObjectName(u"Metallic_MatID_Frame")
        self.Metallic_MatID_Frame.setMinimumSize(QSize(0, 40))
        self.Metallic_MatID_Frame.setMaximumSize(QSize(400, 40))
        self.Metallic_MatID_Frame.setStyleSheet(u"color: rgb(214, 214, 214);")
        self.Metallic_MatID_Frame.setFrameShape(QFrame.StyledPanel)
        self.Metallic_MatID_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.Metallic_MatID_Frame)
        self.horizontalLayout_28.setSpacing(10)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(40, 0, 40, 0)
        self.Metallic_MatID_Label = QLabel(self.Metallic_MatID_Frame)
        self.Metallic_MatID_Label.setObjectName(u"Metallic_MatID_Label")
        self.Metallic_MatID_Label.setMinimumSize(QSize(50, 0))
        self.Metallic_MatID_Label.setMaximumSize(QSize(80, 16777215))
        self.Metallic_MatID_Label.setFont(font)
        self.Metallic_MatID_Label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_28.addWidget(self.Metallic_MatID_Label)

        self.Metallic_MatID_LineEdit = QLineEdit(self.Metallic_MatID_Frame)
        self.Metallic_MatID_LineEdit.setObjectName(u"Metallic_MatID_LineEdit")
        self.Metallic_MatID_LineEdit.setMinimumSize(QSize(150, 30))
        self.Metallic_MatID_LineEdit.setMaximumSize(QSize(150, 30))
        self.Metallic_MatID_LineEdit.setFont(font5)
        self.Metallic_MatID_LineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(35, 35, 45);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(35, 35, 45);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_28.addWidget(self.Metallic_MatID_LineEdit)


        self.verticalLayout_21.addWidget(self.Metallic_MatID_Frame)

        self.Metallic_FOSy_Frame = QFrame(self.Metallic_Input_Frame3)
        self.Metallic_FOSy_Frame.setObjectName(u"Metallic_FOSy_Frame")
        self.Metallic_FOSy_Frame.setMinimumSize(QSize(0, 40))
        self.Metallic_FOSy_Frame.setMaximumSize(QSize(400, 40))
        self.Metallic_FOSy_Frame.setFrameShape(QFrame.StyledPanel)
        self.Metallic_FOSy_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.Metallic_FOSy_Frame)
        self.horizontalLayout_29.setSpacing(10)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(40, 0, 40, 0)
        self.Metallic_FOSy_Label = QLabel(self.Metallic_FOSy_Frame)
        self.Metallic_FOSy_Label.setObjectName(u"Metallic_FOSy_Label")
        self.Metallic_FOSy_Label.setMinimumSize(QSize(80, 0))
        self.Metallic_FOSy_Label.setMaximumSize(QSize(50, 16777215))
        self.Metallic_FOSy_Label.setFont(font)
        self.Metallic_FOSy_Label.setStyleSheet(u"color: rgb(214, 214, 214);")
        self.Metallic_FOSy_Label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_29.addWidget(self.Metallic_FOSy_Label)

        self.Metallic_FOSy_LineEdit = QLineEdit(self.Metallic_FOSy_Frame)
        self.Metallic_FOSy_LineEdit.setObjectName(u"Metallic_FOSy_LineEdit")
        self.Metallic_FOSy_LineEdit.setMinimumSize(QSize(150, 30))
        self.Metallic_FOSy_LineEdit.setMaximumSize(QSize(150, 30))
        self.Metallic_FOSy_LineEdit.setFont(font5)
        self.Metallic_FOSy_LineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(35, 35, 45);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(35, 35, 45);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_29.addWidget(self.Metallic_FOSy_LineEdit)


        self.verticalLayout_21.addWidget(self.Metallic_FOSy_Frame)

        self.Metallic_FOSu_Frame = QFrame(self.Metallic_Input_Frame3)
        self.Metallic_FOSu_Frame.setObjectName(u"Metallic_FOSu_Frame")
        self.Metallic_FOSu_Frame.setMinimumSize(QSize(0, 40))
        self.Metallic_FOSu_Frame.setMaximumSize(QSize(400, 40))
        self.Metallic_FOSu_Frame.setFrameShape(QFrame.StyledPanel)
        self.Metallic_FOSu_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.Metallic_FOSu_Frame)
        self.horizontalLayout_30.setSpacing(10)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(40, 0, 40, 0)
        self.Metallic_FOSu_Label = QLabel(self.Metallic_FOSu_Frame)
        self.Metallic_FOSu_Label.setObjectName(u"Metallic_FOSu_Label")
        self.Metallic_FOSu_Label.setMinimumSize(QSize(80, 0))
        self.Metallic_FOSu_Label.setMaximumSize(QSize(50, 16777215))
        self.Metallic_FOSu_Label.setFont(font)
        self.Metallic_FOSu_Label.setStyleSheet(u"color: rgb(214, 214, 214);")
        self.Metallic_FOSu_Label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_30.addWidget(self.Metallic_FOSu_Label)

        self.Metallic_FOSu_LineEdit = QLineEdit(self.Metallic_FOSu_Frame)
        self.Metallic_FOSu_LineEdit.setObjectName(u"Metallic_FOSu_LineEdit")
        self.Metallic_FOSu_LineEdit.setMinimumSize(QSize(150, 30))
        self.Metallic_FOSu_LineEdit.setMaximumSize(QSize(150, 30))
        self.Metallic_FOSu_LineEdit.setFont(font5)
        self.Metallic_FOSu_LineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(35, 35, 45);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(35, 35, 45);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_30.addWidget(self.Metallic_FOSu_LineEdit)


        self.verticalLayout_21.addWidget(self.Metallic_FOSu_Frame)


        self.horizontalLayout_31.addWidget(self.Metallic_Input_Frame3)

        self.Metallic_Btns_Frame = QFrame(self.Metallic_Input_Frame2)
        self.Metallic_Btns_Frame.setObjectName(u"Metallic_Btns_Frame")
        self.Metallic_Btns_Frame.setFrameShape(QFrame.StyledPanel)
        self.Metallic_Btns_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.Metallic_Btns_Frame)
        self.verticalLayout_22.setSpacing(15)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.Metallic_Add_Btn = QPushButton(self.Metallic_Btns_Frame)
        self.Metallic_Add_Btn.setObjectName(u"Metallic_Add_Btn")
        self.Metallic_Add_Btn.setFocusPolicy(Qt.NoFocus)
        self.Metallic_Add_Btn.setMinimumSize(QSize(100, 30))
        self.Metallic_Add_Btn.setFont(font5)
        self.Metallic_Add_Btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(217, 4, 41);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.verticalLayout_22.addWidget(self.Metallic_Add_Btn)

        self.Metallic_Del_Btn = QPushButton(self.Metallic_Btns_Frame)
        self.Metallic_Del_Btn.setObjectName(u"Metallic_Del_Btn")
        self.Metallic_Del_Btn.setFocusPolicy(Qt.NoFocus)
        self.Metallic_Del_Btn.setMinimumSize(QSize(100, 30))
        self.Metallic_Del_Btn.setFont(font5)
        self.Metallic_Del_Btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(217, 4, 41);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.verticalLayout_22.addWidget(self.Metallic_Del_Btn)


        self.horizontalLayout_31.addWidget(self.Metallic_Btns_Frame, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.horizontalLayout_27.addWidget(self.Metallic_Input_Frame2)


        self.verticalLayout_20.addWidget(self.Metallic_Input_Frame)

        self.Metallic_Table_Frame = QFrame(self.Metallic_Widget)
        self.Metallic_Table_Frame.setObjectName(u"Metallic_Table_Frame")
        self.Metallic_Table_Frame.setStyleSheet(u"background-color: rgb(40, 42, 62);\n"
"")
        self.Metallic_Table_Frame.setFrameShape(QFrame.StyledPanel)
        self.Metallic_Table_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.Metallic_Table_Frame)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.Metallic_TableWidget = QTableWidget(self.Metallic_Table_Frame)
        self.Metallic_TableWidget.setObjectName(u"Metallic_TableWidget")
        self.Metallic_TableWidget.setFrameShape(QFrame.NoFrame)
        self.Metallic_TableWidget.horizontalHeader().setVisible(False)
        self.Metallic_TableWidget.horizontalHeader().setHighlightSections(True)
        self.Metallic_TableWidget.verticalHeader().setVisible(False)

        self.verticalLayout_23.addWidget(self.Metallic_TableWidget)


        self.verticalLayout_20.addWidget(self.Metallic_Table_Frame)

        self.Pages_Widget.addWidget(self.Metallic_Widget)
        self.Run_Widget = QWidget()
        self.Run_Widget.setObjectName(u"Run_Widget")
        self.verticalLayout_24 = QVBoxLayout(self.Run_Widget)
        self.verticalLayout_24.setSpacing(20)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(15, 20, 15, 20)
        self.Save_Process_File_Frame = QFrame(self.Run_Widget)
        self.Save_Process_File_Frame.setObjectName(u"Save_Process_File_Frame")
        self.Save_Process_File_Frame.setMaximumSize(QSize(16777215, 150))
        self.Save_Process_File_Frame.setStyleSheet(u"background-color: rgb(40, 42, 62);\n"
"border-radius:10px;")
        self.Save_Process_File_Frame.setFrameShape(QFrame.StyledPanel)
        self.Save_Process_File_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.Save_Process_File_Frame)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.Save_Input_File_Frame = QFrame(self.Save_Process_File_Frame)
        self.Save_Input_File_Frame.setObjectName(u"Save_Input_File_Frame")
        self.Save_Input_File_Frame.setFrameShape(QFrame.StyledPanel)
        self.Save_Input_File_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.Save_Input_File_Frame)
        self.horizontalLayout_32.setSpacing(10)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(20, 10, 20, 10)
        self.Save_Input_File_Label = QLabel(self.Save_Input_File_Frame)
        self.Save_Input_File_Label.setObjectName(u"Save_Input_File_Label")
        self.Save_Input_File_Label.setFont(font)
        self.Save_Input_File_Label.setStyleSheet(u"color: rgb(214, 214, 214);")

        self.horizontalLayout_32.addWidget(self.Save_Input_File_Label)

        self.Save_Input_File_LineEdit = QLineEdit(self.Save_Input_File_Frame)
        self.Save_Input_File_LineEdit.setObjectName(u"Save_Input_File_LineEdit")
        self.Save_Input_File_LineEdit.setMaximumSize(QSize(16777215, 30))
        self.Save_Input_File_LineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(35, 35, 45);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(35, 35, 45);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_32.addWidget(self.Save_Input_File_LineEdit)

        self.Save_Input_File_Btn = QPushButton(self.Save_Input_File_Frame)
        self.Save_Input_File_Btn.setObjectName(u"Save_Input_File_Btn")
        self.Save_Input_File_Btn.setFocusPolicy(Qt.NoFocus)
        self.Save_Input_File_Btn.setMinimumSize(QSize(100, 30))
        self.Save_Input_File_Btn.setMaximumSize(QSize(100, 30))
        self.Save_Input_File_Btn.setFont(font5)
        self.Save_Input_File_Btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(217, 4, 41);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/16x16/icons/16x16/cil-save.png", QSize(), QIcon.Normal, QIcon.On)
        self.Save_Input_File_Btn.setIcon(icon4)

        self.horizontalLayout_32.addWidget(self.Save_Input_File_Btn)


        self.verticalLayout_25.addWidget(self.Save_Input_File_Frame)

        self.CheckBox_Frame = QFrame(self.Save_Process_File_Frame)
        self.CheckBox_Frame.setObjectName(u"CheckBox_Frame")
        self.CheckBox_Frame.setFrameShape(QFrame.StyledPanel)
        self.CheckBox_Frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_25.addWidget(self.CheckBox_Frame)


        self.verticalLayout_24.addWidget(self.Save_Process_File_Frame)

        self.Run_Analysis_Frame = QFrame(self.Run_Widget)
        self.Run_Analysis_Frame.setObjectName(u"Run_Analysis_Frame")
        self.Run_Analysis_Frame.setStyleSheet(u"background-color: rgb(40, 42, 62);\n"
"border-radius:10px;")
        self.Run_Analysis_Frame.setFrameShape(QFrame.StyledPanel)
        self.Run_Analysis_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.Run_Analysis_Frame)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(20, 10, 20, 10)
        self.Run_Process_Analysis_Label = QLabel(self.Run_Analysis_Frame)
        self.Run_Process_Analysis_Label.setObjectName(u"Run_Process_Analysis_Label")
        self.Run_Process_Analysis_Label.setMinimumSize(QSize(0, 30))
        self.Run_Process_Analysis_Label.setMaximumSize(QSize(200, 40))
        self.Run_Process_Analysis_Label.setFont(font)
        self.Run_Process_Analysis_Label.setStyleSheet(u"color: rgb(214, 214, 214);\n"
"")

        self.verticalLayout_26.addWidget(self.Run_Process_Analysis_Label)

        self.Run_Btns_Frame = QFrame(self.Run_Analysis_Frame)
        self.Run_Btns_Frame.setObjectName(u"Run_Btns_Frame")
        self.Run_Btns_Frame.setFrameShape(QFrame.StyledPanel)
        self.Run_Btns_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.Run_Btns_Frame)
        self.horizontalLayout_33.setSpacing(10)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(10, 10, 10, 10)
        self.Run_Analysis_Btn = QPushButton(self.Run_Btns_Frame)
        self.Run_Analysis_Btn.setObjectName(u"Run_Analysis_Btn")
        self.Run_Analysis_Btn.setFocusPolicy(Qt.NoFocus)
        self.Run_Analysis_Btn.setMinimumSize(QSize(100, 30))
        self.Run_Analysis_Btn.setMaximumSize(QSize(150, 40))
        self.Run_Analysis_Btn.setFont(font)
        self.Run_Analysis_Btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(217, 4, 41);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/20x20/icons/20x20/cil-media-play.png", QSize(), QIcon.Normal, QIcon.On)
        self.Run_Analysis_Btn.setIcon(icon5)

        self.horizontalLayout_33.addWidget(self.Run_Analysis_Btn)

        self.Run_Analysis_Progress_Bar = QProgressBar(self.Run_Btns_Frame)
        self.Run_Analysis_Progress_Bar.setObjectName(u"Run_Analysis_Progress_Bar")
        self.Run_Analysis_Progress_Bar.setMinimumSize(QSize(0, 30))
        self.Run_Analysis_Progress_Bar.setStyleSheet(u"QProgressBar {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"    border-radius: 10px;\n"
"	text-align:center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(239, 35, 60);\n"
"    width: 10px;\n"
"	margin-left:6px;\n"
"\n"
"}")
        self.Run_Analysis_Progress_Bar.setValue(0)

        self.horizontalLayout_33.addWidget(self.Run_Analysis_Progress_Bar)


        self.verticalLayout_26.addWidget(self.Run_Btns_Frame)

        self.Output_Window_Label = QLabel(self.Run_Analysis_Frame)
        self.Output_Window_Label.setObjectName(u"Output_Window_Label")
        self.Output_Window_Label.setMinimumSize(QSize(0, 40))
        self.Output_Window_Label.setMaximumSize(QSize(16777215, 40))
        self.Output_Window_Label.setFont(font)
        self.Output_Window_Label.setStyleSheet(u"color: rgb(214, 214, 214);\n"
"")

        self.verticalLayout_26.addWidget(self.Output_Window_Label)

        self.Output_Window_ListView = QListView(self.Run_Analysis_Frame)
        self.Output_Window_ListView.setObjectName(u"Output_Window_ListView")
        font9 = QFont()
        font9.setPointSize(8)
        self.Output_Window_ListView.setFont(font9)
        self.Output_Window_ListView.setStyleSheet(u"    border: 2px solid rgb(64, 71, 88);\n"
"    border-radius: 10px;")
        self.Output_Window_ListView.setFrameShape(QFrame.NoFrame)
        self.Output_Window_ListView.setLineWidth(1)

        self.verticalLayout_26.addWidget(self.Output_Window_ListView)


        self.verticalLayout_24.addWidget(self.Run_Analysis_Frame)

        self.Pages_Widget.addWidget(self.Run_Widget)

        self.verticalLayout_5.addWidget(self.Pages_Widget)

        self.Developed_Frame = QFrame(self.Pages_Frame)
        self.Developed_Frame.setObjectName(u"Developed_Frame")
        self.Developed_Frame.setMinimumSize(QSize(0, 20))
        self.Developed_Frame.setStyleSheet(u"background-color: rgb(40, 42, 62);")
        self.Developed_Frame.setFrameShape(QFrame.NoFrame)
        self.Developed_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.Developed_Frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Developed_Label = QLabel(self.Developed_Frame)
        self.Developed_Label.setObjectName(u"Developed_Label")
        self.Developed_Label.setStyleSheet(u"color: rgb(141, 153, 174);")

        self.horizontalLayout_3.addWidget(self.Developed_Label)

        self.Version_Label = QLabel(self.Developed_Frame)
        self.Version_Label.setObjectName(u"Version_Label")
        self.Version_Label.setLayoutDirection(Qt.LeftToRight)
        self.Version_Label.setStyleSheet(u"color: rgb(141, 153, 174);")
        self.Version_Label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.Version_Label)

        self.SizeGrip_Frame = QFrame(self.Developed_Frame)
        self.SizeGrip_Frame.setObjectName(u"SizeGrip_Frame")
        self.SizeGrip_Frame.setMinimumSize(QSize(20, 0))
        self.SizeGrip_Frame.setMaximumSize(QSize(20, 16777215))
        self.SizeGrip_Frame.setFrameShape(QFrame.StyledPanel)
        self.SizeGrip_Frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.SizeGrip_Frame)


        self.verticalLayout_5.addWidget(self.Developed_Frame)


        self.horizontalLayout_2.addWidget(self.Pages_Frame)


        self.verticalLayout.addWidget(self.Content_Frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        # CURRENT WIDGET PAGE THAT SHOWS WHEN OPENING APP
        self.Pages_Widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_Toggle.setText("")
        self.App_Name_Label.setText(QCoreApplication.translate("MainWindow", u"PROCESS - Nastran Results Post-Processing Tool ", None))
        self.Btn_Minimize.setText("")
        self.Btn_Maximize.setText("")
        self.Btn_Close.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"| HOME  ", None))
        self.Btn_Home_Menu.setText("")
        self.Btn_OpenFiles_Menu.setText("")
        self.Btn_GroupElm_Menu.setText("")
        self.Btn_Composite_Menu.setText("")
        self.Btn_Metallic_Menu.setText("")
        self.Btn_Run_Menu.setText("")
        self.Home_Label.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.AppDescription_Label.setText(QCoreApplication.translate("MainWindow", u"App Description", None))
        self.Copyright_Label.setText(QCoreApplication.translate("MainWindow", u"Copyright \u00a92021. The Regents of the University of California (Regents). All Rights Reserved. Permission to use and distribute this software, without any modifications to the source code, and its documentation for educational, research, and not-for-profit purposes, without fee and without a signed licensing agreement, is hereby granted, provided that the above copyright notice, this paragraph and the following two paragraphs appear in all copies, modifications, and distributions. Contact The Office of Technology Licensing, UC Berkeley, 2150 Shattuck Avenue, Suite 510, Berkeley, CA 94720-1620, (510) 643-7201, otl@berkeley.edu, http://ipira.berkeley.edu/industry-info for commercial licensing opportunities.", None))
        self.Process_File_Label.setText(QCoreApplication.translate("MainWindow", u"OPEN PROCESS Input File", None))
        self.Process_Input_LineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"INPUT File", None))
        self.Browse_Process_File_Btn.setText(QCoreApplication.translate("MainWindow", u" Browse Process File Input", None))
        self.Add_Input_File_Btn.setText(QCoreApplication.translate("MainWindow", u"Add Input", None))
        self.Open_Results_Label.setText(QCoreApplication.translate("MainWindow", u"OPEN Nastran Input and Output Files", None))
        self.BDF_Input_LineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u".BDF File", None))
        self.Browse_BDF_File_Btn.setText(QCoreApplication.translate("MainWindow", u"Browse .BDF File", None))
        self.F06_Input_LineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u".F06 File", None))
        self.PCH_Input_LineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u".PCH File", None))
        self.Browse_PCH_File_Btn.setText(QCoreApplication.translate("MainWindow", u"Browse .PCH File", None))
        self.GroupName_Label.setText(QCoreApplication.translate("MainWindow", u"Group Name Input", None))
        self.GroupElms_Label.setText(QCoreApplication.translate("MainWindow", u"Group Elements Input", None))
        self.AddGroup_Btn.setText(QCoreApplication.translate("MainWindow", u"Add Group", None))
        self.DelGroup_Btn.setText(QCoreApplication.translate("MainWindow", u"Delete Group", None))
        self.Comp_Facing_Label.setText(QCoreApplication.translate("MainWindow", u"Composite Ply/Facing Material Input", None))
        self.CompFacing_MatID_Label.setText(QCoreApplication.translate("MainWindow", u"Material ID", None))
        self.CompFacing_Add_Btn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.CompFacing_FOSu_Label.setText(QCoreApplication.translate("MainWindow", u"FOSu", None))
        self.CompFacing_Del_Btn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.CompCore_Label.setText(QCoreApplication.translate("MainWindow", u"Composite Ply/Core Material Input", None))
        self.CompCore_MatID_Label.setText(QCoreApplication.translate("MainWindow", u"Material ID", None))
        self.CompCore_FsL_Label.setText(QCoreApplication.translate("MainWindow", u"FsL", None))
        self.CompCore_FsW_Label.setText(QCoreApplication.translate("MainWindow", u"FsW", None))
        self.CompCore_FOSu_Label.setText(QCoreApplication.translate("MainWindow", u"FOSu", None))
        self.CompCore_Add_Btn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.CompCore_Del_Btn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.Comp_Facing_Label_2.setText(QCoreApplication.translate("MainWindow", u"Metallic Material Input", None))
        self.Metallic_MatID_Label.setText(QCoreApplication.translate("MainWindow", u"Material ID", None))
        self.Metallic_FOSy_Label.setText(QCoreApplication.translate("MainWindow", u"FOSy", None))
        self.Metallic_FOSu_Label.setText(QCoreApplication.translate("MainWindow", u"FOSu", None))
        self.Metallic_Add_Btn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.Metallic_Del_Btn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.Save_Input_File_Label.setText(QCoreApplication.translate("MainWindow", u"Save Inputs to File", None))
        self.Save_Input_File_LineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type file name", None))
        self.Save_Input_File_Btn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.Run_Process_Analysis_Label.setText(QCoreApplication.translate("MainWindow", u"Run Post-Processing Analysis", None))
        self.Run_Analysis_Btn.setText(QCoreApplication.translate("MainWindow", u"RUN", None))
        self.Output_Window_Label.setText(QCoreApplication.translate("MainWindow", u"Output Window", None))
        self.Developed_Label.setText(QCoreApplication.translate("MainWindow", u"Developed by", None))
        self.Version_Label.setText(QCoreApplication.translate("MainWindow", u"v1.0.0  ", None))
    # retranslateUi

