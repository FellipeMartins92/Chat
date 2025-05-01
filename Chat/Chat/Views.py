from django.shortcuts import render
from Users.models import custom_login_required

@custom_login_required
def Home(request):
    return render(request,"Home.html")
