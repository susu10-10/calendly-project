from flask import render_template, url_for, request, redirect, flash
from calsite import app
from calsite.forms import RegistrationForm, LoginForm
from werkzeug.security import check_password_hash, generate_password_hash


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
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        #create a new instance of a user
        flash('Your account has been created! You are now able to login')
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

@app.route("/login2/<em>", methods=['GET','POST'])
def login2(em):
    em = em
    em2 = f"<strong>{em}</strong>"
    form = LoginForm()
    if form.validate_on_submit():
        flash('You have been logged in successfully', 'success')
        return redirect(url_for('home'))
    return render_template('login2.html', form=form, em=em, em2=em2)



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500