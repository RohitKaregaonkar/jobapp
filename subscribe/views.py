from django.shortcuts import render
from subscribe.models import Subscribe

# Create your views here.
def subscribe(request):
    email_error = ""
    if request.POST:
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']

        if email == "":
            email_error = "No Email Entered!"

        subscribe = Subscribe(first_name = fname, last_name = lname, email = email)
        subscribe.save()
        
        
    context = {"email_error": email_error}
    return render(request, "subscribe/subscribe.html", context)