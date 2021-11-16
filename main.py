from firebase import firebase
firebase = firebase.FirebaseApplication('https://your_storage.firebaseio.com', authentication=None)

authentication = firebase.Authentication('THIS_IS_MY_SECRET', 'ozgurvt@gmail.com', extra={'id': 123})
firebase.authentication = authentication

result = firebase.get('/users', None, {'print': 'pretty'})
print result
user = authentication.get_user()
print user.firebase_auth_token
