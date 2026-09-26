# Django Learning

This repository tracks my Django learning journey through small, focused modules that build from basics to database and shell practice.

## Repository Structure

- `01_First_Request_Response/`
  - `My_first_project/` - beginner request/response practice
- `02_Templates_And_UI/`
  - `My_sec_project/` - templates and UI-focused practice
- `03_Database_And_Models/`
  - `model_use/` - models and database workflow practice
- `04_Django_Shell/`
  - `django_shell_cheat_sheet.md` - quick notes for Django shell usage

## Getting Started

1. Clone this repository.
2. Move to a Django project folder (choose one):

```bash
cd 01_First_Request_Response/My_first_project
# or
cd 02_Templates_And_UI/My_sec_project
# or
cd 03_Database_And_Models/model_use
```

3. (Recommended) Create and activate a virtual environment.
4. Install dependencies:

```bash
pip install django
```

5. Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

6. Start the development server:

```bash
python manage.py runserver
```

## Helpful Django Commands

Run these commands from a folder that contains `manage.py`.

```bash
# Start a new Django project
django-admin startproject project_name

# Start a new app inside a project
python manage.py startapp app_name

# Run the development server
python manage.py runserver

# Create and apply migrations
python manage.py makemigrations
python manage.py migrate

# Open Django shell
python manage.py shell

# Create admin user
python manage.py createsuperuser

# Run tests
python manage.py test

# Check project configuration
python manage.py check
```

## Learning Goal

Build a strong Django foundation by practicing project setup, apps, views, URLs, templates, models, database operations, and shell usage.
