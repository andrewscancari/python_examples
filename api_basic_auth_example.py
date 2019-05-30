import requests
import getpass
import json

# Get username from Windows logged user
username = getpass.getuser()

# Input username for github Basic Auth
input_username = input(f'username({username}): ')

# Input password for github Basic Auth
password = getpass.getpass(prompt='Password: ', stream='*')

# If user left username empty, then Windows username will be used instead
if input_username:
    username = input_username

# Create a session
s = requests.Session()

# Sign in the session
s.get('https://api.github.com/user', auth=(username, password))

# Get profile details, returning a json response
r = s.get('https://api.github.com/user')

print(json.dumps(r.json(),indent=4))
