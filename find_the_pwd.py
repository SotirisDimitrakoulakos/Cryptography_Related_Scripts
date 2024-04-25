import requests, random
from hashlib import sha256
from base64 import b64decode as bd

pwds = requests.get(bd(b'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL2RhbmllbG1pZXNzbGVyL1NlY0xpc3RzL21hc3Rlci9QYXNzd29yZHMvNTAwLXdvcnN0LXBhc3N3b3Jkcy50eHQ=')).text.split('\n')

# use two words from the above wordlist as username and password
username, password = [random.choice(pwds) for _ in '12']

print('Welcome to my secure authentication system!')

# SOLUTION #

for i in pwds:
    for j in pwds:
        if sha256((f'{i}_{j}').encode()).hexdigest() == 'ae69b741dbd42018bbcc2a3b7f22b3152571ddbe8b6b562665d025a455b0a36f':
            _u = i
            _p = j
            break

# SOLUTION #

assert sha256((f'{_u}_{_p}').encode()).hexdigest() == 'ae69b741dbd42018bbcc2a3b7f22b3152571ddbe8b6b562665d025a455b0a36f', exit("Oops ... Try again!")

print(f'Welcome {_u}! You are logged in! 🎉')