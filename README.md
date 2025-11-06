# Django Signals Assignment

## Overview
This project demonstrates how Django signals work by automatically creating a `Profile` whenever a new `User` is created.

## Features
- Uses `post_save` signal on Django’s User model
- Automatically generates Profile object
- Demonstrates synchronous signal behavior

## How to Run
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
