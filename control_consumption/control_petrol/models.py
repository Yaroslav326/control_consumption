from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    birth_date = models.DateField()
    region = models.CharField(max_length=100)


    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Car(models.Model):
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    car_type = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=100)
    consumption = models.DecimalField(max_digits=5, decimal_places=2)
    win_code = models.CharField(max_length=100)
    year = models.IntegerField()

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


class Station(models.Model):
    station_name = models.CharField(max_length=200)
    region = models.CharField(max_length=100)
    distance = models.IntegerField()


class Route(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    date = models.DateField()


    class Meta:
        verbose_name = 'Маршрут'
