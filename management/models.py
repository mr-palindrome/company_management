from uuid import UUID
from django.db import models
import uuid


# Create your models here.

class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    company_name = models.CharField(max_length=100)
    company_ceo = models.CharField(max_length=100)
    company_address = models.CharField(max_length=100)
    inception_Date = models.DateField()

    def __str__(self):
        return self.company_name
