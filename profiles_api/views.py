from rest_framework.views import APIView
from rest_framework.response import Response



class HelloAPIView(APIView):
    """Test Api View"""

    def get(self, request, format=None):
        """Return a list of APIView Features"""
        an_apiview = [
            'Use Http request as Function (get,put ,patch, put, delete )',
            'Is Similar to a Traditinal Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URls',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
