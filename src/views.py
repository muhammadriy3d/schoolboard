from flask import Blueprint, render_template, session, url_for, redirect
from src.lib.helpers import apology, login_required

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    """ default dashboard page """
    return apology("dad")
    # return render_template('index.html')

@views.route('/about')
def about():
    """ About page """
    return apology("I AM THE WROST CODER IN THE WORLD!")
    # return render_template('home/about.html')