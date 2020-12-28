import json

USERS = PASS = ''


def init():
    global USERS, PASS

    with open('settings.json', 'r') as file:
        data = file.read()

    obj = json.loads(data)

    USERS = obj['loginDetails']['user']
    PASS = obj['loginDetails']['pass']
