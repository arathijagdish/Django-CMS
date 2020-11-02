from django.db import models
from django.db.models.fields import DateTimeField
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    id = models.BigAutoField(
        primary_key=True
    )

    title = models.CharField(
        max_length=170,
        verbose_name="Title",
        help_text="Post title",
        blank=False,
        null=False
    )

    featured_image = models.ImageField(
        upload_to = 'images/',
        blank = True,
    )
    
    body = models.TextField(
        verbose_name="Body",
        help_text="Post content",
        blank=False,
        null=False
    )

    created_on = models.DateTimeField(
        verbose_name="Published on",
        auto_now_add=True
    )

    updated_on = models.DateTimeField(
        verbose_name='Last updated',
        auto_now=True,
    )
    slug = models.CharField(
        verbose_name="Slug",
        max_length=200,
        unique=True
    )
    description = models.CharField(
        max_length=255,
        null=False,
        blank=True,
        help_text='This will be added as the meta description.'
    )
    created_by = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
