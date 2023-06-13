from django.db import models

# Create your models here.
class Memo(models.Model):
    title = models.CharField(verbose_name="제목", max_length=20)
    content = models.TextField(verbose_name="내용")
