from django.urls import path, include
from accounts import views


urlpatterns=[
    path('login/', views.LoginView.as_view(), name="login"),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('user_profile/', views.ProfileView.as_view(), name="user_profile"),
    path('edit_profile/', views.EditProfileView.as_view(), name="edit_profile"),
    path('activate/<uidb64>/<token>/', views.ActivateAccountView.as_view(), name='activate'),
    path('', include("django.contrib.auth.urls")),
]














