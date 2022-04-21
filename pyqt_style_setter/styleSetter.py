from PyQt5.QtWidgets import QWidget, QAbstractButton, QMainWindow, QDialog
from pyqt_dark_gray_theme.darkGrayTheme import *
from pyqt_svg_icon_pushbutton import SvgIconPushButton


class StyleSetter:
    @staticmethod
    def setWindowStyle(main_window: QWidget, theme: str = 'dark', exclude_type_lst: list = []):
        if theme == 'dark':
            theme_style = getThemeStyle()
            if isinstance(main_window, QMainWindow) or isinstance(main_window, QDialog):
                main_window.setStyleSheet(theme_style)
            else:
                main_window.setObjectName('widget')
                main_window.setStyleSheet(theme_style + getMainWidgetStyle())

            # button
            def setButtonStyle(main_window):
                btns = main_window.findChildren(QAbstractButton)
                for btn in btns:
                    # check if text exists
                    if btn.text().strip() == '':
                        # if button type is SvgIconPushButton, let it maintain its own style
                        if isinstance(btn, SvgIconPushButton):
                            pass
                        else:
                            btn.setStyleSheet(getIconButtonStyle())  # no text - icon button style
                    else:
                        # if button type is SvgIconPushButton, let it maintain its own style
                        if isinstance(btn, SvgIconPushButton):
                            pass
                        else:
                            btn.setStyleSheet(getIconTextButtonStyle())  # text - icon-text button style

            # check exclusion of QAbstractButton
            if QAbstractButton in exclude_type_lst:
                pass
            else:
                setButtonStyle(main_window)

            # todo check exclusion of other types
            if len(exclude_type_lst) > 0:
                for _type in exclude_type_lst:
                    widgets = main_window.findChildren(_type)
                    if isinstance(_type, QAbstractButton):
                        print(_type)

            if isinstance(main_window, QMainWindow):
                menu_bar = main_window.menuBar()  # menu bar
                menu_bar_style = getMenuBarStyle(menu_bar)
                menu_bar.setStyleSheet(menu_bar_style)

