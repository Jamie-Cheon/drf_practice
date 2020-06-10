from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from .models import Snippet
from .permissions import IsOwnerOrReadOnly
from .serializers import SnippetSerializer


# ************** Custom classes ************** #

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


class CustomSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        if request.query_params.get('code_only'):
            return ['code']
        return super(CustomSearchFilter, self).get_search_fields(view, request)


# ************** Viewsets ************** #

class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated,
                          IsOwnerOrReadOnly]

    filter_backends = [CustomSearchFilter]
    search_fields = ['code']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



