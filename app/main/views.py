from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import UpdateProfile,OrderForm
from ..models import User,Admin
from flask_login import login_required,current_user
from .. import db,photos
import markdown2  

@main.route('/')
def index():
    '''
    view root page function that returns index page
    '''
    title = 'Home'
    return render_template('index.html', title = title)

@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)





