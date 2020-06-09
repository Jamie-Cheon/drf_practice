from django.urls import path, include
from rest_framework import routers
from snippets import views

router = routers.SimpleRouter()
router.register(r'snippets', views.SnippetViewSet)

urlpatterns = router.urls

