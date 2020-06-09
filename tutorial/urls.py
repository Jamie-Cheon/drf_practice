from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from snippets.views import CustomAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('snippets.urls')),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
    url(r'^api-token-auth/', CustomAuthToken.as_view())
]
