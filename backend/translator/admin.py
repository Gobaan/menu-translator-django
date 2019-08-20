from django.contrib import admin
from django import forms
from .models import Annotation, Clip, Food, Image, Language, Website, UserProfile

class AnnotationAdminForm(forms.ModelForm):

    class Meta:
        model = Annotation
        fields = '__all__'


class AnnotationAdmin(admin.ModelAdmin):
    form = AnnotationAdminForm
    list_display = ['slug', 'created', 'last_updated', 'text', 'annotates_source_language']
    readonly_fields = ['slug', 'created', 'last_updated', 'text', 'annotates_source_language']

admin.site.register(Annotation, AnnotationAdmin)


class ClipAdminForm(forms.ModelForm):

    class Meta:
        model = Clip
        fields = '__all__'


class ClipAdmin(admin.ModelAdmin):
    form = ClipAdminForm
    list_display = ['slug', 'created', 'last_updated', 'bounding_box']
    readonly_fields = ['slug', 'created', 'last_updated', 'bounding_box']

admin.site.register(Clip, ClipAdmin)


class FoodAdminForm(forms.ModelForm):

    class Meta:
        model = Food
        fields = '__all__'


class FoodAdmin(admin.ModelAdmin):
    form = FoodAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated']
    readonly_fields = ['name', 'slug', 'created', 'last_updated']

admin.site.register(Food, FoodAdmin)


class ImageAdminForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = '__all__'


class ImageAdmin(admin.ModelAdmin):
    form = ImageAdminForm
    list_display = ['slug', 'created', 'last_updated', 'cloud_URL', 'filesize', 'longitude', 'latitude', 'width', 'height']
    readonly_fields = ['slug', 'created', 'last_updated', 'cloud_URL', 'filesize', 'longitude', 'latitude', 'width', 'height']

admin.site.register(Image, ImageAdmin)


class LanguageAdminForm(forms.ModelForm):

    class Meta:
        model = Language
        fields = '__all__'


class LanguageAdmin(admin.ModelAdmin):
    form = LanguageAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'short_name']
    readonly_fields = ['name', 'slug', 'created', 'last_updated', 'short_name']

admin.site.register(Language, LanguageAdmin)


class WebsiteAdminForm(forms.ModelForm):

    class Meta:
        model = Website
        fields = '__all__'


class WebsiteAdmin(admin.ModelAdmin):
    form = WebsiteAdminForm
    list_display = ['slug', 'created', 'last_updated', 'URL', 'cache_path']
    readonly_fields = ['slug', 'created', 'last_updated', 'URL', 'cache_path']

admin.site.register(Website, WebsiteAdmin)


class UserProfileAdminForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileAdmin(admin.ModelAdmin):
    form = UserProfileAdminForm
    list_display = ['slug', 'created', 'last_updated', 'category']
    readonly_fields = ['slug', 'created', 'last_updated', 'category']

admin.site.register(UserProfile, UserProfileAdmin)


