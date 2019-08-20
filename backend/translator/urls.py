from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'annotation', api.AnnotationViewSet)
router.register(r'clip', api.ClipViewSet)
router.register(r'food', api.FoodViewSet)
router.register(r'image', api.ImageViewSet)
router.register(r'language', api.LanguageViewSet)
router.register(r'website', api.WebsiteViewSet)
router.register(r'userprofile', api.UserProfileViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Annotation
    path('translator/annotation/', views.AnnotationListView.as_view(), name='translator_annotation_list'),
    path('translator/annotation/create/', views.AnnotationCreateView.as_view(), name='translator_annotation_create'),
    path('translator/annotation/detail/<slug:slug>/', views.AnnotationDetailView.as_view(), name='translator_annotation_detail'),
    path('translator/annotation/update/<slug:slug>/', views.AnnotationUpdateView.as_view(), name='translator_annotation_update'),
)

urlpatterns += (
    # urls for Clip
    path('translator/clip/', views.ClipListView.as_view(), name='translator_clip_list'),
    path('translator/clip/create/', views.ClipCreateView.as_view(), name='translator_clip_create'),
    path('translator/clip/detail/<slug:slug>/', views.ClipDetailView.as_view(), name='translator_clip_detail'),
    path('translator/clip/update/<slug:slug>/', views.ClipUpdateView.as_view(), name='translator_clip_update'),
)

urlpatterns += (
    # urls for Food
    path('translator/food/', views.FoodListView.as_view(), name='translator_food_list'),
    path('translator/food/create/', views.FoodCreateView.as_view(), name='translator_food_create'),
    path('translator/food/detail/<slug:slug>/', views.FoodDetailView.as_view(), name='translator_food_detail'),
    path('translator/food/update/<slug:slug>/', views.FoodUpdateView.as_view(), name='translator_food_update'),
)

urlpatterns += (
    # urls for Image
    path('translator/image/', views.ImageListView.as_view(), name='translator_image_list'),
    path('translator/image/create/', views.ImageCreateView.as_view(), name='translator_image_create'),
    path('translator/image/detail/<slug:slug>/', views.ImageDetailView.as_view(), name='translator_image_detail'),
    path('translator/image/update/<slug:slug>/', views.ImageUpdateView.as_view(), name='translator_image_update'),
)

urlpatterns += (
    # urls for Language
    path('translator/language/', views.LanguageListView.as_view(), name='translator_language_list'),
    path('translator/language/create/', views.LanguageCreateView.as_view(), name='translator_language_create'),
    path('translator/language/detail/<slug:slug>/', views.LanguageDetailView.as_view(), name='translator_language_detail'),
    path('translator/language/update/<slug:slug>/', views.LanguageUpdateView.as_view(), name='translator_language_update'),
)

urlpatterns += (
    # urls for Website
    path('translator/website/', views.WebsiteListView.as_view(), name='translator_website_list'),
    path('translator/website/create/', views.WebsiteCreateView.as_view(), name='translator_website_create'),
    path('translator/website/detail/<slug:slug>/', views.WebsiteDetailView.as_view(), name='translator_website_detail'),
    path('translator/website/update/<slug:slug>/', views.WebsiteUpdateView.as_view(), name='translator_website_update'),
)

urlpatterns += (
    # urls for UserProfile
    path('translator/userprofile/', views.UserProfileListView.as_view(), name='translator_userprofile_list'),
    path('translator/userprofile/create/', views.UserProfileCreateView.as_view(), name='translator_userprofile_create'),
    path('translator/userprofile/detail/<slug:slug>/', views.UserProfileDetailView.as_view(), name='translator_userprofile_detail'),
    path('translator/userprofile/update/<slug:slug>/', views.UserProfileUpdateView.as_view(), name='translator_userprofile_update'),
)

