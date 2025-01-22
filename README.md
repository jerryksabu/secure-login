# Secure Login and Signup Flask App

A simple Flask web application implementing secure login and signup functionalities. This project demonstrates user authentication with secure password handling and basic form validation. Users can create accounts and log in with securely hashed passwords.

## Features

- **User Signup**: Allows users to create accounts with a unique username and secure password.
- **User Login**: Authenticated login using hashed passwords.
- **Password Security**: Uses `werkzeug.security` for password hashing.
- **Session Management**: Keeps track of the logged-in user with Flask sessions.

## Tech Stack

- **Flask**: Web framework for building the application.
- **Jinja2**: Templating engine for HTML rendering.
- **Werkzeug**: For hashing and verifying passwords.
- **SQLite**: Database for storing user credentials (you can replace with other databases like MySQL/PostgreSQL).
- **HTML/CSS**: For creating the user interface.

## Installation

To run this project locally, follow these steps:

### Prerequisites

Ensure you have the following installed:
- Python 3.x
- pip (Python package installer)

### Steps

1. **Clone the repository**:

   Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/secure-login.git
   cd secure-login
2.**Create a virtual environment**:
    python -m venv venv
3.**Activate the virtual environment**:
  venv\Scripts\activate
4.**Install dependencies**:
  Install the required libraries listed in requirements.txt:
  pip install -r requirements.txt
5.**Run the Flask app**:
   python run.py
6.**Open the app in your browser**:
   Go to http://127.0.0.1:5000 in your browser. You should see the secure login and signup page.

**keep directory structure this format**
secure-login/
├── secure_login/
│   ├── __init__.py         # Initialize the Flask app
│   ├── routes.py           # Contains the routes for login and signup
│   ├── models.py           # Contains the user model and database operations
│   ├── templates/
│   │   ├── login.html      # HTML template for login page
│   │   └── signup.html     # HTML template for signup page
│   └── static/
│       └── style.css       # Optional CSS file for styling
├── requirements.txt        # Project dependencies
├── run.py                  # Main file to run the Flask application
└── README.md               # Project documentation
**For production or more complex environments, you can create an .env file to store sensitive data such as your Flask secret key and database configurations. Here's an example**:
FLASK_SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///users.db
**To Do / Features to Add**
1.Email verification: Add email verification for user signup.
2.Forgot Password: Implement a feature to reset forgotten passwords.
3.Input validation: Add more input validation for the form fields.
4.Better UI: Improve the frontend with additional styling and UX enhancements.
