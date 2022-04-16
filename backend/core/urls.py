from django.urls import path, include
from rest_framework import routers
from .views import DossieViewSet


router = routers.SimpleRouter()
router.register("clientes", DossieViewSet, basename="dossieview")

urlpatterns = router.urls
