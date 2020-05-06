# Scammers often try to obtain your details so they can later use it to extract anything they can from you..
# This is an attempt to try and login into the system several times in order to confuse and make their lives difficult

# If you don't have any of the libraries below please install accordingly using pipenv install ..

import json
import os
import random
import string
import requests

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

# URL to be used
url = 'add the url that is trying to scam you'

# download the json file I've produced or create you own
first_names = json.loads(open('ListOfnames.json').read())

# Loop through the Json file names list
for name in first_names:
	name_add_on = ''.join(random.choice(string.digits)) # Add random chars to the name in the list

	username = name.lower() + name_add_on + '@hotmail/gmail/live/yahoo/aol' # Join the name, the name chars, and email of choice extension
	password = ''.join(random.choice(chars) for i in range(8)) # Same for password

	# Use the requests library to add the username & password created. Also prevent the URL from redirecting by setting it to False
	requests.post(url, allow_redirects=False, data={'email': username, 'password': password})

	# Print the name and password being sent to the URL
	print('Username:' + username + '\t' + 'Password:' + password + '\n')