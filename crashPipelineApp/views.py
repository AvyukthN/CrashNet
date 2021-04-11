from django.shortcuts import render
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Create your views here.
def home(request):
    context = {}

    if not firebase_admin._apps:
        cred = credentials.Certificate("crashPipelineApp/credentials.json")
        firebase_admin.initialize_app(cred)

    db = firestore.client()
    doc_ref = db.collection(u'crashSites').document(u'location')
    # doc_ref = db.collection(u'users')

    doc = doc_ref.get()
    if doc.exists:
        print(f'Document data: {doc.to_dict()}')
        context = doc.to_dict()
        coords = (context['location'])
        description = context['description']
        latitude = float(coords[0])
        longitude = float(coords[1])
        print(latitude)
        print(longitude)
        print(description)
        return render(request, 'home2.html', {"latitude": latitude, "longitude": longitude, "description": description})
    else:
        print(u'empty')
    return render(request, 'home2.html', context)

def map(request):
    context = {}
    return render(request, 'heatmap.html', context)