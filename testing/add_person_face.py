
import httplib, urllib, base64
from django.shortcuts import render
from django.template import loader
from django.template import Context
from django.conf import settings
from . import detectface

def addFace(request):


    headers = {
    # Request headers
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': '800be4bdc4b8456f9266ab1177104bc3',
    }

    params = urllib.urlencode({
    # Request parameters
    'userData': '{string}',
    'targetFace': '{string}',
    })
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        #data= open(myfile, "rb").read()
        data=myfile.read()
        #faceid=detectface.detectFace(data)
        #print faceid

        personid = str(request.POST.get('personid',''))
        
        
        try:

            conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
            conn.request("POST", "/face/v1.0/persongroups/4thyearcse/persons/%s/persistedFaces?"%personid , data, headers)
            response = conn.getresponse()
            data = response.read()
            print(data)
            conn.close()
        except Exception as e:
            print e
            #print("[Errno {0}] {1}".format(e.errno, e.strerror))
        return render(request, 'testing/addpersonface.html', {
            'status': data
        })
    return render(request, 'testing/addpersonface.html')

