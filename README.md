# Flask Todo App

A simple todo application built with Flask and SQLite.

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/yourusername/flask_todo.git
cd flask_todo
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

The application will automatically create the database and necessary tables on first run. The database file will be stored in the `instance` directory.

## Features
- Create, read, update, and delete tasks
- Tasks are stored with timestamps
- Simple and clean user interface 