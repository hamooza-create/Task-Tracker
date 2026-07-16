# Task Tracker

A simple command-line interface (CLI) built in Python to track tasks — what you need to do, what you're working on, and what you've finished. Tasks are stored locally in a `tasks.json` file, so your list persists between runs.

Based on the [Task Tracker project on roadmap.sh](https://roadmap.sh/projects/task-tracker).

## Features

- Add new tasks
- Update a task's description
- Update a task's status (`todo`, `in-progress`, `done`)
- Delete a task
- List all tasks
- List tasks filtered by status
- Automatic timestamps (`CreatedAt`, `UpdatedAt`)
- Data persisted to a local JSON file — no database required

## Requirements

- Python 3.x
- No external libraries — uses only Python's standard library (`json`, `os`, `sys`, `datetime`)

## Getting Started

Clone or download this repository, then run the script directly with Python:

```bash
python task_cli.py <command> [arguments]
```

On first run, a `tasks.json` file is created automatically in the same folder to store your tasks.

## Usage

### Add a task

```bash
python task_cli.py add "Buy groceries"
```

```
Task added successfully (ID: 1)
```

### Update a task's description

```bash
python task_cli.py update-description 1 "Buy groceries and cook dinner"
```

### Update a task's status

```bash
python task_cli.py update-status 1 in-progress
python task_cli.py update-status 1 done
```

Valid statuses: `todo`, `in-progress`, `done`

### Delete a task

```bash
python task_cli.py delete-task 1
```

> Deleting a task automatically renumbers the remaining tasks, so IDs stay sequential with no gaps.

### List all tasks

```bash
python task_cli.py list-tasks
```

### List tasks by status

```bash
python task_cli.py list-tasks-status done
python task_cli.py list-tasks-status todo
python task_cli.py list-tasks-status in-progress
```

### Help

```bash
python task_cli.py help
```

Displays the full list of available commands.

## Command Reference

| Command | Description | Example |
|---|---|---|
| `add "<description>"` | Add a new task | `add "Buy groceries"` |
| `update-status <id> <status>` | Change a task's status | `update-status 1 done` |
| `update-description <id> "<text>"` | Change a task's description | `update-description 1 "New text"` |
| `delete-task <id>` | Delete a task by ID | `delete-task 1` |
| `list-tasks` | Show all tasks | `list-tasks` |
| `list-tasks-status <status>` | Show tasks with a given status | `list-tasks-status todo` |
| `help` | Show the help menu | `help` |

## Task Properties

Each task is stored as a JSON object with the following fields:

| Field | Description |
|---|---|
| `id` | Unique, sequential task identifier |
| `Description` | The task's text |
| `Status` | One of `todo`, `in-progress`, `done` |
| `CreatedAt` | Timestamp of when the task was created |
| `UpdatedAt` | Timestamp of the most recent update |

### Example `tasks.json`

```json
[
    {
        "id": 1,
        "Description": "Buy groceries",
        "Status": "done",
        "CreatedAt": "2026-07-16 15:04:22",
        "UpdatedAt": "2026-07-16 16:10:03"
    },
    {
        "id": 2,
        "Description": "Walk the dog",
        "Status": "todo",
        "CreatedAt": "2026-07-16 15:05:41",
        "UpdatedAt": "2026-07-16 15:05:41"
    }
]
```

## Running It Like a Real Command (Optional)

By default you run the script with `python task_cli.py ...`. If you'd rather type just `task-cli add "..."` from anywhere, see the setup guides below for your OS:

- **Windows** — create a `.bat` wrapper or a PowerShell function, and add its folder to your `PATH`
- **Linux/macOS** — add a shebang line, `chmod +x task_cli.py`, and move it into a folder already in your `PATH` (e.g. `/usr/local/bin`)

## Project Structure

```
project/
├── task_cli.py      # main script
├── tasks.json        # auto-generated task storage (created on first run)
└── README.md
```

## Notes

- All data is stored locally in plain JSON — easy to inspect, back up, or edit by hand if needed.
- No external dependencies or installation steps required beyond Python itself.
