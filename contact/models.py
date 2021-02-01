from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField('Tên liên lạc', max_length=100, null=True)
    phone_number = models.CharField('Số điện thoại', max_length=13, null=False)
    type = models.IntegerField('Loại', default=1)

    def __str__(self):
        return self.name