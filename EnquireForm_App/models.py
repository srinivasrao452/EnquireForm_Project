
from django.db import models
from multiselectfield import MultiSelectField

# Add one coment line from github server

class EnquireData(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    mobile = models.BigIntegerField()

    COURSES_CHOICES = (
        ('Python', 'Python'),
        ('Django','Django'),
        ('Flask', 'Flask'),
        ('REST_API', 'REST_API'),
    )
    course = MultiSelectField(choices=COURSES_CHOICES)

    Location_Choices = (
        ('Hyderabad','Hyd'),
        ('Bangalore','Bang'),
        ('Chennai','Che'),
    )
    location = MultiSelectField(choices=Location_Choices)

    start_date = models.DateField(max_length=100)  # mm/dd/yyyy

    gender = models.CharField(max_length=10)




