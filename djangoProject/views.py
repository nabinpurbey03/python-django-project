import re

from django.shortcuts import render
from database.models import Student

def home(request):
    data = Student.objects.all()
    return render(request, 'home.html', {'data':data})

def edit_data(request):
    ID = request.GET['id']
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        validated = True if first_name and last_name and email and phone else False
        errors = ["Error found! Please enter all the fields."]
        if validated:
            if len(phone) < 10:
                errors.append("Phone number must be at least 10 digits.")
                validated = False
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            if re.match(regex, email) is None:
                errors.append("Email address is invalid.")
                validated = False
        if validated:
            Student.objects.filter(id=ID).update(first_name=first_name, last_name=last_name, email=email, phone_number=phone)
            return home(request)
        else:
            return render(request, 'edit.html', {'error_status': True, 'errors': errors})



    data = Student.objects.get(pk=ID)
    return render(request, 'edit.html', {'data':data})

def add_data(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        validated = True if first_name and last_name and email and phone else False
        errors = ["Error found! Please enter all the fields."]
        if validated:
            if len(phone) < 10:
                errors.append("Phone number must be at least 10 digits.")
                validated = False
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            if re.match(regex, email) is None:
                errors.append("Email address is invalid.")
                validated = False
        if validated:
            em = Student.objects.create(first_name=first_name, last_name=last_name, email=email, phone_number=phone)
            em.save()
            return home(request)
        else:
            return render(request, 'add.html', {'error_status': True, 'errors': errors})
    return render(request, 'add.html')

