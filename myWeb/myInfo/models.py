from django.db import models

# Create your models here.
class ExamInfo(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=10000)

    def __str__(self):
        return self.title

class Admin(models.Model):
    name = models.CharField(max_length=10)
    p_id = models.CharField(max_length=20)
    p_class = models.CharField(max_length=20)
    #exam = models.ForeignKey('ExamInfo',on_delete=models.CASCADE)
