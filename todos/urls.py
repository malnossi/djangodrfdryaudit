from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(prefix=r"todos", viewset=views.TodoViewSet, basename="todos")


urlpatterns = router.urls
