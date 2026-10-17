# Django Learning

A hands-on Django practice repository organized into progressive modules, moving from core request/response concepts to templates, models, and shell workflows.

## Learning Modules

| Module | Focus | Path |
| --- | --- | --- |
| 01 | Request/response basics | `01_First_Request_Response/My_first_project/` |
| 02 | Templates and UI rendering | `02_Templates_And_UI/My_sec_project/` |
| 03 | Models, migrations, database flow | `03_Database_And_Models/model_use/` |
| 04 | Django shell notes and commands | `04_Django_Shell/django_shell_cheat_sheet.md` |

## Prerequisites

- Python 3.10+ (recommended)
- `pip`
- Basic command-line familiarity

## Quick Start

### 1) Clone the repository

```bash
git clone https://github.com/aayushmanz/Django-Learning.git
cd Django-Learning
```

### 2) Enter one practice project

```bash
# Option 1
cd 01_First_Request_Response/My_first_project

# Option 2
cd 02_Templates_And_UI/My_sec_project

# Option 3
cd 03_Database_And_Models/model_use
```

### 3) Create and activate a virtual environment

```bash
python -m venv .venv

# macOS/Linux
source .venv/bin/activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

### 4) Install Django

```bash
pip install django
```

### 5) Apply migrations and run server

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

App URL: `http://127.0.0.1:8000/`

## Common Commands

Run these from a folder that contains `manage.py`.

```bash
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py shell
python manage.py createsuperuser
python manage.py test
python manage.py check
```

## Learning Goal

Build a strong Django foundation through practical repetition of:

- URL routing and views
- Templates and UI rendering
- Models and migration workflows
- Database interaction patterns
- Django shell exploration

## License

This project is licensed under the [LICENSE](LICENSE) file.
