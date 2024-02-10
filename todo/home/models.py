from django.db import models

# Create your models here.
class Task(models.Model):
     taskTitle=models.CharField(max_length=30)
     taskDese=models.TextField(max_length=300)
     time=models.DateTimeField(auto_now_add=True)

     def __str__(self):
          return self.taskTitle