from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class Member(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     phone = models.CharField(max_length=15, blank=True)
#     join_date = models.DateTimeField(auto_now_add=True)


#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
    
#     class Meta:
#         db_table='member'

class Subscriber(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.phone
    
    class Meta:
        db_table='subscriber'


class MembershipPlan(models.Model):
    name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField(help_text="Duration in months")
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name
    
    
    class Meta:
        db_table='membershipplan'

class Payment(models.Model):
    member = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField()
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.member} - {self.date}"
    
    
    class Meta:
        db_table='payment'

class Attendance(models.Model):
    member = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    date = models.DateField()
    attendance_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.member} - {self.date}"
    
    
    class Meta:
        db_table='attendance'

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)
    contact = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.name
    
    
    class Meta:
        db_table='trainer'

class GymEquipment(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
    
    class Meta:
        db_table='gymequipment'
