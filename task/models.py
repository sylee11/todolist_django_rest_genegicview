from django.db import models

# Create your models here.

class Tasks(models.Model):
    title = models.CharField('Tiêu đề', max_length=255, )
    status = models.BooleanField("Trạng thái", default=False)

    def __str__(self):
        return  self.title