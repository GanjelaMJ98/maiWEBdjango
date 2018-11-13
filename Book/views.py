from django.shortcuts import render
from .models import User, Work,Street,City
from django.http import HttpResponseRedirect, HttpResponse



# Create your views here.
def index(request):
    user_list = User.objects.all()[:10]
    context = {'user_list': user_list}
    return render(request, 'Book/index.html', context)

def add(request):
    user_list = User.objects.all()[:10]
    context = {'user_list': user_list}
    return render(request, 'Book/add.html', context)

def input(request):
    name = request.POST['name']
    surname = request.POST['surname']
    patron = request.POST['patron']
    gender = request.POST['gender']
    number = request.POST['number']
    email = request.POST['email']
    street = request.POST['street']
    city = request.POST['city']
    work_place = request.POST['work1']
    work_position = request.POST['work2']
    new_work = Work(place = work_place, position = work_position)
    new_street = Street(street_name = street)
    new_city = City(city_name = city)
    new_work.save()
    new_street.save()
    new_city.save()
    new_user = User(name = name, surname = surname,patron = patron,gender = gender,number = number, email = email,city = new_city, street = new_street,work = new_work )
    new_user.save()

    user_list = User.objects.all()[:10]
    context = {'user_list': user_list}
    return render(request, 'Book/index.html', context)