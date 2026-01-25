from django.db import models
from accounts.models import CustomUser
from services.models import *

class Order(models.Model):
    STATUS_CHOISES = (
        ('created', 'created'),
        ('accepted', 'accepted'),
        ('in_progress', 'in_progress'),
        ("completed", 'completed')
    )


    client = models.ForeignKey(CustomUser, 
        related_name='user_orders', on_delete=models.CASCADE
    )
    service = models.ForeignKey(Service,
        related_name='service_order', on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    status = models.CharField(max_length=20, 
        choices=STATUS_CHOISES, default='created'
    )
    start_date = models.DateField()
    end_date = models.DateField()
    is_delete = models.BooleanField(default=False)

    


class OrderImage(models.Model):
    order = models.ForeignKey(Order, 
        related_name='order_image', on_delete=models.CASCADE    
    )
    image = models.ImageField()


