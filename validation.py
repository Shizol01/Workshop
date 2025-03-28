from models import User
errors = []
def username_validation(username):

    if not username:
        errors.append('Nazwa użytkownika pusta')
    if len(username) > 255:
        errors.append('Nazwa użytkownika zbyt długa \n Max 255 znaków')
    if len(username) < 3:
        errors.append('Nazwa użytkownika za ktrótka')

    user = User.load_user_by_username(username)
    if user:
        errors.append("Nazwa użytkownika zajęta")

    return username if not errors else None




def password_validation(password,password_2):

    if len(password) > 80:
        errors.append('Hasło za długie')

    if len(password) < 8:
        errors.append('Hasło za krótkie')

    if password != password_2:
        errors.append('Hasła nie pasują')


    return password if not errors else None

def user_validation(username):
    if not username:
        errors.append('Nazwa użytkownika pusta')

    user = User.load_user_by_username(username)
    if not user:
        errors.append("Użytkownik nie istnieje")

    return username if not errors else None

def user_password_validation(username, password):
    pw = User.load_user_by_username(username)
    if pw[1] != password:
        errors.append('Nieprawidłowe hasło')

    return password if not errors else None

def to_user_validation(username):
    if not username:
        errors.append('Nazwa użytkownika pusta')

    user = User.load_user_by_username(username)
    if not user:
        errors.append("Odbiorca nie istnieje")

    return username if not errors else None