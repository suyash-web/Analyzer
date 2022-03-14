from django.http import HttpResponse
from django.shortcuts import render
import requests
from requests.structures import CaseInsensitiveDict


def index(request):
    return render(request, 'index.html')

def analyzer(request):
    context = {}
    txt = request.GET.get('website', 'please enter your website here')
    mail = request.GET.get('email', 'please enter your email here')
    context["website"] = txt
    context["email"] = mail
    website_matches = ["https://www."]
    email_matches = ["@", ".com"]
    if any(x not in txt for x in website_matches) and any(x not in mail for x in email_matches):
        return render(request, 'badcredentials.html')
    if any(x not in txt for x in website_matches):
        return render(request, 'badwebsite.html')
    if any(x not in mail for x in email_matches):
        return render(request, 'bademail.html')
    else:
        url = "https://api.eu1.robocorp.com/process-v1/workspaces/94cf01b3-52bd-4cc4-be2e-3288fa65dc12/processes/7152992f-fd54-405f-b092-0ff199afb88e/runs?"
        headers = CaseInsensitiveDict()
        headers["Authorization"] = "RC-WSKEY 78fyFDhRr0h7kMQ6sBAmUAsvDmz71FeCZNULSVPjCKMKGCasYBpllIGZOeyB8Ltzyy1hV0cZGlwfXMgqgUwqZxxYXKH0c"
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        data = {txt : mail}
        requests.post(url, headers=headers, json=data)
        return render(request, 'goodrequest.html', context=context)