from django.urls import path, include
from .views import ContactCreateAPIView, ContactListAPIView,ContactUpdateApiView, DeleteApiView, ContactViewSet, test
from rest_framework.routers import DefaultRouter, SimpleRouter

urlpatterns = [
    path('', ContactListAPIView.as_view(), name = 'contact_listview'),
    path('/create', ContactCreateAPIView.as_view(), name = 'contact_create'),
    path('/<int:pk>/update', ContactUpdateApiView.as_view(), name = 'contact_update'),
    path('/<int:pk>/delete', DeleteApiView.as_view(), name = 'contact_delete'),
    path('/test', test, name = 'contact_delete22'),
]

router = SimpleRouter()
router.register(r'/contact2',viewset=ContactViewSet, basename='contact')
urlpatterns += router.urls