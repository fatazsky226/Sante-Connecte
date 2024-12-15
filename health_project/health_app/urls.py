from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, MedicalHistoryViewSet, ConsultationViewSet
from . import views

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('medical_histories', MedicalHistoryViewSet)
router.register('consultations', ConsultationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('manage-users/', views.manage_users, name='manage_users'),
    path('users/', views.user_list, name='user_list'),
]


