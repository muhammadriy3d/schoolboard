import re
from flask import Blueprint, render_template, request, redirect, session, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from src.lib.helpers import apology, validate_email, validate_password, validate_username
from . import db
from datetime import date

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    """Login page"""
    
    if request.method == "POST":
        # Get user input
        username = request.form.get("username")
        password = request.form.get("password")

        # Check if any required fields are empty
        if not username or not password:
            flash("All fields are required!", category='error')
            return redirect(url_for('auth.login'))

        # Validate username (you should implement this function)
        valid_username = validate_username(username)
        if valid_username:
            flash("Password or username is invalid", category='error')
            return redirect(url_for('auth.login'))
        
        # Validate password (you should implement this function)
        valid_password = validate_password(password)
        if valid_password:
            flash("Password or username is invalid", category='error')
            return redirect(url_for('auth.login'))
        
        # Fetch user from the database based on username (adjust this part for your database setup)
        rows = db.execute("SELECT * FROM users WHERE username = ?", (username,))

        if len(rows) != 1 or not check_password_hash(
            rows[0]["password"], password
        ):
            flash("Invalid username and/or password", category="error")
            return redirect(url_for('auth.login'))
            
        # Store user ID in the session
        session["user_id"] = rows[0]["id"]

        flash("Logged in successfully!", category='success')
        return redirect(url_for('views.home'))
    return render_template("auth/login.html")
    


@auth.route("/logout")
def logout():
    """Logout function"""
    session.clear()
    return redirect(url_for('auth.login'))


@auth.route("/register", methods=["GET", "POST"])
def register():
    """Registration page"""
    if request.method == "POST":
        # Get user input
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Check if any required fields are empty
        if not username or not email or not password or not confirmation:
            flash("All fields are required!", category='error')
            return redirect(url_for('auth.register'))

        # Validate username
        valid_username = validate_username(username)
        if valid_username:
            flash(valid_username, category='error')
            return redirect(url_for('auth.register'))

        # Validate email
        valid_email = validate_email(email)
        if valid_email:
            flash(valid_email, category='error')
            return redirect(url_for('auth.register'))

        # Validate password
        valid_password = validate_password(password)
        if valid_password:
            flash(valid_password, category='error')
            return redirect(url_for('auth.register'))

        # Check if password and confirmation match
        if password != confirmation:
            flash("Passwords do not match!", category='error')
            return redirect(url_for('auth.register'))

        # Hash the password
        hashed_password = generate_password_hash(password)
        
        try:

            existing_username = db.execute("SELECT id FROM users WHERE username = :username", username=username)
            if existing_username:
                return apology(
                    "Username already exists. Please choose a different one.", 400
                )
            
            existing_email = db.execute("SELECT id FROM users WHERE email = :email", email=email)
            if existing_email:
                return apology(
                    "Email Adress's already exists. Please choose a different one.", 400
                )
            
            db.execute("INSERT INTO users(username, email, password, date) VALUES(:username, :email, :password, :date)", username=username, email=email, password=hashed_password, date=date.today())

            flash("Registration successful!", category='success')
            return redirect(url_for('auth.login'))
    
        except Exception as e:
            # Handle exceptions appropriately
            flash(f"An error occurred: {e}", category='error')

    return render_template("auth/register.html")


@auth.route("/reset", methods=["GET", "POST"])
def reset():
    """Password Reset"""
    if request.method == "POST":
        # Get user input
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        # Check if any required fields are empty
        if not username or not email or not password:
            apology("All fields are required!")
            return redirect(url_for('auth.login'))

        # Validate username (you should implement this function)
        valid_username = validate_username(username)
        if valid_username:
            flash("Email or username is invalid", category='error')
            return redirect(url_for('auth.login'))
        
        # Validate email (you should implement this function)
        valid_email = validate_email(email)
        if valid_email:
            flash("Email or username is invalid", category='error')
            return redirect(url_for('auth.login'))
        
        # Validate password (you should implement this function)
        valid_password = validate_password(password)
        if valid_password:
            flash(valid_password, category='error')
            return redirect(url_for('auth.login'))
        

        exist_username = db.execute("SELECT username FROM users WHERE username = :username", username=username)
        exist_email = db.execute("SELECT email FROM users WHERE email = :email", email=email)
        
        if not exist_username and not exist_email:
            apology("There's no user found!")
            return redirect(url_for('auth.login'))
        
        hashed_password = generate_password_hash(password)
        db.execute("UPDATE users SET password=:password WHERE username=:username AND email=:email", password=hashed_password, username=username, email=email)
        flash("Congrats password recovered sucessfully!", category="success")
        return redirect(url_for('auth.login'))
        
    return render_template("auth/reset.html")
