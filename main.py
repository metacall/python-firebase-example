import os
from firebase import firebase

auth = firebase.Authentication(os.environ['API_KEY'], os.environ['API_EMAIL'])
firebase = firebase.FirebaseApplication(os.environ['API_URL'], authentication=auth)

def query():
    return firebase.get('/sessions', None, {'print': 'pretty'})
