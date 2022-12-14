# The different Routes for out app

from datetime import datetime
from flask_login import current_user, login_required, login_user, logout_user
from .. import app, db, bcrypt
from flask import render_template, flash, redirect, url_for
from .forms import LoginForm, MembershipForm, UserRegistration
from .model import Batch, Membership, User


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = UserRegistration()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password, age=form.age.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created. You can now login', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            if user.memberships:
                if user.memberships.dateValid.date().month != datetime.now().month or user.memberships.dateValid.date().year != datetime.now().year:
                   user.memberships.status = False
                   db.session.commit()
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please enter the right username/password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    # To show how the date update works
    # user = User.query.get(current_user.id)
    # user.memberships.dateValid = datetime.now() - timedelta(days=31)
    # db.session.commit()
    logout_user()
    flash('Logged Out. Successfully', "success")
    return redirect(url_for('home'))

@app.route('/membership', methods=['GET', 'POST'])
@login_required
def membership():
    user = User.query.get(current_user.id)
    
    if User.query.filter_by(id=user.id).first().memberships:
        if User.query.filter_by(id=user.id).first().memberships.status == True:
            flash('You have already enrolled this month. This option will be available again next month', 'success')
            return redirect(url_for('details'))
    form = MembershipForm()
    if form.validate_on_submit():
        data = str(form.batch.data)
        batchId = Batch.query.filter_by(batchTime= data).first().batchId
        if User.query.filter_by(id=user.id).first().memberships:
            Membership.query.filter_by(userId=user.id).delete()
        member = Membership(userId=user.id, batchId=batchId, status=True)
        db.session.add(member)
        db.session.commit()
        flash('You have successfully enrolled for batch: {}'.format(batchId), 'success')
        return redirect(url_for('details'))
    return render_template('membership.html', title='Enroll', form=form, user=user, User=User)                


@app.route('/details', methods=['GET', 'POST'])
@login_required
def details():
    user = User.query.get(current_user.id)
    if User.query.filter_by(id=user.id).first().memberships:
        batch = User.query.filter_by(id=user.id).first().memberships.batchId
        status = ""
        if user.memberships.status:
            status = 'Valid'
        else:
            status = 'Invalid'
        return render_template('details.html', title='Details', user=user, User=user, status=status, batch=batch, Batch=Batch)
    else:
        return render_template('details.html', title='Details', user=user, User=user) 


 # Further Improvements. Not implemented
@app.route('/unenroll', methods=['GET', 'POST'])
@login_required
def unenroll():
    user = User.query.get(current_user.id)
    user.memberships.status = False
    user.memberships.dateValid = datetime.now() # - timedelta(days=1)
    db.session.commit()
    flash("Successfully Unenrolled")
    return redirect(url_for('details'))
