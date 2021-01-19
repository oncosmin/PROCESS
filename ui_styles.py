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
        padding: 15px;;
    }
    QTableWidget::item{
        padding-left: 5px;
        padding-right: 5px;
        border: 0.5px solid rgb(35, 35, 45);
    }
    QTableWidget::item:selected{
        background-color: rgb(141, 153, 174);
    }
    QScrollBar:vertical {
        background: rgb(43, 45, 66);
        width: 16px;   
        margin: 22px 0px 22px 0px;
	    border-radius: 8px;
    }
    QScrollBar::handle:vertical {
        background: rgb(141, 153, 174);
        min-width: 16px;
        border-radius: 8px;
    }
    QScrollBar::add-page:vertical {
        background: rgb(43, 45, 66);
    }
    QScrollBar::sub-page:vertical {
        background: rgb(43, 45, 66);
    }
    QScrollBar::add-line:vertical {
        background: rgb(43, 45, 66);
        border-bottom-right-radius: 8px;
        border-bottom-left-radius: 8px;
        height: 20px;
        subcontrol-position: bottom;
        subcontrol-origin: margin;
    }
    QScrollBar::sub-line:vertical {
        background: rgb(43, 45, 66);
        border-top-right-radius: 8px;
        border-top-left-radius: 8px;
        height: 20px;
        subcontrol-position: top;
        subcontrol-origin: margin;
    }
    QHeaderView::section{
        background-color: rgb(35, 35, 45);
        width: 25px;
        border-style: none;
    }
    QTableCornerButton::section{
        background-color: rgb(35, 35, 45);
    }
    QTableWidget::horizontalHeader {	
        background-color: rgb(35, 35, 45);
    }
    QHeaderView::section:horizontal
    {
        border: 1px solid rgb(35, 35, 45);
        background-color: rgb(35, 35, 45);
        padding: 3px;
        border-top-left-radius: 10px;
        border-top-right-radius: 10px;
    }
    QHeaderView::section:vertical
    {
        border: 1px solid rgb(35, 35, 45);
    }
    """
    )
