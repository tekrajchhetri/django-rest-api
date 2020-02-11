from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework import status
from profiles_api import serializer

class HelloAPIView(APIView):
    """Test API view"""

    serializer_class = serializer.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        apiview=[
            'use http method as function (get, post, patch,put,delete)',
            'similar to django view',
            'gives control over application',
            'this is it for test',
        ]

        return Response({'message':'hello','api_view':apiview})

    def post(self, request):
        """create hello message with our name"""
        serializer= self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}"
            return Response({"message":message})
        else:
            return  Response( serializer.errors,
                status = 400)

    def put(self, request, pk=None):
        """Handle updating an update"""
        return Response({"method":"PUT"})

    def patch(self, request, pk=None):
        """Handles a partial update of an object"""
        return Response({"method": "PATCH"})

    def delete(self, request, pk=None):
        """Deletes an object"""
        return Response({"message": "delete"})
