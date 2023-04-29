from flask import Flask,redirect, url_for, render_template, request, flash, get_flashed_messages
from portal import app, db, User, Application
from portal.forms import RegistrationForm, ApplicationForm, loginForm
from flask_login import login_manager, logout_user, login_user, login_required, current_user

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
        user =User(email_address=form.email_address.data, password = form.password1.data)
        with app.app_context():
            db.create_all()
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
        application_to_create = Application(first_name=form.first_name.data, middle_name=form.middle_name.data, last_name=form.last_name.data,
                                            home_town=form.home_town.data, permanent_address=form.permanent_address.data,town_of_residence=form.town_of_residence,
                                            residential_address=form.residential_address.data,state_of_residence=form.state_of_residence, state_of_origin=form.state_of_origin.data,
                                            lga=form.lga.data, phone=form.phone.data, nin = form.nin.data, gender= form.gender.data, primary_school=form.primary_school.data, secondary_school=form.secondary_school.data,
                                            tertiary_school=form.tertiary_school.data, highest_qualification=form.highest_qualification.data, position_applying_for=form.position_applying_for.data, passport_photo=form.passport_photo.data,
                                            birth_cert=form.birth_cert.data,school_cert=form.school_cert_photo.data,ssce_photo=form.ssce_photo.data,
                                            tertiary_cert=form.tertiary_cert.data,nysc_cert=form.nysc_cert.data,professional_cert=form.professional_cert.data,other_cert=form.other_cert.data)
        db.session.add(application_to_create)
        db.session.commit()
        flash(f'SUCCESSFUL', category='info')
        
    
    return render_template('apply.html', form=form)
@app.route('/login',methods=['GET','POST'])
def login_page():
    form = loginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(email_address=form.email_address.data).first()
        if attempted_user and  attempted_user.check_password_correlation(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'You are successfully logged in as: {attempted_user.email_address}!', category='success')
            return redirect(url_for('apply_page'))
        else:
            flash(f'Username and Password do not match, please try again!', category='danger')
    return render_template('login.html', form=form)
