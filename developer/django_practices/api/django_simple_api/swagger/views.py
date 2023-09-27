from rest_framework.views import APIView
from drf_spectacular.utils import (extend_schema,
                                   OpenApiParameter,
                                   OpenApiExample,
                                   inline_serializer)
from drf_spectacular.types import OpenApiTypes
from rest_framework import serializers


class Swagger(APIView):

    @extend_schema(
        tags=['swagger-custom'],
        parameters=[OpenApiParameter(name='artist', description='Filter by artist', required=False, type=str)],
        responses=inline_serializer( 
            name='SwaggerCustom', 
            fields={ 
                'id': serializers.IntegerField(), 
                'name': serializers.CharField(),
            },
         )
    )

    def get(self, request):
        return Response([{'id': 1, 'name': 'admin'}, {'id': 2, 'name': 'user_test'}])

    @extend_schema(
        tags=['swagger-custom'],
        parameters=[OpenApiParameter(name='artist', description='Filter by artist', required=False, type=str)],
        request=inline_serializer( 
            name='SwaggerCustomPost', 
            fields={ 
                'id': serializers.IntegerField(), 
                'name': serializers.CharField(),
            },
        ),
        responses=inline_serializer( 
            name='post', 
            fields={ 
                'id': serializers.IntegerField(), 
                'name': serializers.CharField(),
            },
         )
    )

    def post(self, request):
        return None

    @extend_schema(
        tags=['swagger-custom'],
        parameters=[OpenApiParameter(name='artist', description='Filter by artist', required=False, type=str)],
        responses=inline_serializer( 
            name='put', 
            fields={ 
                'id': serializers.IntegerField(), 
                'name': serializers.CharField(),
            },
         )
    )

    def put(self, request):
        return None

    @extend_schema(
        tags=['swagger-custom'],
        parameters=[OpenApiParameter(name='artist', description='Filter by artist', required=False, type=str)],
        responses=inline_serializer( 
            name='patch', 
            fields={ 
                'id': serializers.IntegerField(), 
                'name': serializers.CharField(),
            },
         )
    )

    def patch(self, request):
        return None

    @extend_schema(
        tags=['swagger-custom'],
        parameters=[OpenApiParameter(name='artist', description='Filter by artist', required=False, type=str)],
        responses=inline_serializer( 
            name='delete', 
            fields={ 
                'id': serializers.IntegerField(), 
                'name': serializers.CharField(),
            },
         )
    )

    def delete(self, request):
        return None



