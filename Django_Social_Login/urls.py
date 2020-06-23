"""Django_Social_Login URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Social_Apps import views
from Contact import views  as Contact_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home, name='home'),
    path('profile/',views.Profile, name='Profile'),
    path('', auth_views.LoginView.as_view(template_name='Social_Apps/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Social_Apps/logout.html'), name='logout'),
    path('sign-up/',views.register, name='sign_up'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='Social_Apps/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='Social_Apps/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='Social_Apps/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='Social_Apps/password_reset_complete.html'), name='password_reset_complete'),
    path('change/profile/', views.ChangeProfile.as_view(), name='change_profile'),

    path('settings/', views.SettingsView.as_view(), name='settings'),
    path('settings/password/', views.password, name='password'),
    path('oauth/', include('social_django.urls', namespace='social')),

    path('addContact/', Contact_views.addContact, name='addContact'),
    path('viewContact/', Contact_views.viewContactList.as_view(), name='viewContact'),
    path('deleteContact/<int:pk>', Contact_views.deleteContact, name='deleteContact'),
    path('editContact/<int:pk>', Contact_views.updateContact, name='editContact'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)