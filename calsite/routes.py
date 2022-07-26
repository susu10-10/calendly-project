from flask import render_template, url_for, request, redirect, flash, abort
from calsite import app, db
from calsite.forms import RegistrationForm, LoginForm, EmailForm, EventForm
from flask_login import current_user, login_required, login_user, logout_user
from calsite.models import User, Events
from werkzeug.urls import url_parse



@app.route("/", methods=['POST','GET'])
def calhome():
    em = None
    if request.method == 'POST':
        em = request.form['email']
        return redirect(url_for('register', em=em))
    else:
        return render_template('index.html')

@app.route('/register/', defaults={'em':'None'}, methods=['GET','POST'])
@app.route("/register/<em>", methods=['GET','POST'])
def register(em):
    em = em
    if current_user.is_authenticated:
        return redirect(url_for('homepage'))
    form = RegistrationForm()
    if form.validate_on_submit():
        #create a new instance of a user
        user = User(fullname=form.fullname.data,
                    email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to login', 'success')
        return redirect(url_for('login2', em=form.email.data))

    return render_template('signup.html', form=form, em=em)

@app.route("/login", methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('homepage'))
    form = EmailForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            flash('Invalid Email', 'danger')
            return redirect(url_for('login'))
        else:
            return redirect(url_for('login2', em=form.email.data))
    else:
        return render_template('login.html', form=form)

@app.route("/login2/<em>", methods=['GET','POST'])
def login2(em):
    em = em
    print(em)
    em2 = f"<strong>{em}</strong>"
    if current_user.is_authenticated:
        return redirect(url_for('homepage'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=em).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login2'))
        login_user(user)
        flash('You have been logged in successfully', 'success')
        return redirect(url_for('homepage'))
        # next_page = request.args.get('next')
        # if not next_page or url_parse(next_page).netloc != '':
        #     next_page = url_for('homepage')
        # return redirect(next_page)
    return render_template('login2.html', form=form, em=em, em2=em2)

@app.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out successfully', 'success')
    return redirect(url_for('login'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500


@app.route('/home', methods=['GET','POST'])
@login_required
def homepage():
    form = EventForm()
    if form.validate_on_submit():
        event = Events(
            title=form.title.data, start_date=form.start_date.data,
            end_date=form.end_date.data, description=form.description.data,
            invitees=form.invitees.data, author=current_user)
        db.session.add(event)
        db.session.commit()
        flash('Your Event has been created!', 'success')
        return redirect(url_for('homepage'))

    myevent = Events.query.all()
    return render_template('homepage.html', form=form, myevent=myevent)

@app.route('/event/<int:event_id>/', methods=['GET','POST'])
@login_required
def event(event_id):
    event = Events.query.get_or_404(event_id)
    if event.author != current_user:
        abort(403)
    form = EventForm()
    if form.validate_on_submit():
        event.title = form.title.data
        event.start_date = form.start_date.data
        event.end_date = form.end_date.data
        event.description = form.description.data
        event.invitees = form.invitees.data
        db.session.commit()
        flash('Event Updated Successfully', 'success')
        return redirect(url_for('homepage', event_id=event.id))
    elif request.method == 'GET':
        form.title.data = event.title
        form.description.data = event.description
        form.invitees.data = event.invitees
    return render_template('event.html', event=event, form=form)

@app.route('/event/<int:event_id>/delete', methods=['GET','POST'])
@login_required
def delete_event(event_id):
    event = Events.query.get_or_404(event_id)
    if event.author != current_user:
        abort(403)
    db.session.delete(event)
    db.session.commit()
    flash('Your Event has been removed!', 'success')
    return redirect(url_for('homepage'))

# def get_google_provider_cfg():
#     return requests.get(GOOGLE_DISCOVERY_URL).json

