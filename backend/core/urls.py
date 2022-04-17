from django.urls import path, include
from rest_framework import routers
from .views import DossieViewSet, ParamsViewsSet


router = routers.SimpleRouter()
router.register("clientes", DossieViewSet, basename="dossieview")
router.register("params", ParamsViewsSet, basename="paramsview")

urlpatterns = router.urls
