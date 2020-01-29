from django.db import models


class Contact(models.Model):

    contact_name = models.CharField(max_length=50,blank=True,null=True)
    contact_group = models.CharField(max_length=50,blank=True,null=True)
    phone = models.CharField(max_length=20,blank=True,null=True)
    email = models.EmailField(max_length=30,blank=True,null=True)

    def __str__(self):
        return self.name
