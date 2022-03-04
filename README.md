# pyqt-style-setter
PyQt Style Setter

## Note
Currently the only style which can be set is dark-gray(<a href="https://github.com/yjg30737/pyqt-dark-gray-theme.git">pyqt-dark-gray-theme</a>).

## Requirements
* PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-style-setter.git --upgrade```

## Included Packages
* <a href="https://github.com/yjg30737/pyqt-dark-gray-theme.git">pyqt-dark-gray-theme</a>
* <a href="https://github.com/yjg30737/pyqt-svg-icon-pushbutton.git">pyqt-svg-icon-pushbutton</a>

## Usage
* ```StyleSetter.setWindowStyle(main_window: QWidget, exclude_type_lst: list = [])``` - ```main_window``` is the widget which user want to set the style. ```exclude_type_lst```'s items are excluded from applying style. Item type should be ```type```(ex. ```QAbstractButton```). Currently it only works for ```QAbstractButton```.
