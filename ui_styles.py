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
