# Flask-Based Blog Application

## Overview

This Flask application provides a platform for users to create, manage, and view blog posts. It incorporates various technical features to ensure a robust and user-friendly experience.

## Key Features

### User Authentication
- Secure login and signup using email and password.
- Password hashing with `bcrypt` for enhanced security.

### Post Management
- Create, edit, and delete posts.

### User Profile
- Personal profile page with customizable information.
- Profile picture upload and management.

### Pagination
- Efficient handling of large post lists with pagination.

### Error Handling
- Graceful error handling for invalid requests and exceptions.

## Technical Implementation

### Backend
- **Flask Framework**: Core of the application, providing the web server and routing.
- **SQLAlchemy**: Object-Relational Mapper (ORM) for database interactions.
- **Flask-WTF**: Form validation and security.
- **Flask-Login**: User authentication and session management.
- **bcrypt**: Password hashing and salting.

### Frontend
- **Jinja2**: Templating engine for dynamic content generation.
- **Bootstrap**: CSS framework for responsive design and UI elements.
- **JavaScript**: Client-side scripting for interactive features.

## How to Run

To set up and run this application on your local machine, follow these steps:

1. **Clone the repository** to your local machine
2. **Install dependencies from the requirements.txt file:** <br>pip install -r requirements.txt
3. **Run the application:** <br>python run.py
