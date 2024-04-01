# blog/urls.py
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import BlogCrudView, AuthorCrudView,EntryCrudView
#UserDetailsView, ProfileView


urlpatterns = [
    path('posts/', BlogCrudView.as_view(), name='post-list'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('authors/', AuthorCrudView.as_view(), name='authors'),
    path('entries/', EntryCrudView.as_view(), name='entries')

#     path('user-details/' , UserDetailsView.as_view(), name='user-details'),
#     path('profile/', ProfileView.as_view(), name='profile'),
#     # Add other endpoints as needed
]

