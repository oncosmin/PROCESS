################################################################################
##
## BY: ONCESCU IONUT-COSMIN
## PROJECT MADE WITH: Qt Designer, PySide2 and SQLite
## DATE: 15.01.2021
## V: 1.0.0
## WITH THANKS TO: WANDERSON M.PIMENTA
##
################################################################################

class Style():

    style_bt_standard = (
    """
    QPushButton {
        background-image: ICON_REPLACE;
        background-position: left center;
        background-repeat: no-repeat;
        border: none;
        border-left: 28px solid rgb(35, 35, 45);
        background-color: rgb(35, 35, 45);
        text-align: center;
        font-family: 'Segoe UI';
        font: bold;
        font-size: 13px;
        color: rgb(214, 214, 214);
    }
    QPushButton[Active=true] {
        background-image: ICON_REPLACE;
        background-position: left center;
        background-repeat: no-repeat;
        border: none;
        border-left: 28px solid rgb(35, 35, 45);
        background-color: rgb(35, 35, 45);
        text-align: center;
        font-family: 'Segoe UI';
        font: bold;
        font-size: 13px;
        color: rgb(214, 214, 214);
    }
    QPushButton:hover {
        background-color: rgb(43, 45, 66);
        border-left: 28px solid rgb(43, 45, 66);
    }
    QPushButton:pressed {
        background-color: rgb(239, 35, 60);;
        border-left: 28px solid rgb(239, 35, 60);
        outline: none;
    }
    """
    )
    
    style_table_standard=(
    """
    QTableWidget {	
        background-color: rgb(40, 42, 62);
		padding: 15px;
        gridline-color: rgb(64, 67, 99);
    }
    QTableWidget::item{
        padding-left: 5px;
		padding-right: 5px;
    }
    QTableWidget::item:selected{
        background-color: rgb(141, 153, 174);
    }
    QScrollBar:vertical {
        background: rgb(64, 67, 99);
        width: 16px;   
        margin: 22px 0px 22px 0px;
    }
    QScrollBar::handle:vertical {
        background: rgb(141, 153, 174);
		border-radius: 6px;
    }
    QScrollBar::add-page:vertical {
        background: rgb(64, 67, 99);
    }
    QScrollBar::sub-page:vertical {
        background: rgb(64, 67, 99);
    }
    QScrollBar::add-line:vertical {
        background: rgb(64, 67, 99);
		border-bottom-right-radius: 8px;
        border-bottom-left-radius: 8px;
		height: 20px;
        subcontrol-position: bottom;
        subcontrol-origin: margin;
    }
    QScrollBar::sub-line:vertical {
        background: rgb(64, 67, 99);
		border-top-right-radius: 8px;
        border-top-left-radius: 8px;
        height: 20px;
        subcontrol-position: top;
        subcontrol-origin: margin;
    }
    
    QScrollBar:horizontal {
        background: rgb(64, 67, 99);
        height: 16px;   
        margin: 0px 21px 0px 21px;
    }
    QScrollBar::handle:horizontal {
        background: rgb(141, 153, 174);
		border-radius: 6px;
    }
    QScrollBar::add-page:horizontal {
        background: rgb(64, 67, 99);
    }
    QScrollBar::sub-page:horizontal {
        background: rgb(64, 67, 99);
    }
    QScrollBar::add-line:horizontal {
        background: rgb(64, 67, 99);
		border-top-right-radius: 8px;
        border-bottom-right-radius: 8px;
		width: 20px;
        subcontrol-position: right;
        subcontrol-origin: margin;
    }
    QScrollBar::sub-line:horizontal {
        background: rgb(64, 67, 99);
		border-top-left-radius: 8px;
        border-bottom-left-radius: 8px;
        width: 20px;
        subcontrol-position: left;
        subcontrol-origin: margin;
    }
    
    QHeaderView::section{
        background-color: rgb(35, 35, 45);
    }
    QTableCornerButton::section{
        background-color: rgb(35, 35, 45);
        border: 1px solid rgb(64, 67, 99);
        border-radius: 5px;
    }
    QTableWidget::horizontalHeader {	
        background-color: rgb(35, 35, 45);
    }
    QHeaderView::section:horizontal
    {
        border: 1px solid rgb(64, 67, 99);
        background-color: rgb(35, 35, 45);
        padding: 3px;
        border-top-left-radius: 4px;
        border-top-right-radius: 4px;
    }
    QHeaderView::section:vertical
    {
        border: 1px solid rgb(64, 67, 99);
        background-color: rgb(35, 35, 45);
        padding: 5px;
        border-top-left-radius: 4px;
        border-bottom-left-radius: 4px;
    }
    """
    )
    style_message_box = (
    """
    QMessageBox {
        border-radius: 50px;
        background-color: rgb(35, 35, 45);
        border: 2px solid rgb(217, 4, 41);
    }
    QMessageBox QLabel {
        color: rgb(225, 225, 225);
        font-size: 15px;
        font: 'Segoe UI';
    }
    QMessageBox QPushButton {
        width: 50;
        height: 20;
        border: 2px solid rgb(52, 59, 72);
        border-radius: 5px;	
        background-color: rgb(52, 59, 72);
        color: rgb(225, 225, 225);
    } 
    QMessageBox QPushButton::hover {
        background-color: rgb(57, 65, 80);
	    border: 2px solid rgb(61, 70, 86);
    } 
    QMessageBox QPushButton::pressed {
        background-color: rgb(217, 4, 41);
        border: 2px solid rgb(43, 50, 61);
    } 
    """
    )