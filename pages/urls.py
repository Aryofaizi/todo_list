from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home_page"),
    path("mark_task/<int:pk>/", views.mark_task, name="mark_task"),
    path("delete_task/<int:pk>/", views.delete_task, name="delete_task" ),
    path("edit_task/<int:pk>/", views.edit_task, name="edit_task")
]
