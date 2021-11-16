import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

# Set up credentials
cred = credentials.Certificate(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'service-account.json'))

firebase_admin.initialize_app(cred, {
    'storageBucket': os.environ['PROJECT_ID'] + '.appspot.com'
})

firestore_db = firestore.client()

def query():
    snapshots = list(firestore_db.collection(os.environ['TABLE_ID']).get())

    result = []

    for snapshot in snapshots:
        result.append(snapshot.to_dict())

    return result
