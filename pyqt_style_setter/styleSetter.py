from PyQt5.QtWidgets import QWidget, QAbstractButton
from pyqt_dark_gray_theme.darkGrayTheme import *


class StyleSetter:
    @staticmethod
    def setWindowStyle(main_window: QWidget):
        main_window.setStyleSheet(getThemeStyle())  # theme
        btns = main_window.findChildren(QAbstractButton)  # buttons
        for btn in btns:
            # check if text exists
            if btn.text().strip() == '':
                btn.setStyleSheet(getIconButtonStyle())  # no text - icon button style
            else:
                btn.setStyleSheet(getIconTextButtonStyle())  # text - icon-text button style
        menu_bar = main_window.menuBar()  # menu bar
        menu_bar_style = getMenuBarStyle(menu_bar)
        menu_bar.setStyleSheet(menu_bar_style)
