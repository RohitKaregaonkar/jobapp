from django.shortcuts import render
from subscribe.models import Subscribe
from subscribe.forms import SubscribeForm

# Create your views here.
def subscribe(request):
    subscribe_form = SubscribeForm()
    email_error = ""
    if request.POST:
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            print("Valid Form")
            print(subscribe_form.cleaned_data)
            fname = subscribe_form.cleaned_data['first_name']
            lname = subscribe_form.cleaned_data['last_name']
            email = subscribe_form.cleaned_data['email']
            
            subscribe = Subscribe(first_name= fname, last_name= lname, email= email)
            subscribe.save()
            
    #     fname = request.POST['fname']
    #     lname = request.POST['lname']
    #     email = request.POST['email']

    #     if email == "":
    #         email_error = "No Email Entered!"

    #     subscribe = Subscribe(first_name = fname, last_name = lname, email = email)
    #     subscribe.save()

    context = {"form":subscribe_form, "email_error": email_error}
    return render(request, "subscribe/subscribe.html", context)