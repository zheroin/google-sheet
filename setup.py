#!/usr/bin/env python

import os.path
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import sys

if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist")
    os.system("python2 setup.py bdist_wheel")
    os.system("python3 setup.py bdist_wheel")
    os.system('twine upload dist/* -r pypi')
    sys.exit()


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


description = 'Google Spreadsheets Python API v4'
long_description = read('README.md')

version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                    read('pygsheets/__init__.py'), re.MULTILINE).group(1)

install_require = [
    'google-api-python-client>=2.50.0',
    'google-auth-oauthlib>=0.7.1',
    'enum34 >= 1.1.6;python_version<"3.4"',
]

setup(
    name='pygsheets',
    packages=['pygsheets'],
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    version=version,
    author='Nithin Murali',
    author_email='imnmfotmal@gmail.com',
    url='https://github.com/nithinmurali/pygsheets',
    keywords=['spreadsheets', 'google-spreadsheets', 'pygsheets'],
    install_requires=install_require,
    extras_require={'pandas': ['pandas>=0.14.0']},
    download_url='https://github.com/nithinmurali/pygsheets/tarball/'+version,
    include_package_data=True,
    package_data={'data': ['data/drive_discovery.json', 'data/sheets_discovery.json']},
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research",
        "Topic :: Office/Business :: Financial :: Spreadsheet",
        "Topic :: Software Development :: Libraries :: Python Modules"
        ],
    license='MIT'
    )
