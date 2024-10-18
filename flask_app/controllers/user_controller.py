from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.user_model import User
from flask_app.models.avatar_model import Avatar
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)



# ---- Sign up - Login ----
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process/registration', methods=['post'])
def process():

    if not User.validate_reg(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    
    user_data = {
        **request.form,
        'password' : pw_hash
    }

    user_id = User.create_user(user_data) #creates user data with hashed password

    session['user_id'] = user_id
    return redirect('/select')

@app.route('/process/login', methods=['post'])
def login():
    user_in_db = User.get_email(request.form['email'])
    if not user_in_db:
        flash("Invalid Email", 'login')
        return redirect ('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Password", 'login')
        return redirect('/')
    
    session['user_id'] = user_in_db.id
    return redirect('/account')

# ---- Account ----
@app.route('/account')
def account():
    if 'user_id' not in session:
        return redirect('/')

    logged_user = User.get_id(session['user_id'])

    all_avatars = Avatar.get_all_avatars()

    return render_template('account.html',
                            logged_user = logged_user,
                            all_avatars = all_avatars)


@app.route('/account/update', methods=['post'])
def account_update():
    if 'user_id' not in session:
        return redirect('/')
    User.update_user(request.form)
    return redirect ('/account')

#  ---- Logout ----
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')