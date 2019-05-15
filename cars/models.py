from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

import datetime

CATEGORIES = enumerate(('ekonomiczna', 'biznesowa', 'pierwsza'))
ENGINES = enumerate(('spalinowy', 'hybrydowy', 'elektryczny'))
CAR_TYPES = enumerate(('Limousine', 'Mini-Bus', 'Sedan', 'Stretch limousine', 'SUV', 'Van', 'Other'))


class Producer(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    name = models.CharField(max_length=25)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    car_type = models.IntegerField(choices=CAR_TYPES)

    def __str__(self):
        return "{}: {}".format(self.producer, self.name)


class Car(models.Model):
    reg_num = models.CharField('registration number', max_length=10)
    max_pass = models.PositiveIntegerField(
        'max passengers',
        validators=[MinValueValidator(1), MaxValueValidator(30)],
        default=1)
    prod_year = models.PositiveIntegerField(
        'production year', validators=[MinValueValidator(1970), MaxValueValidator(datetime.datetime.now().year)])
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    category = models.IntegerField(choices=CATEGORIES)
    engine = models.IntegerField(choices=ENGINES)

    def __str__(self):
        return self.reg_num
