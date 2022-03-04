from setuptools import setup, find_packages

setup(
    name='pyqt-style-setter',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt Style Setter',
    url='https://github.com/yjg30737/pyqt-style-setter.git',
    install_requires=[
        'PyQt5>=5.8',
        'pyqt-dark-gray-theme @ git+https://git@github.com/yjg30737/pyqt-dark-gray-theme.git@main',
        'pyqt-svg-icon-pushbutton @ git+https://git@github.com/yjg30737/pyqt-svg-icon-pushbutton.git@main'
    ]
)