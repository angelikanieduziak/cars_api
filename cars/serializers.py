from .models import Car, CarModel
from rest_framework import serializers


class CarModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarModel
        fields = ('id', 'name', 'producer', 'car_type')


class CarSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Car
        fields = ('id', 'reg_num', 'max_pass', 'prod_year', 'model', 'category', 'engine')


