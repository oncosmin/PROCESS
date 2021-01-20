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
