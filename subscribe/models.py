from django.db import models

NEWSLETTER_OPTIONS = [
    ('W', 'Weekly'),
    ('M', 'Monthly')
]

# Create your models here.
class Subscribe(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    option = models.CharField(max_length=2, choices=NEWSLETTER_OPTIONS, default='W')
        