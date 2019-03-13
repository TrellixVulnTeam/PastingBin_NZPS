#urls.py
from django.urls import path
from django.contrib import admin
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('admin/', admin.site.urls),
    path('createpost/', views.createpost),
    path('createaccount/', views.createaccount),
    path('dashboard/', views.dashboard, name='dashboard')
]
urlpatterns += [
    path('<int:pk>/update/', views.UserUpdate.as_view(), name='user_update'),
    path('<int:pk>/delete/', views.UserDelete.as_view(), name='user_delete'),
]
