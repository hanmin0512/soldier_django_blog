from django.db import models
from django.urls import reverse
from photo.fields import ThumbnailImageField
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField('TITLE', max_length=20)
    content = models.TextField('CONTENT', blank=True)
    upload_date = models.DateTimeField('Update Date', auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)
    tag = TaggableManager(blank=True)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, null=True, blank=True)
    class Meta:
        ordering = ('-upload_date',)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'post'
        ordering = ('-upload_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:post_detail', args=(self.id,))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

class IMG(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = ThumbnailImageField('IMAGE', upload_to = 'photo/%Y/%m')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)
        # Create your models here.
