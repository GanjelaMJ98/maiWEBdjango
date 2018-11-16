from django.shortcuts import render
from .models import User, Work,Street,City
from django.http import HttpResponseRedirect, HttpResponse



# Create your views here.
def index(request):
    user_list = User.objects.all()[:10]
    context = {'user_list': user_list}
    return render(request, 'Book/index.html', context)

def add_view(request):
    user_list = User.objects.all()[:10]
    context = {'user_list': user_list}
    return render(request, 'Book/add_view.html', context)

def add(request):
    name = request.POST['name']
    surname = request.POST['surname']
    patron = request.POST['patron']
    gender = request.POST['gender']
    number = request.POST['number']
    email = request.POST['email']
    street = request.POST['street']
    city = request.POST['city']
    work_place = request.POST['place']
    work_position = request.POST['position']

    current_street = Street.objects.filter(street_name = street)
    print(type(current_street))
    if not current_street:
        print("//////////////////////////////////")
        new_street = Street(street_name=street)
        new_street.save()
        print("new street added: {0}".format(new_street.street_name))
    else:
        print("+++++++++++++++++++++++++++++++++++++++")
        new_street = current_street[0]
        print("alrady exist: {0}".format(new_street.street_name))

    current_city = City.objects.filter(city_name = city)
    if not current_city:
        new_city = City(city_name=city)
        new_city.save()
        print("new city added: {0}".format(new_city.city_name))
    else:
        new_city = current_city[0]
        print("alrady exist: {0}".format(new_city.city_name))

    current_work = Work.objects.filter(place = work_place, position = work_position)
    if not current_work:
        new_work = Work(place = work_place, position = work_position)
        new_work .save()
        print("new work  added: {0}".format(new_work.view()))
    else:
        new_work = current_work[0]
        print("alrady exist: {0}".format(new_work.view()))

    new_user = User(name = name, surname = surname,patron = patron,gender = gender,number = number, email = email,city = new_city, street = new_street,work = new_work )
    new_user.save()

    return render(request, 'Book/add.html')


def search(request):
    if not request.POST['patron']:
        gender = None
    else:
        gender = request.POST['gender']
    if not request.POST['name']:
        name = None
    else:
        name = request.POST['name']


    surname = request.POST['surname']
    patron = request.POST['patron']
    number = request.POST['number']
    email = request.POST['email']
    user_list = User.objects.filter(name = "Павел")
    print(user_list)
    context = {'user_list': user_list}
    return render(request, 'Book/search.html', context)


def delete_view(request, user_id):
    user = User.objects.get(id = user_id)
    context = {'user': user}
    return render(request, 'Book/delete_view.html', context)

def delete(request, user_id):
    user = User.objects.get(id = user_id)
    context = {'user': user}
    user.delete()
    return render(request, 'Book/delete.html', context)

def change_view(request, user_id):
    user = User.objects.get(id = user_id)
    streets = Street.objects.all()
    cities = City.objects.all()
    works = Work.objects.all()
    if user.gender == "Man":
        context = {'user': user, 'streets': streets, 'cities': cities, 'works': works , "gender": "Man"}
    else:
        context = {'user': user, 'streets': streets, 'cities': cities, 'works': works, "gender": "Woman"}
    return render(request, 'Book/change_view.html', context)

def change(request, user_id):
    user = User.objects.get(id = user_id)
    user.name = request.POST['name']
    user.surname = request.POST['surname']
    user.patron = request.POST['patron']
    user.number = request.POST['number']
    user.gender = request.POST['gender']
    user.email = request.POST['email']
    street = Street.objects.get(street_name = request.POST['street'])
    user.street = street
    city = City.objects.get(city_name=request.POST['city'])
    user.city = city
    work = Work.objects.get(place=request.POST['place'], position = request.POST['position'])
    user.work = work
    user.save()
    context = {'user': user}
    return render(request, 'Book/change.html', context)

