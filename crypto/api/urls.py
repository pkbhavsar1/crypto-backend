from django.urls import path, include
from .views import ContactUsViewSet, FeedbackViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('contact', ContactUsViewSet, basename = 'contact')
router.register('feedback', FeedbackViewSet, basename='feedback')
router.register('users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]
