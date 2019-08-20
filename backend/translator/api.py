from . import models
from . import serializers
from rest_framework import viewsets, permissions


class AnnotationViewSet(viewsets.ModelViewSet):
    """ViewSet for the Annotation class"""

    queryset = models.Annotation.objects.all()
    serializer_class = serializers.AnnotationSerializer
    permission_classes = [permissions.IsAuthenticated]


class ClipViewSet(viewsets.ModelViewSet):
    """ViewSet for the Clip class"""

    queryset = models.Clip.objects.all()
    serializer_class = serializers.ClipSerializer
    permission_classes = [permissions.IsAuthenticated]


class FoodViewSet(viewsets.ModelViewSet):
    """ViewSet for the Food class"""

    queryset = models.Food.objects.all()
    serializer_class = serializers.FoodSerializer
    permission_classes = [permissions.IsAuthenticated]


class ImageViewSet(viewsets.ModelViewSet):
    """ViewSet for the Image class"""

    queryset = models.Image.objects.all()
    serializer_class = serializers.ImageSerializer
    permission_classes = [permissions.IsAuthenticated]


class LanguageViewSet(viewsets.ModelViewSet):
    """ViewSet for the Language class"""

    queryset = models.Language.objects.all()
    serializer_class = serializers.LanguageSerializer
    permission_classes = [permissions.IsAuthenticated]


class WebsiteViewSet(viewsets.ModelViewSet):
    """ViewSet for the Website class"""

    queryset = models.Website.objects.all()
    serializer_class = serializers.WebsiteSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserProfileViewSet(viewsets.ModelViewSet):
    """ViewSet for the UserProfile class"""

    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


