from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Annotation, Clip, Food, Image, Language, Website, UserProfile
from .forms import AnnotationForm, ClipForm, FoodForm, ImageForm, LanguageForm, WebsiteForm, UserProfileForm


class AnnotationListView(ListView):
    model = Annotation


class AnnotationCreateView(CreateView):
    model = Annotation
    form_class = AnnotationForm


class AnnotationDetailView(DetailView):
    model = Annotation


class AnnotationUpdateView(UpdateView):
    model = Annotation
    form_class = AnnotationForm


class ClipListView(ListView):
    model = Clip


class ClipCreateView(CreateView):
    model = Clip
    form_class = ClipForm


class ClipDetailView(DetailView):
    model = Clip


class ClipUpdateView(UpdateView):
    model = Clip
    form_class = ClipForm


class FoodListView(ListView):
    model = Food


class FoodCreateView(CreateView):
    model = Food
    form_class = FoodForm


class FoodDetailView(DetailView):
    model = Food


class FoodUpdateView(UpdateView):
    model = Food
    form_class = FoodForm


class ImageListView(ListView):
    model = Image


class ImageCreateView(CreateView):
    model = Image
    form_class = ImageForm


class ImageDetailView(DetailView):
    model = Image


class ImageUpdateView(UpdateView):
    model = Image
    form_class = ImageForm


class LanguageListView(ListView):
    model = Language


class LanguageCreateView(CreateView):
    model = Language
    form_class = LanguageForm


class LanguageDetailView(DetailView):
    model = Language


class LanguageUpdateView(UpdateView):
    model = Language
    form_class = LanguageForm


class WebsiteListView(ListView):
    model = Website


class WebsiteCreateView(CreateView):
    model = Website
    form_class = WebsiteForm


class WebsiteDetailView(DetailView):
    model = Website


class WebsiteUpdateView(UpdateView):
    model = Website
    form_class = WebsiteForm


class UserProfileListView(ListView):
    model = UserProfile


class UserProfileCreateView(CreateView):
    model = UserProfile
    form_class = UserProfileForm


class UserProfileDetailView(DetailView):
    model = UserProfile


class UserProfileUpdateView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm

