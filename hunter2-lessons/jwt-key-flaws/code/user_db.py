from user import User
import bcrypt

def addUser(userData):
    user = User()
    user.name = userData['name']
    user.password = userData['password']
    user.email = userData['email']
    user.username = userData['username']

    return user.save()

def save(user_id, userData):
    user = User.find(user_id)
    user.update(userData)
    return user

def getAll():
    return User.all()

def find(type, match, data = None):
    return User.where(type, '=', match).first()
    
def findById(user_id, data = None):
    return find('id', user_id, data)

def findByUsername(username, data = None):
    return find('username', username, data)

def findByToken(token, data = None):
    return find('token', token, data)
