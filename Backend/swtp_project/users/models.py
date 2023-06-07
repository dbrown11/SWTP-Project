from decimal import Decimal
from enum import unique
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, DateField, DateTimeField, DecimalField, TextField, ManyToManyField, ForeignKey, JSONField
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Car(models.Model):
    reg_number = CharField(unique=True,max_length=8)

    def __str__(self):
        return self.reg_number

class User(AbstractUser):
    """
    Default custom user model for swtp-project.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    dob =  DateField(blank=True, null=True)
    address = TextField(blank=True, null=True)
    postcode = CharField(blank=True, null=True, max_length=8)

    cars_owned = ManyToManyField(Car)
    #phone number 
    #referal code
    #links to friends
    #list of cars? (array)
    #score
    #history of journeys 


    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})



class Journey(models.Model):
    user = ForeignKey(User,on_delete=models.CASCADE)
    car = ForeignKey(Car,on_delete=models.CASCADE)
    distance_miles = DecimalField(max_digits=7, decimal_places=2)
    energy_used_kwh = DecimalField(max_digits=7, decimal_places=2)
    start_time = DateTimeField()
    end_time = DateTimeField() 
    start_battery_percent = DecimalField(max_digits=6, decimal_places=2)
    end_battery_percent = DecimalField(max_digits=6, decimal_places=2)

    data = JSONField(null=True)

    def __str__(self):
        return self.car.reg_number
    
    
    
    ''''
    
    class car 
        reg_number
        engine_size/motor_size
        battery size
        vin number
        age
        power 
        model
        weight?
        avg_efficenty - mpg/ mpkwh


    class journey
        user 
        car
        distance
        speed
        avg energy used
        gps_coordinates?
        accleration
        time 
        breaking
        weather 
        pressures
        energy_usage 

        vechile status 
    '''