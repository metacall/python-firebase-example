import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
from os.path import join, dirname, abspath

# Set up credentials
cred = credentials.Certificate(join(dirname(abspath(__file__)), 'service-account.json'))

firebase_admin.initialize_app(cred, {
    'storageBucket': os.environ['STORAGE_ID'] + '.appspot.com'
})

bucket = storage.bucket(os.environ['BUCKET_ID'])

def query():
    return list(bucket.list_blobs())
