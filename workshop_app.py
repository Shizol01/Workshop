from flask import Flask, render_template, request
from models import User
from validation import username_validation, password_validation, errors

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
        password = password_validation(password,password_2)

        if not username:
            return render_template('create_user.html', errors=errors)

        if not password:
            return render_template('create_user.html', errors=errors)

        u = User(username, password)
        u.save()
        return render_template('create_user.html', success_message="User was created.")






if __name__ == '__main__':
    app.run(debug = True)
