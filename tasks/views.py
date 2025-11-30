from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Task Tracker Home Page")

def task_list(request):
    tasks = ["Learn Docker", "Build Django App", "Deploy Application"]
    task_html = "<br>".join([f"- {task}" for task in tasks])
    return HttpResponse(f"<h2>My Tasks:</h2>{task_html}")

def about(request):
    return HttpResponse("<h2>About Task Tracker</h2><p>Simple app to learn Django and Docker</p>")