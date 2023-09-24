from flask import Blueprint, flash, redirect, render_template, session, request, url_for, jsonify
from src.lib.helpers import apology, login_required
from . import db
from datetime import date

views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
@login_required
def home():
    """default dashboard page"""
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        city = request.form.get("city")

        if not username or not email or not city:
            return apology("All fields are required!")
            # return redirect(url_for('views.home'))

        exist_username = db.execute(
            "SELECT id FROM users WHERE username = :username", username=username)
        exist_email = db.execute(
            "SELECT id FROM users WHERE email = :email", email=email)

        if exist_username and exist_email:
            return apology("Student already registered!")
            # return redirect(url_for('views.home'))

        today = date.today()
        db.execute("INSERT INTO users(username, email, city, date) VALUES(:username, :email, :city, :date)",
                   username=username, email=email, city=city, date=today)
        flash("Student has been added successfully!", category="success")
        return redirect(url_for("views.users"))

    uid = session.get("user_id")

    username = db.execute("SELECT username FROM users WHERE id=:uid", uid=uid)
    for row in username:
        username = row['username']

    return render_template('pages/index.html', username=username)


@views.route("/current-user")
@login_required
def current_user():
    """ Current user fetching data """

    uid = session.get("user_id")
    username = db.execute("SELECT username FROM users WHERE id=:uid", uid=uid)
    for row in username:
        username = row["username"]

    uid = session.get("user_id")
    email = db.execute("SELECT email FROM users WHERE id=:uid", uid=uid)
    for row in email:
        email = row["email"]

    return jsonify({
        "username": username,
        "email": email
    })


@views.route("/about")
def about():
    """About page"""
    return apology("I AM THE WROST CODER IN THE PLANET!", 200)
    # return render_template('pages/about.html')


@views.route("/users")
@login_required
def users():
    """Users page"""

    if (session.get('user_id')):
        students = db.execute("SELECT * FROM users")

        return render_template('pages/users.html', students=students)

    return render_template('pages/users.html')




@views.route("/users/<int:studentId>", methods=["DELETE"])
@login_required
def delete_student(studentId):
    """delete Users"""
    try:
        if not studentId:
            return apology("Invalid ID", 400)  # Return a 400 Bad Request for invalid ID

        # Ensure the user is logged in
        if session.get('user_id'):
            # Validate and sanitize user input (e.g., checking if studentId is an integer)
            if not isinstance(studentId, int):
                return apology("Invalid input", 400)  # Return a 400 Bad Request for invalid input


            student = db.execute(
                "SELECT * FROM users WHERE id = :id", id=studentId
            )


            if student:
                # Attempt to delete the student
                try:
                    db.execute("DELETE FROM users WHERE id = :id", id=studentId)
                    flash("Student deleted successfully!", category="success")
                except Exception as err:
                    return apology(f"Delete failed: {err}", 500)
            else:
                return apology("Student not found", 404)  # Return a 404 Not Found if the student doesn't exist
        else:
            return apology("Unauthorized", 401)  # Return a 401 Unauthorized if the user is not logged in
    except Exception as e:
        return apology(f"An error occurred: {str(e)}", 500)  # Return a 500 Internal Server Error for other errors

    return jsonify({"message": "Student deleted successfully"})