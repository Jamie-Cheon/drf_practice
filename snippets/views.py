from rest_framework import viewsets, filters, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from django_filters import rest_framework as filters, BooleanFilter

from .models import Snippet
from .permissions import IsOwnerOrReadOnly
from .serializers import SnippetSerializer


class SnippetFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', method='filter_title')
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    def filter_title(self, queryset, name, value):
        lookup = Snippet.objects.filter(title__startswith=value)
        return lookup

    class Meta:
        model = Snippet
        fields = ['title', 'min_price', 'max_price']


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SnippetFilter
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



