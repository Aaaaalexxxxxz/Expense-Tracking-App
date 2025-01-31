from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('/login', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('add_record/', views.add_record, name='add_record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record')
    #path('show_report/', views.show_report, name='show_report')
]