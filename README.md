# Daily Vlog Social Platform API

## Project Overview

The **Daily Vlog Social Platform API** is a RESTful backend application built with **Django** and **Django REST Framework (DRF)**.  
It allows users to register, authenticate, upload daily vlogs, follow other users, and interact with vlogs through likes.

This project was developed as part of the **ALX Capstone Project**, following best practices in API design, authentication, permissions, and deployment readiness.

---

## Features

- Custom user authentication with JWT
- User profile management
- Vlog (post) creation and management
- Follow / unfollow system
- Like / unlike vlogs
- Feed showing vlogs from followed users
- Secure, permission-based access control
- RESTful API design

---

## Technology Stack

- **Backend Framework:** Django
- **API Framework:** Django REST Framework (DRF)
- **Authentication:** JWT (SimpleJWT)
- **Database:** SQLite (development)
- **Version Control:** Git & GitHub
- **Testing:** DRF Browsable API / Postman

---

## Project Structure

daily_vlog_api/
│
├── users/ # Custom user model & authentication
├── vlogs/ # Vlog CRUD operations
├── follows/ # Follow / unfollow functionality
├── likes/ # Like / unlike vlogs
│
├── daily_vlog_api/
│ ├── settings.py
│ ├── urls.py
│
├── manage.py
├── requirements.txt
└── README.md


---

## Custom User Model

- Extends Django’s `AbstractUser`
- Additional fields:
  - `bio`
  - `profile_picture`
- Configured using:
```python
AUTH_USER_MODEL = "users.User"

## Setup Instructions

1. Clone the repository
```bash
git clone <repository-url>
cd daily_vlog_api

Create and activate a virtual environment

python -m venv venv

source venv/bin/activate  

Install dependencies: pip install -r requirements.txt

Run database migrations: python manage.py migrate

Start the development server: python manage.py runserver
---

```markdown
This API uses JWT (JSON Web Tokens) for authentication.

- Register a user: `POST /api/auth/register/`
- Login and obtain token: `POST /api/auth/login/`

Authenticated requests must include the header:
Authorization: Bearer <access_token>




- Authentication (register, login)
- User profiles
- Vlog creation and management
- Follow and unfollow users
- Like and unlike vlogs
- Feed from followed users

All endpoints follow RESTful API conventions.



The core backend functionality has been completed and tested.
The project is deployed using render.com.