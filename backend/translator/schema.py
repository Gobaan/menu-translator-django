import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_file_upload.scalars import Upload
from backend.translator.models import Annotation, Clip, Image, Language, Website, Food, UserProfile

class AnnotationNode(DjangoObjectType):
    class Meta:
        model = Annotation
        filter_fields = []
        interfaces = (graphene.relay.Node, )

class ClipNode(DjangoObjectType):
    class Meta:
        model = Clip
        filter_fields = []
        interfaces = (graphene.relay.Node, )

class ImageNode(DjangoObjectType):
    class Meta:
        model = Image
        filter_fields = []
        interfaces = (graphene.relay.Node, )

class LanguageNode(DjangoObjectType):
    class Meta:
        model = Language
        filter_fields = []
        interfaces = (graphene.relay.Node, )

class WebsiteNode(DjangoObjectType):
    class Meta:
        model = Website
        filter_fields = []
        interfaces = (graphene.relay.Node, )

class FoodNode(DjangoObjectType):
    class Meta:
        model = Food
        filter_fields = []
        interfaces = (graphene.relay.Node, )

class UserNode(DjangoObjectType):
    class Meta:
        model = UserProfile
        filter_fields = []
        interfaces = (graphene.relay.Node, )

class CreateImage(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        longitude = graphene.Int()
        latitude = graphene.Int()
        picture = Upload(required=True)

    # The class attributes define the response of the mutation
    image = graphene.Field(ImageNode)

    def mutate(self, info, longitude, latitude, picture):
        if not latitude:
            print ("hmm")
        image = Image()
        image.longitude = longitude
        image.latitude = latitude
        image.width = 0
        image.height = 0
        image.filesize = 50
        image.save()

        return CreateImage(image=image)

class Query(graphene.ObjectType):
    annotation = graphene.relay.Node.Field(AnnotationNode)
    clip = graphene.relay.Node.Field(ClipNode)
    image = graphene.relay.Node.Field(ImageNode)
    language = graphene.relay.Node.Field(LanguageNode)
    website = graphene.relay.Node.Field(WebsiteNode)
    food = graphene.relay.Node.Field(FoodNode)
    users = graphene.relay.Node.Field(UserNode)
 
    all_images = DjangoFilterConnectionField(ImageNode)
    all_foods = DjangoFilterConnectionField(FoodNode)
    all_users = DjangoFilterConnectionField(UserNode)

class Mutations(graphene.ObjectType):
    create_image = CreateImage.Field()
