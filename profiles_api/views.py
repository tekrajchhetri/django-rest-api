from rest_framework.views import APIView
from rest_framework.response import  Response

class HelloAPIView(APIView):
    """Test API view"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        apiview=[
            'use http method as function (get, post, patch,put,delete)',
            'similar to django view',
            'gives control over application',
            'this is it for test',
        ]

        return Response({'message':'hello','api_view':apiview})