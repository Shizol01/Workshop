from models import User
def username_validation(username):
    if len(username) > 255:
        raise Exception('Nazwa użytkownika zbyt długa \n Max 255 znaków')

    user = User.load_user_by_username(username)
    if user:
        raise Exception('Nazwa użytkownika zajęta')

    return username




def password_validation(password,password_2):
    if len(password) > 80:
        raise Exception('Hasło za długie')

    if len(password) < 8:
        raise Exception('Hasło za krótkie')

    if password != password_2:
        raise Exception('Hasła nie pasują')

    return password