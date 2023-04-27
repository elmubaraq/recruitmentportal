from flask import Flask,redirect,url_for,render_template,request,flash, get_flashed_messages
from portal import app,db,User
from portal.forms import RegistrationForm, ApplicationForm

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('index.html')
    return render_template('index.html')

@app.route('/register', methods=['GET','POST'])
def register_page():
    form = RegistrationForm()
    if form.validate_on_submit():
        user =User( email_address=form.email_address.data, password_harsh = form.password1.data)
        db.session.add(user)
        db.session.commit()
    if form.errors !={}:
        for err_msg in form.errors.values():
            flash(f'There was an error creating a user: {err_msg}',category='danger')
    return render_template('register.html', form=form)
@app.route('/apply', methods=['GET','POST'])
def apply_page():
    form = ApplicationForm()
    if form.validate_on_submit():
        pass
    return render_template('apply.html', form=form)