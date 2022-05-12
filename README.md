# pyqt-style-setter
PyQt style setter

## Note
Currently the only style you can set is dark-gray(<a href="https://github.com/yjg30737/pyqt-dark-gray-theme.git">pyqt-dark-gray-theme</a>).

## Requirements
* PyQt5 >= 5.8

## Setup
`python -m pip install pyqt-style-setter`

## Included Packages
* <a href="https://github.com/yjg30737/pyqt-dark-gray-theme.git">pyqt-dark-gray-theme</a>
* <a href="https://github.com/yjg30737/pyqt-svg-icon-pushbutton.git">pyqt-svg-icon-pushbutton</a> - To exclude svg icon set `QPushButton`, also known as `SvgIconPushButton`. It should use its own style or else svg icon will be disappeared by overwritten style. 

## Usage
* `StyleSetter.setWindowStyle(main_window: QWidget, theme: str = 'dark', exclude_type_lst: list = [])` - `main_window` is the widget which user want to set the style. `exclude_type_lst`'s items are excluded from applying style. Item type should be `type`(ex. `QAbstractButton`). Currently it only works for `QAbstractButton`.

## Example
※ I use the <a href="https://github.com/yjg30737/pyqt-timer.git">pyqt-timer</a>'s settings dialog as an example. 

PyQt default theme

```python
from PyQt5.QtWidgets import QApplication
from pyqt_timer.settingsDialog import SettingsDialog

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = SettingsDialog()
    window.show()
    app.exec_()
```

![image](https://user-images.githubusercontent.com/55078043/167977357-9398f798-0088-47c5-af80-159c6fb1831b.png)

Dark-gray theme

```python
from PyQt5.QtWidgets import QApplication
from pyqt_style_setter import StyleSetter
from pyqt_timer.settingsDialog import SettingsDialog

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = SettingsDialog()
    StyleSetter.setWindowStyle(window) # add this
    window.show()
    app.exec_()
```

![image](https://user-images.githubusercontent.com/55078043/167977474-81411648-de15-45e9-91cd-8f83ea3e863d.png)
