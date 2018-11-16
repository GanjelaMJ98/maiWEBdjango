"""PhoneBook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include
from django.contrib import admin
from . import views
from . import tables

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_view/$', views.add_view, name='add_view'),
    url(r'^search/$', views.search, name='search'),
    url(r'^add_view/add/$', views.add, name='add'),
    url(r'^delete_view/(?P<user_id>[0-9]+)/$', views.delete_view, name='delete_view'),
    url(r'^delete/(?P<user_id>[0-9]+)/$', views.delete, name='delete'),
    url(r'^change_view/(?P<user_id>[0-9]+)/$', views.change_view, name='change_view'),
    url(r'^change/(?P<user_id>[0-9]+)/$', views.change, name='change'),
    url(r'^street/$', tables.street, name='street'),
    url(r'^city/$', tables.city, name='city'),
    url(r'^work/$', tables.work, name='work'),
    url(r'^street/(?P<value_id>[0-9]+)/$', tables.street_view, name='street_view'),
    url(r'^city/(?P<value_id>[0-9]+)/$', tables.city_view, name='city_view'),
    url(r'^work/(?P<value_id>[0-9]+)/$', tables.work_view, name='work_view'),
    url(r'^street/(?P<value_id>[0-9]+)/change/$', tables.street_view, name='street_view'),
    url(r'^city/(?P<value_id>[0-9]+)/change/$', tables.city_view, name='city_view'),
    url(r'^work/(?P<value_id>[0-9]+)/change/$', tables.work_view, name='work_view'),
]
