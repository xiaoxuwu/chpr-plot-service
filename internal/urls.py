from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('data/', views.data, name='data'),
    path('process/<int:id>', views.process, name='process'),
    path('login/', views.login_view, name='login'),
    path('login/submit/', views.login_submit_view, name='login_submit'),
    path('logout/', views.logout_view, name='logout'),
]