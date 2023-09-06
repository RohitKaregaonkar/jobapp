from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse 
from django.template import loader

job_title = [
    'Home',
    'First Job',
    'Second Job'
]

job_description = [
    'Home',
    'First Job Description',
    'Second Job Description'
]

def hello(request):
    template = loader.get_template('app/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def home(request):
    job_list = "<ul>"
    for j in job_title:
        job_id = job_title.index(j)
        url= reverse('job_details', args=(job_id,))
        job_list += f"<li><a href='{url}'>{j}</a></li>"
    job_list += "</ul>"
    
    return HttpResponse(job_list)

def job_details(request, id):
    try:
        if id == 0:
            return redirect(reverse('home'))
        job_data = f'<h1>{job_title[id]}</h1><h3>{job_description[id]}</h3>'
        return HttpResponse(job_data)
    except:
        return HttpResponseNotFound("Not Found")