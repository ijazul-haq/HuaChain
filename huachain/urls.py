from django.contrib import admin
from django.urls import path, include
from website import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('gallery/', views.gallery, name='gallery'),
    path('collection/', views.collection, name='collection'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_reg/', views.user_reg, name='user_reg'),
    path('artwork_reg/', views.artwork_reg, name='artwork_reg'),
    path('log_out/', views.log_out, name='log_out'),
    path('', views.index, name='index'),
]
