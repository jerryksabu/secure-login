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

To create a virtual environment for your project, run:

bash
Copy
python -m venv ven 

3.**Activate the virtual environment**:

On Windows:
bash
Copy
venv\Scripts\activate
On macOS/Linux:
bash
Copy
source venv/bin/activate

4.**Install dependencies**:

Install the required libraries listed in requirements.txt:

bash
Copy
pip install -r requirements.txt

5.**Create the .env file (for environment variables)**:



FLASK_APP=run.py 

FLASK_ENV=development

FLASK_SECRET_KEY=your_flask_secret_key_here

DATABASE_URL=sqlite:///users.db

MAIL_USERNAME=your_email@example.com

MAIL_PASSWORD=your_email_password

MAIL_SERVER=smtp.example.com
MAIL_PORT=587

MAIL_USE_TLS=True

Replace your_flask_secret_key_here with a secure key for your app.

Replace your_email@example.com and your_email_password with your email details (if you're using email features).

6.**Run the Flask application**:

python run.py

Open the app in your browser:

Go to http://127.0.0.1:5000 in your browser. You should see the secure login and signup page.

7.**Note**:

Keep the directory structure in this format:

secure-login/

├── secure_login/

│   ├── __init__.py  

│   ├── routes.py  
│   ├── models.py  
│   ├── templates/
│   │   ├── login.html  
│   │   └── signup.html 
│   └── static/
│       └── style.css 
├── requirements.txt   
├── run.py    
└── README.md   

