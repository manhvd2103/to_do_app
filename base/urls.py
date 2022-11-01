from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login/", views.UserLoginView.as_view(), name="login"), 
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"), 
    path("register/", views.UserRegister.as_view(), name="register"),
    path("", views.TaskList.as_view(), name="tasks"),
    path("task/<int:pk>/", views.TaskDetail.as_view(), name="task_detail"),
    path("task_create/", views.TaskCreate.as_view(), name="task_create"),
    path("task_update/<int:pk>", views.TaskUpdate.as_view(), name="task_update"),
    path("task_detele/<int:pk>", views.TaskDelete.as_view(), name="task_delete"),
]