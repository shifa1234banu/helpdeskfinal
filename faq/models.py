from django.db import models
from organization.models import Organization
# Create your models here.



class Faq(models.Model):
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)