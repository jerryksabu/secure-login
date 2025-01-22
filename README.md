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
