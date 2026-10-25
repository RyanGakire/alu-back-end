# API

Python scripts that get data from a REST API
(https://jsonplaceholder.typicode.com) and display it.

## Files

| File | Description |
| ---- | ----------- |
| `0-gather_data_from_an_API.py` | Takes an employee ID and prints how many of their TODO tasks are done, followed by the titles of the completed tasks. |
| `1-export_to_CSV.py` | Takes an employee ID and saves all of their tasks to `USER_ID.csv` in the format `"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"`. |

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
