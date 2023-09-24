import re

from flask import redirect, render_template, session, url_for
from functools import wraps


def apology(message, code=400):
    """Render message as an apology to user."""

    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [
            ("-", "--"),
            (" ", "-"),
            ("_", "__"),
            ("?", "~q"),
            ("%", "~p"),
            ("#", "~h"),
            ("/", "~s"),
            ('"', "''"),
        ]:
            s = s.replace(old, new)
        return s

    return render_template("fun/apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)

    return decorated_function


def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"

def validate_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long"
    
    # Improved regex pattern to check for uppercase, lowercase, digit, and special character
    password_pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&*!])[A-Za-z\d@#$%^&*!]+$"

    if not re.match(password_pattern, password):
        return "Invalid password"

def validate_username(username):
    if len(username) < 4:
        return "Username must be at least 4 characters long"
    
    # Improved regex pattern to allow lowercase letters, digits, underscores, and hyphens
    username_pattern = r"^((?![_-])[a-z0-9]{2,}(?:[a-z0-9.%+]*[a-z0-9])?(?<![_-]))$"

    if not re.match(username_pattern, username):
        return "Invalid username"

def validate_email(email):
    if len(email) <= 3:
        return "Email address must be more than or 3 characters"
    
    email_pattern = r'^[a-zA-Z0-9](?:[a-zA-Z0-9_-]*[a-zA-Z0-9])+@[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?(?:\.[a-zA-Z]{2,})+$'
    
    if not re.match(email_pattern, email):
        return "Invalid email address"
    
