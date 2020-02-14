"""myblogsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from articles import views as articles_views
from accounts import views as accounts_views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', articles_views.guest_articles_view),
    path('viewallarticles/',
    articles_views.all_articles_view,
    name = 'viewallarticles'),
    path('createnewarticle/',
    articles_views.create_article_view,
    name = 'createnewarticle'),
    path('articledetails/<article_id>',
    articles_views.article_details_view,
    name = 'articledetails'),
    path('updatearticle/<article_id>',
    articles_views.update_article_view,
    name = 'updatearticle'),
    path('deletearticle/<article_id>',
    articles_views.delete_article_view,
    name = 'deletearticle'),
    path('register/', accounts_views.register_view,
    name = 'register'),
    path('login/', accounts_views.login_view,
    name = 'login'),
    path('viewprofile/', accounts_views.profile_view,
    name = 'viewprofile'),
    path('editprofile/',
    accounts_views.edit_profile_view,
    name = 'editprofile'),
    path('changepassword/', accounts_views.change_password_view,
    name = 'changepassword'),
    path('password-reset/',
    auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
    name = 'password_reset'),
    path('password-reset/done/',
    auth_views.PasswordResetDoneView.as_view(template_name='reset_password_done.html'),
    name = 'password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name='reset_password_confirm.html'),
    name = 'password_reset_confirm'),
    path('password-reset/complete/',
    auth_views.PasswordResetCompleteView.as_view(template_name='reset_password_complete.html'),
    name = 'password_reset_complete'),
    path('logout/', accounts_views.logout_view,
    name = 'logout'),
    path('guestarticles/',
    articles_views.guest_articles_view,
    name = 'guestarticles'),
    path('guestarticledetails/<article_id>',
    articles_views.guest_article_details,
    name = 'guestarticledetails'),
] + static(settings.MEDIA_URL,
document_root = settings.MEDIA_ROOT)
