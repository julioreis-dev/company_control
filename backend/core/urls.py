from django.urls import path, include
from rest_framework import routers
from .views import DossieViewSet, ParamsViewsSet, LogsActionsViewsSet


router = routers.SimpleRouter()
router.register("clientes", DossieViewSet, basename="dossieview")
router.register("params", ParamsViewsSet, basename="paramsview")
router.register("logaction", LogsActionsViewsSet, basename="logsactionview")

urlpatterns = router.urls
