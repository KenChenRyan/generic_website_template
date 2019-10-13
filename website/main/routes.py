from flask import Blueprint, render_template, request, redirect
  
main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    return (render_template('index.html',title='Steam Bot Workshop'))

@main.route("/callback")
def callback():
    return redirect(url_for('home.home'))
