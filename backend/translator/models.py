from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import BooleanField
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import DecimalField
from django.db.models import IntegerField
from django.db.models import TextField
from django.db.models import URLField
from django_extensions.db.fields import AutoSlugField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields
from django.utils import timezone

class TrackedMixin(models.Model):
    slug = extension_fields.AutoSlugField(populate_from='id', blank=True)
    created = models.DateTimeField(default=timezone.now, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

class Annotation(TrackedMixin):
    # Fields
    text = models.TextField()
    annotates_source_language = models.BooleanField()

    # Relationship Fields
    clip = models.ForeignKey(
        'translator.Clip',
        on_delete=models.CASCADE, related_name="annotations", 
        null=True
    )
    creator = models.ForeignKey(
        'translator.UserProfile',
        on_delete=models.CASCADE, related_name="annotations", 
        null=True
    )
    language = models.ForeignKey(
        'translator.Language',
        on_delete=models.CASCADE, related_name="annotations", 
    )

    def get_absolute_url(self):
        return reverse('translator_annotation_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('translator_annotation_update', args=(self.slug,))


class Clip(TrackedMixin):
    # Fields
    bounding_box = models.TextField(max_length=100)

    # Relationship Fields
    image = models.ForeignKey(
        'translator.Image',
        on_delete=models.CASCADE, related_name="clips", 
    )
    creator = models.ForeignKey(
        'translator.UserProfile',
        on_delete=models.CASCADE, related_name="clips", 
        null=True
    )

    def get_absolute_url(self):
        return reverse('translator_clip_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('translator_clip_update', args=(self.slug,))



class Image(TrackedMixin):
    # Fields
    cloud_URL = models.URLField()
    filesize = models.IntegerField()
    longitude = models.IntegerField()
    latitude = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()

    # Relationship Fields
    original_image = models.ForeignKey(
        'translator.Image',
        on_delete=models.CASCADE, related_name="images", 
        null=True
    )

    creator = models.ForeignKey(
        'translator.UserProfile',
        on_delete=models.CASCADE, related_name="images", 
        null=True
    )

    def get_absolute_url(self):
        return reverse('translator_image_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('translator_image_update', args=(self.slug,))


class Language(TrackedMixin):

    # Fields
    name = models.CharField(max_length=255)
    short_name = models.TextField(max_length=10)


class Website(TrackedMixin):

    # Fields
    URL = models.URLField()
    cache_path = models.URLField()

    # Relationship Fields
    food = models.ForeignKey(
        'translator.Food',
        on_delete=models.CASCADE, related_name="websites", 
    )

    creator = models.ForeignKey(
        'translator.UserProfile',
        on_delete=models.CASCADE, related_name="websites", 
        null=True
    )


class UserProfile(TrackedMixin):

    # Fields
    category = models.TextField(max_length=100, choices=(
        ('GOOGLE', 'google-api'), 
        ('CUSTOM', 'custom-api'), 
        ('JUDGE', 'judge'),
        ('NORMAL', 'normal')))

    # Relationship Fields
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name="profile", 
    )

    def get_absolute_url(self):
        return reverse('translator_userprofile_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('translator_userprofile_update', args=(self.slug,))


class Food(TrackedMixin):
    # Fields
    name = models.CharField(max_length=255)

    # Relationship Fields
    language = models.ForeignKey(
        'translator.Language',
        on_delete=models.CASCADE, related_name="foods", 
    )
    thumbnails = models.ManyToManyField(Image)
    creator = models.ForeignKey(
        'translator.UserProfile',
        on_delete=models.CASCADE, related_name="foods", 
        null=True
    )


    def get_absolute_url(self):
        return reverse('translator_food_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('translator_food_update', args=(self.slug,))

