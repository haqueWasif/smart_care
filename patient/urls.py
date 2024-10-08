from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

# We can do create, update and delete all together because of router
router = DefaultRouter()

router.register('list', views.PatientViewSet) # antena of router

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.UserRegistrationApiView.as_view(), name='register'),
    path('active/<uid64>/<token>/', views.activate, name = 'activate'),
    path('login/', views.UserLoginApiView.as_view(), name = 'login'),
    path('logout/', views.UserLogoutApiView.as_view(), name = 'logout'),
]