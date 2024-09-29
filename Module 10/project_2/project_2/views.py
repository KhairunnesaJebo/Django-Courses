from django.shortcuts import render

# /home/jebo/Desktop/Django/project_2/templates

def index(request):
    return render(request,'index.html')