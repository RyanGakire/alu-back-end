# API

Python scripts that get data from a REST API
(https://jsonplaceholder.typicode.com) and display it.

## Files

| File | Description |
| ---- | ----------- |
| `0-gather_data_from_an_API.py` | Takes an employee ID and prints how many of their TODO tasks are done, followed by the titles of the completed tasks. |

## Usage

```
$ ./0-gather_data_from_an_API.py 2
Employee Ervin Howell is done with tasks(8/20):
	 distinctio vitae autem nihil ut molestias quo
	 ...
```

## Requirements

- Ubuntu 14.04 LTS, Python 3.4.3
- `requests` module
- PEP 8 style
