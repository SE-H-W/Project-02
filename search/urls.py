from django.urls import path
from django.contrib.auth import views as auth_views
from .views import city_suggestions, city_photo

urlpatterns = [
    path("city", city_suggestions, name="city_search"),
    path("city/photo", city_photo, name="city_photo"),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
