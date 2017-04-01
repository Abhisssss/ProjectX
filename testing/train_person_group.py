
import httplib, urllib, base64
from django.shortcuts import render
from django.template import loader
from django.template import Context
from django.conf import settings
def trainGroup(request):
    headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '800be4bdc4b8456f9266ab1177104bc3',
    }

    params = urllib.urlencode({
    })
    if request.method == 'POST':
        groupid = str(request.POST.get('groupid',''))

        try:
            conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
            conn.request("POST", "/face/v1.0/persongroups/%s/train?%s" % (groupid,params), "", headers)
            response = conn.getresponse()
            data = response.read()
            print(data)
            conn.close()
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))
        return render(request, 'testing/traingroup.html', {
            'status': data
        })
    return render(request, 'testing/traingroup.html')



