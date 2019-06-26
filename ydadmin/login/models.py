from django.db import models

# Create your models here.
class Grade(models.Model):
	gname = models.CharField( max_length=20 )
	gdate = models.DateTimeField()


