from django import forms
from .models import Annotation, Clip, Food, Image, Language, Website, UserProfile


class AnnotationForm(forms.ModelForm):
    class Meta:
        model = Annotation
        fields = ['text', 'annotates_source_language', 'creator', 'language', 'clip']


class ClipForm(forms.ModelForm):
    class Meta:
        model = Clip
        fields = ['bounding_box', 'image', 'creator']


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'language', 'thumbnails', 'creator']


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['cloud_URL', 'filesize', 'longitude', 'latitude', 'width', 'height', 'original_image']


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['name', 'short_name']


class WebsiteForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = ['URL', 'cache_path', 'food']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['category', 'user']


