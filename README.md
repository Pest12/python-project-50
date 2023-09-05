# Difference generator


### Hexlet tests and linter status:
[![Actions Status](https://github.com/Pest12/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/Pest12/python-project-50/actions)
[![Project2 check](https://github.com/Pest12/python-project-50/actions/workflows/project2_test.yml/badge.svg)](https://github.com/Pest12/python-project-50/actions/worklows/project2_test.yml)
[![Test Coverage](https://api.codeclimate.com/v1/badges/ab1ba76d1100eb29e6a4/test_coverage)](https://codeclimate.com/github/Pest12/python-project-50/test_coverage)
[![Maintainability](https://api.codeclimate.com/v1/badges/ab1ba76d1100eb29e6a4/maintainability)](https://codeclimate.com/github/Pest12/python-project-50/maintainability)


## Description


Difference generator is a program that determines the difference between two data structures.
A program is able to work with the formats: ```json```, ```yaml```


## Installation


Clone the repository and use this commands:

```
make install
make build
make package-install
```


## Optional arguments

1. **-h, --help** 8 `gendiff -h` - launch help
2. **-f, --format** `gendiff -f` - set format of output
**Available formats:**
* `-f stylish` - default format
* `-f plain`
* `-f json`


### Comparison of flat files (JSON)

`gendiff filepath1.json filepath2.json`

[![asciicast](https://asciinema.org/a/604071.svg)](https://asciinema.org/a/604071)


### Comparison of flat files (YAML, YML)

`gendiff filepath1.yaml filepath2.yaml`

[![asciicast](https://asciinema.org/a/604620.svg)](https://asciinema.org/a/604620)

### Comparison of two files with a recursive structure (JSON, YAML, YML)

`gendiff filepath1.json filepath2.json`

[![asciicast](https://asciinema.org/a/605799.svg)](https://asciinema.org/a/605799)


### Work example formatter **plain**

`gendiff filepath1.json filepath2.json -f plain`

[![asciicast](https://asciinema.org/a/606092.svg)](https://asciinema.org/a/606092)


### Work example formatter **json**

`gendiff filepath1.json filepath2.json -f json`

[![asciicast](https://asciinema.org/a/606204.svg)](https://asciinema.org/a/606204)
