# Google Spreadsheets Python API v4
[![Downloads](https://img.shields.io/pypi/dm/pygsheets.svg)](https://pypi.python.org/pypi/pygsheets)

Manage your spreadsheets with _pygsheets_ in Python.

Features:

* Simple to use
* Open spreadsheets using _title_ or _key_
* Extract range, entire row or column values.
* Google spreadsheet api __v4__ support

##Installation

1. 

## Basic Usage

1. [Obtain OAuth2 credentials from Google Developers Console](https://console.developers.google.com/start/api?id=sheets.googleapis.com) for google spreadsheet and drive api and save the file as client_secret.json in same directory as project

2. Start using pygsheets:

```python
import pygsheets

gc = pygsheets.authorize()

# Open a worksheet from spreadsheet with one shot
wks = gc.open('my new ssheet').sheet1

wks.update_acell('B2', "it's down there somewhere, let me take another look.")

# Fetch a cell range
cell_list = wks.range('A1:B7')
```

## More Examples

### Opening a Spreadsheet

```python
# You can open a spreadsheet by its title as it appears in Google Docs 
sh = gc.open("My poor gym results") # <-- Look ma, no keys!

# If you want to be specific, use a key (which can be extracted from
# the spreadsheet's url)
sht1 = gc.open_by_key('0BmgG6nO_6dprdS1MN3d3MkdPa142WFRrdnRRUWl1UFE')

# Or, if you feel really lazy to extract that key, paste the entire url
sht2 = gc.open_by_url('https://docs.google.com/spreadsheet/ccc?key=0Bm...FE&hl')
```

### Selecting a Worksheet

```python
# Select worksheet by index. Worksheet indexes start from zero
worksheet = sh.get_worksheet('index',0)

# By title
worksheet = sh.worksheet('title',"January")

# Most common case: Sheet1
worksheet = sh.sheet1

# Get a list of all worksheets
worksheet_list = sh.worksheets()
```

## Requirements

Python 2.6+

## Installation

### From GitHub

```sh
git clone https://github.com/nithinmurali/pygsheets.git
cd pygsheets
python setup.py install
```

### From PyPI (TBD)


## [Contributors](https://github.com/nithinmurali/pygsheets/graphs/contributors)

## How to Contribute

### Report Issues

Please report bugs and suggest features via the [GitHub Issues](https://github.com/nithinmurali/pygsheets/issues).

Before opening an issue, search the tracker for possible duplicates. If you find a duplicate, please add a comment saying that you encountered the problem as well.

### Contribute code

* Check the [GitHub Issues](https://github.com/nithinmurali/pygsheets/issues) for open issues that need attention.
* Follow the [Contributing to Open Source](https://guides.github.com/activities/contributing-to-open-source/) Guide.


## NB
Most of the code of this library is copied form the gspread library