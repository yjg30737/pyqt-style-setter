from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name='pyqt-style-setter',
    version='0.0.15',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt style setter',
    url='https://github.com/yjg30737/pyqt-style-setter.git',
    long_description_content_type='text/markdown',
    long_description=long_description,
    install_requires=[
        'PyQt5>=5.8',
        'pyqt-dark-gray-theme>=0.0.1',
        'pyqt-light-gray-theme>=0.0.1',
        'pyqt-svg-button>=0.0.1'
    ]
)