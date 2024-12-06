from django.db import models

# Create your models here.
class Customers(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    about_customers = models.TextField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
        ordering = ['-published']

    def __str__(self):
        return self.name