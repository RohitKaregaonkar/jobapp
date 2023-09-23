from django.shortcuts import render

# Create your views here.
def subscribe(request):
    email_error = ""
    if request.POST:
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']

        if email == "":
            email_error = "No Email Entered!"

    
    context = {"email_error": email_error}
    return render(request, "subscribe/subscribe.html", context)