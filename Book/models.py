from django.db import models

class Work(models.Model):
    place = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    def __str__(self):
        return self.place

class Street(models.Model):
    street_name = models.CharField(max_length=50)
    def __str__(self):
        return self.street_name

class City(models.Model):
    city_name = models.CharField(max_length=50)
    def __str__(self):
        return self.city_name


class User(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    patron = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)

    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)

    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    def __str__(self):
        return "{0} {1} {2}".format(self.surname, self.name, self.patron)
    def viev(self):
        return "{0} {1} {2}".format(self.surname, self.name, self.patron)

