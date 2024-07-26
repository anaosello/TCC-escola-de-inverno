from django.urls import path # type: ignore
from . import views

urlpatterns = [

    path('',views.home, name="home"),

    #Registrar usuário
    path('register',views.register, name="register"),

    #Login usuário
    path('my-login',views.my_login, name = "my-login"),

    #Dashboard
    path('dashboard',views.dashboard, name = "dashboard"),

    #Criar Tarefa
    path('create-task', views.createTask, name="create-task"),

    #Ver Tarefa
    path('view-task', views.viewTask, name="view-task"),

    #Deletar Tarefa
    path('delete-task/<str:pk>/', views.deleteTask, name="delete-task"),

    #Logout usuário
    path('user-logout',views.user_logout, name = "user-logout"),
]












