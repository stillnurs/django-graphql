from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from graphene_django.views import GraphQLView

from .schema import schema

urlpatterns = [
    # Only single URL to access GraphQL
    path('graphql', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]
