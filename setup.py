from setuptools import setup, find_packages

setup(
    name='pyqt-style-setter',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt style setter',
    url='https://github.com/yjg30737/pyqt-style-setter.git',
    install_requires=[
        'PyQt5>=5.8',
        'pyqt-dark-gray-theme>=0.0.1',
        'pyqt-svg-icon-pushbutton>=0.0.1'
    ]
)