from django.db import models

class Aboutus(models.Model):
    title = models.CharField(max_length=40)
    text = models.TextField(max_length=500)
    image = models.ImageField(upload_to='media/about')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Biz Haqimizda'
        verbose_name_plural = 'Bizning o`quv markaz haqida'



