from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Dog, Breed
from .serializers import DogSerializer, BreedSerializer
from rest_framework import status, permissions, renderers, viewsets
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from django.contrib.auth import authenticate
from spyne import Application, rpc, ServiceBase, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoApplication
from django.views.decorators.csrf import csrf_exempt
#from .permissions import IsOwner
from rest_framework import generics

# I imported views from parvious labs, but then decided to research and go with the viewset style which is below

'''
@api_view(['GET'])
#@permission_classes([permissions.IsAuthenticated])
@renderer_classes([renderers.JSONRenderer])
def rest_get_dog(request, dog_id):
    try:
        dog = Dog.objects.get(pk=dog_id)
        if dog.owner != request.user:
            return Response({'error': 'You do not have permission to view this dog.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = DogSerializer(dog)
        return Response(serializer.data)
    except Dog.DoesNotExist:
        return Response({'error': 'Dog not found.'}, status=status.HTTP_404_NOT_FOUND)
    
class DogDetailAPIView(generics.RetrieveAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    #permission_classes = [permissions.IsAuthenticated, IsOwner]
    

def authenticate_user(request):
    """
    Authenticates a user using HTTP Basic Authentication.

    Returns:
        user (User): The authenticated user object, or None if authentication fails.
        error_response (tuple): A tuple containing the HTTP status code and message if authentication fails.
    """
    if 'HTTP_AUTHORIZATION' in request:
        auth = request['HTTP_AUTHORIZATION'].split()
        if len(auth) == 2 and auth[0].lower() == 'basic':
            import base64
            try:
                username, password = base64.b64decode(auth[1]).decode('utf-8').split(':')
                user = authenticate(username=username, password=password)
                if user is not None and user.is_authenticated:
                    return user, None
            except (UnicodeDecodeError, ValueError):
                pass

    # Authentication failed
    return None, (401, 'Unauthorized', {'WWW-Authenticate': 'Basic realm="DogService"'})


class DogService(ServiceBase):
    @rpc(Integer, _returns=Unicode)
    def get_dog(ctx, dog_id):
        request = ctx.transport.req
        user = None
        
        user, error_response = authenticate_user(request)
        # Get the Basic Auth credentials
        if user is None:
            status_code, message, headers = error_response
            ctx.transport.resp_code = status_code
            for header, value in headers.items():
                ctx.transport.resp_headers[header] = value
            return message

        try:
            dog = Dog.objects.get(pk=dog_id)
            if dog.owner != user:
                return f"You do not have permission to view this dog."
            return f"Dog: {dog.name}, Age: {dog.age}, Breed: {dog.breed}"
        except Dog.DoesNotExist:
            return "Dog not found."
'''        



class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer


class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
