# Django Learning

This repository contains my Django learning journey, practice projects, and experiments while exploring Django fundamentals.

## Repository Structure

- `01_First_Request_Response/` - beginner Django request/response practice
  - `My_first_project/` - first Django project
- `02_Templates_And_UI/` - template rendering and UI-focused practice
  - `My_sec_project/` - second Django project

## Getting Started

1. Clone this repository.
2. Move to a Django project folder (choose one):

```bash
cd 01_First_Request_Response/My_first_project
# or
cd 02_Templates_And_UI/My_sec_project
```

3. (Recommended) Create and activate a virtual environment.
4. Install dependencies:

```bash
pip install django
```

5. Run the development server:

```bash
python manage.py runserver
```

## Helpful Django Commands (Most Used)

Run these commands from a folder that contains `manage.py`.

```bash
# Start a new Django project
django-admin startproject project_name

# Start a new app inside a project
python manage.py startapp app_name

# Run the development server
python manage.py runserver

# Create migration files after model changes
python manage.py makemigrations

# Apply migrations to the database
python manage.py migrate

# Open Django shell
python manage.py shell

# Create admin user
python manage.py createsuperuser

# Run tests
python manage.py test

# Collect static files (production use)
python manage.py collectstatic

# Check project configuration
python manage.py check
```

## Learning Goal

Build a solid Django foundation by practicing project setup, apps, views, URLs, templates, models, and database operations.
