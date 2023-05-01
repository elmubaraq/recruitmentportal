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
@login_required
def apply_page():
    form = ApplicationForm()
    check_id = Application.query.filter_by(application_check=current_user.id).first()
    
    if  check_id != None:
        print(current_user.id)
        flash(f'Welcome', category = 'info')
        return render_template('application_slip.html')
        
    if request.method == "POST" and form.validate():
    
        
        file1 = request.files['passport_photo']
        file2 = request.files['birth_cert']
        file3 = request.files['nysc_cert']
        file4 = request.files['other_cert']
        file5 = request.files['school_cert_photo']
        file6 = request.files['ssce_photo']
        file7 = request.files['tertiary_cert']
        file8 = request.files['professional_cert'] 
        file1_filename = file1.filename
        file2_filename = file2.filename
        file3_filename = file3.filename
        file4_filename = file4.filename
        file5_filename = file5.filename
        file6_filename = file6.filename
        file7_filename = file7.filename
        file8_filename = file8.filename
        
        file1.save(app.config['UPLOAD_FOLDER'] + '/' + file1_filename)
        file2.save(app.config['UPLOAD_FOLDER'] + '/' + file2_filename)
        file3.save(app.config['UPLOAD_FOLDER'] + '/' + file3_filename)
        file4.save(app.config['UPLOAD_FOLDER'] + '/' + file4_filename)
        file5.save(app.config['UPLOAD_FOLDER'] + '/' + file5_filename)
        file6.save(app.config['UPLOAD_FOLDER'] + '/' + file6_filename)
        file7.save(app.config['UPLOAD_FOLDER'] + '/' + file7_filename)
        file8.save(app.config['UPLOAD_FOLDER'] + '/' + file8_filename)
        application_to_create = Application(first_name =  request.form['first_name'] , middle_name =request.form['middle_name'], last_name=request.form['last_name'],
                                            home_town=request.form['home_town'], permanent_address=request.form['permanent_address'],town_of_residence=request.form['town_of_residence'],
                                            residential_address=request.form['residential_address'],state_of_residence=request.form['state_of_residence'], state_of_origin=request.form['state_of_origin'],
                                            lga=request.form['lga'], phone=request.form['phone'], nin = request.form['nin'], gender= request.form['gender'], primary_school=request.form['primary_school'], secondary_school=request.form['secondary_school'],
                                            tertiary_school=file7_filename, highest_qualification=request.form['highest_qualification'], position_applying_for=request.form['position_applying_for'], passport_photo=file1_filename,
                                            birth_cert=file2_filename,school_cert=file5_filename,ssce_photo=file6_filename,
                                            tertiary_cert=file7_filename,nysc_cert=file3_filename,professional_cert=file8_filename,other_cert=file4_filename, email_address=current_user.email_address,application_check=current_user.id)
        db.session.add(application_to_create)
        db.session.commit()
        flash(f'SUCCESSFUL', category='info')
    if form.errors !={}:
        for err_msg in form.errors.values():
            flash(f'There was an error creating a user: {err_msg}',category='danger')
        
    
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
@app.route('/log_out', methods= ['POST','GET'])
def logout():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("home"))
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error404.html')
    
    
