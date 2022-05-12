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
