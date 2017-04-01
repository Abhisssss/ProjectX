
import httplib, urllib, base64
from django.shortcuts import render
from django.template import loader
from django.template import Context

from django.conf import settings
def createPerson(request):

    headers = {
    # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '800be4bdc4b8456f9266ab1177104bc3',
    }

    params = urllib.urlencode({'personGroupId':'4thyearcse'
    })

    if request.method == 'GET' :
        usn = str(request.GET.get('usn',''))
        name=str(request.GET.get('name',''))
        

        try:
            body='{"name":"'+usn+'","userData":"'+name+'"}'
            print body
            conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
            conn.request("POST", "/face/v1.0/persongroups/{personGroupId}/persons?%s" % params, str(body), headers)
            response = conn.getresponse()
            data = response.read()
            #print(data)
            conn.close()
        except Exception as e:
            print e
            #print("[Errno {0}] {1}".format(e.errno, e.strerror))
        return render(request, 'testing/createperson.html', {
            'uploaded_file_url': data

            })
    return render(request, 'testing/createperson.html')

