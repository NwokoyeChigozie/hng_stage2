from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255, blank=False, null=True)
    email = models.EmailField(blank=False, max_length=255, verbose_name="email")
    message = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name