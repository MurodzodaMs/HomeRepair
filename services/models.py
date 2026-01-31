from django.db import models
from accounts.models import CustomUser
from brigade.models import Brigade


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image = models.ImageField(upload_to='categories/', null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Service(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='services', on_delete=models.CASCADE
                                 )
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    brigade = models.ForeignKey(Brigade, null=True, on_delete=models.CASCADE)


class ServicePhoto(models.Model):
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField()
