from flask import Flask, render_template, request
from models import User, Message
from validation import username_validation, password_validation, errors, user_password_validation
from validation import *

app = Flask(__name__)

@app.route('/create/user', methods = ['POST', 'GET'] )
def create_user():
    errors.clear()

    if request.method == 'GET':
        return render_template("create_user.html")

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password_2 = request.form.get('password2')

        username = username_validation(username)
        if not username:
            return render_template('create_user.html', errors=errors)

        password = password_validation(password,password_2)
        if not password:
            return render_template('create_user.html', errors=errors)

        u = User(username, password)
        u.save()
        return render_template('create_user.html', success_message="User was created.")


@app.route('/users', methods = ['GET'])
def users():
    if request.method == 'GET':
        users = User.load_all_users()
        return render_template('list_users.html', users=users)

@app.route('/send/message', methods = ['GET', 'POST'])
def send_message():
    errors.clear()

    if request.method == 'GET':
        return render_template('send_message.html')

    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        to_username = request.form.get('to_username')
        msg = request.form.get('msg')

    username = user_validation(username)
    if not username:
        return render_template('send_message.html', errors=errors)

    password = user_password_validation(username, password)
    if not password:
        return render_template('send_message.html', errors=errors)

    to_username = to_user_validation(to_username)
    if not to_username:
        return render_template('send_message.html', errors=errors)

    user_id = User.load_user_by_username(username)[2]
    to_id = User.load_user_by_username(to_username)[2]

    m = Message(user_id, to_id, msg)
    m.save_to_db()
    print(msg)
    return render_template('send_message.html', success_message="Wiadomość wysłana.")




if __name__ == '__main__':
    app.run(debug = True)
