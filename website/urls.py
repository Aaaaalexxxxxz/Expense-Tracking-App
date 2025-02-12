from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('/login', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('add_record/', views.add_record, name='add_record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('report/', views.report, name='report'),
    path('view_recurring_records', views.view_recurring_records, name='view_recurring_records'),
    #path('delete_recurring_record/<int:pk>', views.delete_recurring_record, name='delete_recurring_record'),
]