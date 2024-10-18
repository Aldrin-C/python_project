from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.avatar_model import Avatar



@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/create/class', methods=['post'])
def create_class():
    print(request.form)

    if not Avatar.validate(request.form):
        return redirect('/select')

    avatar_dictionary = {
        **request.form,
        'user_id' : session['user_id']
    }

    print(avatar_dictionary)
    Avatar.create_class(avatar_dictionary)
    return redirect ('/dashboard')


# ---- View One on Dashboard ----

@app.route('/view/<int:id>/avatar')
def view_one_avatar(id):
    if 'user_id' not in session:
        return redirect('/')
    
    one_avatar = Avatar.get_by_id(id)
    return render_template('view_art.html',
                            one_avatar = one_avatar)


@app.route('/select')
def select_class():
    return render_template('class_selection.html')

# ---- Dashboard ----
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# ---- Farm ----
@app.route('/farm')
def farm():
    return render_template('farm.html')

# ---- Dojo ----
@app.route('/dojo')
def dojo():
    return render_template('dojo.html')

# ---- Delete ----
@app.route('/avatar/<int:id>/delete', methods=['post'])
def delete(id):
    if 'user_id' not in session:
        return redirect('/')
    
    Avatar.delete_avatar(request.form)
    return redirect('/account')