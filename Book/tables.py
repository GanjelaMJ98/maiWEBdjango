from django.shortcuts import render
from .models import User, Work,Street,City
from django.http import HttpResponseRedirect, HttpResponse


def street(request):
    table_list = Street.objects.all()
    context = {'table_list': table_list, "table": "street"}
    return render(request, 'Table/tamplate.html', context)

def city(request):
    table_list = City.objects.all()
    context = {'table_list': table_list, "table": "city"}
    return render(request, 'Table/tamplate.html', context)

def work(request):
    table_list = Work.objects.all()
    context = {'table_list': table_list, "table": "work"}
    return render(request, 'Table/tamplate.html', context)




def street_view(request,value_id):
    street = Street.objects.get(id = value_id)
    street_list = list()
    street_list.append(street.street_name)
    context = {'value': street, "table": "street", "value_list": street_list}
    return render(request, 'Table/change.html', context)

def city_view(request,value_id):
    city = City.objects.get(id = value_id)
    city_list = list()

    city_list.append(city.city_name)

    context = {'value': city, "table": "city", "value_list": city_list}
    return render(request, 'Table/change.html', context)

def work_view(request,value_id):
    work = Work.objects.get(id = value_id)
    work_list = list()
    work_list.append(work.place)
    work_list.append(work.position)
    context = {'value': work, "table": "work", "value_list": work_list}
    return render(request, 'Table/change.html', context)


