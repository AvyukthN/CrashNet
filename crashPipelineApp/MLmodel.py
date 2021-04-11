import cv2
import numpy as np
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import geocoder
import smtplib
from credentials import gmail_pass

# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture('crash.mp4')

# Check if camera opened successfully
if (cap.isOpened()== False):
 print("Error opening video  file")

start = time.time()
while(cap.isOpened()):
 currTime = time.time()
 if currTime - start >= 8:
    g = geocoder.ip('me')

    location = g.latlng

    print("=== CRASH DETECTED ===")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    print(gmail_pass['mail'], gmail_pass['pass'])

    server.login(gmail_pass['mail'], gmail_pass['pass'])

    subject = 'AVY BYARD UPDATE'
    body = "CAR CRASH AT " + str(location[0]) + ", " + str(location[1])

    msg = f"Subject: {subject}\n\n{body}"

    sender = "avyukthnilajagi@gmail.com"
    recipients = ["maanas.baraya@gmail.com", "vchitturi9@gmail.com", "avyukthnilajagi@gmail.com"]
    for i in range(len(recipients)):
        server.sendmail(sender, recipients[i], msg)
    print(" == EMAIL SENT == ")
    file1 = open("myfile.txt","w")
    file1.write("Car Crash")
    file1.close()
    cap.release()
    cv2.destroyAllWindows()
    cred = credentials.Certificate("./credentials.json")
    firebase_admin.initialize_app(cred)

    db = firestore.client()

    data = {

        u'location': g.latlng,
        u'description': "CRASH",
    }
    # Add a new doc in collection 'cities' with ID 'LA'
    db.collection(u'crashSites').document(u'location').set(data)
 # Capture frame-by-frame
 ret, frame = cap.read()
 if ret == True:

   # Display the resulting frame
   cv2.imshow('Frame', frame)

   # Press Q on keyboard to  exit
   if cv2.waitKey(25) & 0xFF == ord('q'):
     break

 # Break the loop
 else:
   break

# When everything done, release
# the video capture object

cap.release()

# Closes all the frames
cv2.destroyAllWindows()