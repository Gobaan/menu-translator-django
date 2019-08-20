import graphene
from graphene_django.debug import DjangoDebug
import backend.translator.schema

class Query(backend.translator.schema.Query, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='_debug')

class Mutation(backend.translator.schema.Mutations, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='_debug')

schema = graphene.Schema(query=Query, mutation=Mutation)
