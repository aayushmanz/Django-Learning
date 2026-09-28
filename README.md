# Django Learning

A structured, hands-on Django learning repository designed to build practical skills step by step, from basic request/response handling to templates, models, database workflows, and shell usage.

## Overview

This repository is organized as progressive modules. Each module focuses on a specific Django concept so you can learn in a clear sequence and reinforce fundamentals through practice.

## Learning Path

1. **Request & Response Basics**
2. **Templates and UI Rendering**
3. **Database and Model Workflows**
4. **Django Shell Practice**

## Repository Structure

- `01_First_Request_Response/`
  - `My_first_project/` — beginner practice with Django request/response flow
- `02_Templates_And_UI/`
  - `My_sec_project/` — working with templates and UI presentation
- `03_Database_And_Models/`
  - `model_use/` — model definitions, migrations, and database interactions
- `04_Django_Shell/`
  - `django_shell_cheat_sheet.md` — quick-reference notes for Django shell usage

## Prerequisites

Before running any project in this repository, make sure you have:

- Python 3.10+ (recommended)
- `pip` installed
- Basic command-line familiarity

## Getting Started

### 1) Clone the repository

```bash
git clone https://github.com/aayushmanz/Django-Learning.git
cd Django-Learning
```

### 2) Choose a module project

```bash
cd 01_First_Request_Response/My_first_project
# or
cd 02_Templates_And_UI/My_sec_project
# or
cd 03_Database_And_Models/model_use
```

### 3) Create and activate a virtual environment (recommended)

```bash
python -m venv .venv

# macOS/Linux
source .venv/bin/activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

### 4) Install dependencies

```bash
pip install django
```

### 5) Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6) Start the development server

```bash
python manage.py runserver
```

By default, the app runs at `http://127.0.0.1:8000/`.

## Common Django Commands

Run these commands from a project directory that contains `manage.py`.

```bash
# Start a new Django project
django-admin startproject project_name

# Start a new app inside an existing project
python manage.py startapp app_name

# Run the development server
python manage.py runserver

# Create and apply migrations
python manage.py makemigrations
python manage.py migrate

# Open the Django shell
python manage.py shell

# Create an admin user
python manage.py createsuperuser

# Run tests
python manage.py test

# Validate project configuration
python manage.py check
```

## Learning Goal

Develop a strong Django foundation by practicing:

- Project setup and structure
- Apps, views, and URL routing
- Template rendering and UI basics
- Models, migrations, and database operations
- Interactive exploration with Django shell

## License

This project is licensed under the terms of the [LICENSE](LICENSE) file.
