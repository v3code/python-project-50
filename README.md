### Hexlet tests and linter status:

[![Actions Status](https://github.com/v3code/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/v3code/python-project-50/actions)
[![Python CI](https://github.com/v3code/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/v3code/python-project-50/actions/workflows/pyci.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/ce93a59349ae42d1b6a3/maintainability)](https://codeclimate.com/github/v3code/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/ce93a59349ae42d1b6a3/test_coverage)](https://codeclimate.com/github/v3code/python-project-50/test_coverage)

# Diff generator

CLI tool to visualise difference in structured files

## Requirements

- Python: >=3.10
- Poetry: 1.5.1
- make: >=4.3

## How to install

Type `make package install` to install package into the system

## How to initialize development environment

Just type `make install` and poetry will do all things required.

## Supported file formats

- json
- yaml/yml

## Supported render formats

### plain

```
Property 'common.setting2' was updated. From 200 to 100
Property 'common.setting3' was removed
Property 'common.setting6.doge.wow' was updated. From '' to 'mew'
Property 'common.setting6.key' was removed
Property 'common.setting6.list' was added with value: [complex value]
Property 'group1' was removed
Property 'group2.abc' was updated. From 12345 to 'abcd'
Property 'group2.deep.name' was added with value: 'john'
Property 'group3' was added with value: [complex value]
```

### stylish

```
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```

### json

```json
[
  {
    "key": "follow",
    "value": false,
    "type": "deleted"
  },
  {
    "key": "host",
    "value": "hexlet.io",
    "type": "unchanged"
  },
  {
    "key": "proxy",
    "value": "123.234.53.22",
    "type": "deleted"
  },
  {
    "key": "timeout",
    "value": {
      "before": 50,
      "after": 20
    },
    "type": "modified"
  },
  {
    "key": "verbose",
    "value": true,
    "type": "added"
  }
]
```

## Examples

### stylish (default)
[![asciicast](https://asciinema.org/a/eGCPXuL8ZVsbbkUNvy06TLdn2.svg)](https://asciinema.org/a/eGCPXuL8ZVsbbkUNvy06TLdn2)


### plain
[![asciicast](https://asciinema.org/a/xbULkTl0rUcvvrx1dqzaJozHP.svg)](https://asciinema.org/a/xbULkTl0rUcvvrx1dqzaJozHP)

### json
[![asciicast](https://asciinema.org/a/xbULkTl0rUcvvrx1dqzaJozHP.svg)](https://asciinema.org/a/xbULkTl0rUcvvrx1dqzaJozHP)
