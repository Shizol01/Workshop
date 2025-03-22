from flask import Flask, render_template, request
from models import User
from validation import username_validation, password_validation

app = Flask(__name__)

@app.route('/create/user', methods = ['POST', 'GET'] )
def create_user():
    if request.method == 'GET':
        return render_template("create_user.html")

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password_2 = request.form.get('password2')

        username = username_validation(username)
        password = password_validation(password,password_2)


        u = User(username, password)
        u.save()
        return render_template('create_user.html') + "Zarejestrowano"





if __name__ == '__main__':
    app.run(debug = True)
