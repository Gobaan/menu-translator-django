from django.test import TestCase
from backend.translator.models import *

class SchemaStructureTest(TestCase):
    fixtures = ['translator.json',]
    def testAnnotation(self):
        s = Annotation.objects.get(pk=1)
        print(s)
        assert s.text == 'Pho'
        assert s.annotates_source_language == True
        assert s.language.name == "English (United States)"
        assert s.clip.image.filesize == 300000
        assert s.creator.user.username == 'google-ocr'

    def testClip(self):
        s = Clip.objects.get(pk=2)
        assert s.annotations.all()[0].text == 'Pho'
        assert s.bounding_box == "[(30, 30), (20, 20), (10, 10), (5, 5)]"
        assert s.creator.user.username == 'google-ocr'
        assert s.image.filesize == 300000

    def testFood(self):
        s = Food.objects.get(pk=3)
        assert s.name == 'Pho'
        assert s.language.name == "English (United States)"
        assert s.creator.user.username == 'google-ocr'
        assert s.thumbnails.all()[0].cloud_URL == 'gobaan.com'
        assert s.websites.all()[0].URL == "www.recipes.com"

    def testImage(self):
        s = Image.objects.get(pk=4)
        assert s.filesize == 300000
        assert s.cloud_URL ==  "www.google.com/[TODO:Insert Image Here]"
        assert s.creator.user.username == 'google-ocr'

    def testLanguage(self):
        s = Language.objects.get(pk=5)
        assert s.name == "English (United States)"

    def testWebsite(self):
        s = Website.objects.get(pk=6)
        assert s.food.name == 'Pho'
        assert s.URL == "www.recipes.com"

    def testUserProfile(self):
        s = UserProfile.objects.get(pk=7)
        assert s.user.username == 'google-ocr'
        assert s.category == "google-api"
        assert s.user.password == 'theonetruepassword'
