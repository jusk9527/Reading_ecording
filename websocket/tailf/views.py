from django.shortcuts import render

# Create your views here.


from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def tailf(request):
    logDict = settings.TAILF
    return render(request, 'chat/index.html', {"logDict": logDict})