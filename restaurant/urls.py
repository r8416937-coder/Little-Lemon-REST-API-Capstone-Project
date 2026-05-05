from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router = DefaultRouter()
router.register(r'menu-items', views.MenuViewSet, basename='menu-items')
router.register(r'bookings', views.BookingViewSet, basename='bookings')

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
    path('api/menu-items/', views.MenuViewSet.as_view({'get': 'list', 'post': 'create'}), name='menu-items'),
    path('api/menu-items/<int:pk>/', views.MenuViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='menu-item-detail'),
    path('api/bookings/', views.BookingViewSet.as_view({'get': 'list', 'post': 'create'}), name='bookings'),
    path('api/bookings/<int:pk>/', views.BookingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='booking-detail'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
