from django.db import models

class Brigade(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey("services.Category", 
        related_name="brigades", on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    