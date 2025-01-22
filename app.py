from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
import os, random, time
from itsdangerous import TimedSerializer
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash
import secrets

app = Flask(__name__)
load_dotenv()
app.secret_key = secrets.token_hex(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = os.getenv('MAIL_PORT')
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS') == 'True'
app.config['MAIL_USERNAME'] = os.getenv('EMAIL_ADDRESS')
app.config['MAIL_PASSWORD'] = os.getenv('EMAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

mail = Mail(app)
db = SQLAlchemy(app)
otp_serializer = TimedSerializer(app.secret_key)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        users = User.query.filter_by(email=email).first()

        if users and check_password_hash(users.password, password):
            session['new_visit']=True
            return redirect(url_for('welcome'))
        else:
            flash('Invalid username or password')
            return render_template('login.html')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        re_pass = request.form['re_password']

        if not email or not password:
            flash('Email and password cannot be empty!')
            return render_template('signup.html')

        if password != re_pass:
            flash('Passwords do not match!')
            return render_template('signup.html')

        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            flash('This email is already registered!')
            return render_template('signup.html')
        password_hash = generate_password_hash(password)
        session['email'] = email
        session['password_hash'] = password_hash

        otp = random.randint(100000, 999999)
        otp_token = otp_serializer.dumps({'otp': otp, 'timestamp': time.time()})
        send_otp_email(email, otp)
        session['otp_token'] = otp_token

        return redirect(url_for('verify'))

    return render_template('signup.html')

def send_otp_email(email, otp):
    try:
        msg = Message(f"Your Verification Code", recipients=[email])
        msg.body = f"Your OTP code is {otp}. This OTP will expire in 10 minutes."
        mail.send(msg)
    except Exception as e:
        flash("An error occurred while sending the OTP email.")
        return redirect(url_for('signup'))

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if request.method == 'POST':
        user_otp = request.form['otp']


        try:
            # Check if OTP session exists
            if 'otp_token' not in session:
                flash('OTP session expired. Please try again.', 'danger')
                return redirect(url_for('login'))

            #
            otp_data = otp_serializer.loads(session['otp_token'])
            original_otp = otp_data['otp']
            timestamp = otp_data['timestamp']


            if time.time() - timestamp > 60:  # 10 minutes
                flash('OTP has expired. Please try again.', 'danger')
                return redirect(url_for('login'))

            if int(user_otp) == original_otp:
                session['new_visit'] = True
                email = session.get('email')
                password_hash = session.get('password_hash')
                if email and password_hash:
                    new_user = User(email=email, password=password_hash)
                    db.session.add(new_user)
                    db.session.commit()
                    session.pop('otp_token', None)
                    flash('Verification successful. You are now registered!', 'success')
                    # Clear the OTP token from session
                    return redirect(url_for('welcome'))
                else:
                    flash('Error: Missing user data. Please try again.', 'danger')
                    return redirect(url_for('signup'))
            else:
                flash('Invalid OTP. please enter valid otp.', 'danger')
                return redirect(url_for('verify'))  # Show error message if OTP is wrong



        except Exception as e:
            flash('OTP verification failed. Please try again later.', 'danger')
            return redirect(url_for('login'))

    return render_template('verify.html')

@app.route('/welcome')
def welcome():
    try:
        if session['new_visit']:
            session.pop('new_visit',None)
            return render_template('welcome.html')


    except:
        return "oops please login or sign up"

if __name__ == '__main__':
    app.run(debug=True)
