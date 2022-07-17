from email.policy import default
from tkinter.messagebox import NO
from flask import Flask, render_template, url_for, request, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'

@app.route("/", methods=['POST','GET'])
def calhome():
    em = None
    if request.method == 'POST':
        em = request.form['email']
        return redirect(url_for('register', em=em))
    else:
        return render_template('index.html')

@app.route('/register', defaults={'em': None})
@app.route("/register/<em>")
def register(em):
    em = em
    form = RegistrationForm()
    return render_template('signup.html', form=form, em=em)

@app.route("/login", methods=['GET','POST'])
def login():
    em = None
    form = LoginForm()
    if request.method == 'POST':
        em = request.form['email']
        return redirect(url_for('login2', em=em))
    else:
        return render_template('login.html', form=form)

@app.route("/login2/<em>")
def login2(em):
    em = em
    em2 = f"<strong>{em}</strong>"
    form = LoginForm()
    return render_template('login2.html', form=form, em=em, em2=em2)



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500