from django.urls import path # type: ignore
from . import views

urlpatterns = [

    path('',views.home, name="home"),

    #Register a user#
    path('register',views.register, name="register"),

    #Login a user#
    path('my-login',views.my_login, name = "my-login"),

    #Dashboard page#
    path('dashboard',views.dashboard, name = "dashboard"),

    #Create a Task
    path('create-task', views.createTask, name="create-task"),

    #View a Task
    path('view-task', views.viewTask, name="view-task"),

    #Delete a Task
    path('delete-task/<str:pk>/', views.deleteTask, name="delete-task"),

    #Logout a user#
    path('user-logout',views.user_logout, name = "user-logout"),
]












