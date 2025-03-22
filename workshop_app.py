from flask import Flask, render_template, request
from models import User

app = Flask(__name__)

@app.route('/create/user', methods = ['POST', 'GET'] )
def create_user():
    if request.method == 'GET':
        return render_template("create_user.html")

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password_2 = request.form.get('password2')
        if password != password_2:
          return render_template('create_user.html') + "Hasła nie pasują"
        elif username and password:
            u = User(username, password)
            u.save()
            return render_template('create_user.html') + "Zarejestrowano"





if __name__ == '__main__':
    app.run(debug = True)
