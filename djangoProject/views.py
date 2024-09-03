from django.shortcuts import render
from database.models import Student

def home(request):
    data = Student.objects.all()
    return render(request, 'home.html', {'data':data})

def edit_data(request):
    ID = request.GET['id']
    data = Student.objects.get(pk=ID)
    return render(request, 'edit.html', {'data':data})

def add_data(request):
    return render(request, 'add.html')
