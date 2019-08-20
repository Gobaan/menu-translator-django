from . import models

from rest_framework import serializers


class AnnotationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Annotation
        fields = (
            'slug', 
            'created', 
            'last_updated', 
            'text', 
            'annotates_source_language', 
            'clip',
        )


class ClipSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Clip
        fields = (
            'slug', 
            'created', 
            'last_updated', 
            'bounding_box', 
        )


class FoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Food
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
        )


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Image
        fields = (
            'slug', 
            'created', 
            'last_updated', 
            'cloud_URL', 
            'filesize', 
            'longitude', 
            'latitude', 
            'width', 
            'height', 
        )


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Language
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'short_name', 
        )


class WebsiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Website
        fields = (
            'slug', 
            'created', 
            'last_updated', 
            'URL', 
            'cache_path', 
        )


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserProfile
        fields = (
            'slug', 
            'created', 
            'last_updated', 
            'category', 
        )


