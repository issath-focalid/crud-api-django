# Django CRUD Operations with Django REST Framework


## Overview

This simple project demonstrates basic CRUD (Create, Read, Update, Delete) operations using Django and Django REST Framework. It provides a simple API and simple interface desgin using with HTML,CSS and Bootstap5 for managing list of students.

## Features

- **Create:** Add new records to the database.
- **Read:** Retrieve and display existing records.
- **Update:** Modify and save changes to existing records.
- **Delete:** Remove records from the database.

## Technologies Used

- [Django](https://www.djangoproject.com/): A high-level Python web framework.
- [Django REST Framework](https://www.django-rest-framework.org/): A powerful and flexible toolkit for building Web APIs.
- [XAMPP](https://www.apachefriends.org/): It is a free and open-source cross-platform web server.
- [phpMyAdmin](https://www.phpmyadmin.net/): It is a free and open source administration tool for MySQL and MariaDB.
  
## Project Structure

- **`/student`:** This django app containing the main application logic.
- **`/profile_info`:** Configuration settings for the Django project.
- **`/static` and `/templates`:** Static files and HTML templates.
- **`/requirements.txt`:** List of project dependencies.
- **`Dockerfile`:** Docker configuration for containerization.
- **`manage.py`:** Django management script.

## API Endpoints

## Docker Support

## Getting started

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/django-crud-api.git
   ```
3. Connect XAMPP server
4. Create database name with **`profile_info`**
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Apply migrations:
   ```bash
   python manage.py migrate
   ```
7. Run the development server:
   ```bash
   python manage.py runserver
   ```
8. Visit http://localhost:8000/ to access the application.


## Handling this web app

1. Visit http://localhost:8000/stu with your browser and handle the list of students.
2. With the  **`Edit`** button you can update the student details.
3. With the **`Delete`** button you can delete the student details.  
4. Visit http://localhost:8000/student with handle the Django REST framework.  
5. You can check GET, POST, PUT, DELETE.

   
