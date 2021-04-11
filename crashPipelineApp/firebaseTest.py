from google.cloud import firestore
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate("./credentials.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

data = {
    u'location': u'someaddress'
}
# Add a new doc in collection 'cities' with ID 'LA'
db.collection(u'crashSites').document(u'location1').set(data)

"""doc_ref = db.collection(u'users').document(u'alovelace')
doc_ref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 1815
})
db.collection("cities").doc("LA").set({
    name: "Los Angeles",
    state: "CA",
    country: "USA"
})
"""
"""db.collection(u'crashSites').doc(u'location1').set({
    u'location': u'owiejweoif'
})"""