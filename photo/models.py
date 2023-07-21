from django.db import models
from django.urls import reverse
from photo.fields import ThumbnailImageField
from django.utils import timezone

class Album(models.Model):
    name = models.CharField('NAME',max_length = 50, null=True)
    description = models.CharField('Explain briefly.', max_length=50, blank=True, null=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null= True)

    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('photo:album_detail', args=(self.id,))

class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete= models.CASCADE)
    title = models.CharField('TITLE', max_length=30)
    description = models.TextField('Photo Description', blank=True)
    image = ThumbnailImageField('IMAGE',upload_to='photo/%Y/%m')
    #image = ('IMAGE', upload_to='SorlPhoto/%Y')
    upload_dt = models.DateTimeField('UPLOAD DATE', auto_now_add=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)

    class Meta:
        ordering = ('title',)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=(self.id,))

# Create your models here.
