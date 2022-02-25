from django.db import models

# Create your models here.
class Note(models.Model):
    title=models.CharField(verbose_name='Заголовок', max_length=50)
    content=models.TextField(verbose_name='Контент')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title