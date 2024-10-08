from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

# We can do create, update and delete all together because of router
router = DefaultRouter()

router.register('', views.ServiceViewSet) # antena of router

urlpatterns = [
    path('', include(router.urls)),
]