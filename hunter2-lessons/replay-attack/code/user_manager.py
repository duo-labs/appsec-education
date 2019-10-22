import json, re, bcrypt

def addUser(userData):
    data = parseJson()
    userData['id'] = len(data['users'])+1

    data['users'].append(userData)
    writeJson(data)

def save(user_id, userData):
    data = parseJson()
    for user in data['users']:
        if str(user['id']) == str(user_id):
            # Hash our password if provided
            if "password" in userData:
                if len(userData['password']) > 0:
                    password = userData['password'].encode('utf-8')
                    userData['password'] = str(bcrypt.hashpw(password, bcrypt.gensalt()))
                else:
                    del userData['password']

            user.update(userData)

    writeJson(data)

def getAll():
    data = parseJson()
    return data['users']

def find(type, match, data=None):
    if data == None:
        data = parseJson()
        
    for user in data['users']:
        if type in user and str(user[type]) == str(match):
            return user
    
    return False
    
def findById(user_id, data=None):
    return find('id', user_id, data)

def findByUsername(username, data=None):
    return find('username', username, data)

def findBySecret(secret, data=None):
    return find('secret', secret, data)

def findBySession(session, data=None):
    return find('session', session, data)

## ---------------------

def readJson():
    f = open('data/users.json', 'r')
    contents = f.read()
    contents = re.sub('\s{3,}','', contents.strip())
    return contents

def parseJson():
    f = open('data/users.json', 'r')
    data = json.loads(f.read())

    return data

def writeJson(data):
    f = open('data/users.json', 'w')
    f.write(json.dumps(data))

    return True
