from django.db import models

# Create your models here.
class Kategori(models.Model):
    isim = models.CharField(max_length=100)

    def __str__(self):
        return self.isim

class Movie(models.Model):
    kategori = models.ForeignKey(Kategori ,on_delete=models.CASCADE)
    isim = models.CharField(max_length=200)
    resim = models.FileField(upload_to="filmler/",null=True ,verbose_name="film resmi")
    film = models.FileField(upload_to="film/",null=True ,verbose_name="film video")

    def __str__(self):
        return self.isim
    
