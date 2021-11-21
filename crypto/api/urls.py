from django.urls import path, include
from .views import ContactViewSet, FeedbackViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('contact', ContactViewSet, basename = 'contact')
router.register('feedback', FeedbackViewSet, basename='feedback')

urlpatterns = [
    path('api/', include(router.urls))
]
