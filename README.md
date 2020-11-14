# CALC-Lang - A simple TOY Scripting Language
[![License](https://img.shields.io/badge/license-BSD--3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![Python](https://img.shields.io/badge/Python-v.3.*-green.svg)](https://www.python.org/download/releases/3.0/)

A Simple TOY Scripting language

## Requirements
- Python v.3.^
- PIP

## Installation
```
$ git clone https://github.com/ariabishma/CALC-Lang.git
$ cd CALC-Lang
$ python3 setup.py
$ cd src
$ python3 ./shell.py
```
## Usage 
```
$ python3 ./shell.py [filename]
```
## Examples

```
_var x = 100
_var y = 200
_var z = 300

_print x * y *z
_print x + 100 * 10
_print 10

>> OUTPUT
PRINT OUT :  6000000
PRINT OUT :  1100
PRINT OUT :  10
```


## TODO
- [x] multi expression (example : 1+2*3+4)
- [x] Variable Assignment
- [x] String
