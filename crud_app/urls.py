from django.urls import path
from .views import create_token, create_item, get_items, delete_item, update_item
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('create/', create_item, name='create-item'),
    path('list/', get_items, name='list-items'),
    path('delete/<int:pk>/', delete_item, name='delete-item'),
    path('update/<int:pk>/', update_item, name='update-item'),
]
