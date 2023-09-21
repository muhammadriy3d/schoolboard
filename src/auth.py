from flask import Blueprint, render_template, request, redirect, url_for
from src.lib.helpers import apology

auth = Blueprint("auth", __name__)

@auth.route('/login')
def login():
    """ Login page """
    return render_template('auth/login.html')


@auth.route('/logout')
def logout():
    """ Logout function """
    return "alert('Logout function')"


@auth.route('/register', methods=["GET", "POST"])
def register():
    """ Registeration page """
    if request.method == "POST":
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirmation = request.form.get('confirmation')

        # Validate each credit
        """ TODO: Username must be from 8 to 24 character """
        """  """

        # Check password confirm matches

        # Store the data in the DB

        # return user to home
        return redirect(url_for('views.home'))
    else:
        return render_template('auth/register.html')


@auth.route('/reset')
def reset():
    """ Password Reset """
    return render_template('auth/reset.html')

