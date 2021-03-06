from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework_jwt.views import ObtainJSONWebToken

from rest_framework.settings import api_settings
from rest_framework.permissions import AllowAny
from user.serializers import UserSerializer, AuthTokenSerializer


class CreateUserView(generics.CreateAPIView):

    permission_classes = (AllowAny,)
    # create a new user in the system
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):

    # create new auth token for user
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

# class CreateTokenView(ObtainJSONWebToken):

#     # create new auth token for user
#     serializer_class = AuthTokenSerializer
#     renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):

    # manage the authenticated user
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        # retrieve and return authenticated user
        return self.request.user
