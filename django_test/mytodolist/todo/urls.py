from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('<int:pk>/', views.todo_detail, name='todo_detail'),
    path('post/', views.todo_post, name="todo_post"),
    path('todo/<int:pk>/edit/', views.todo_edit, name='todo_edit'),
    path('done/', views.todo_done_list, name='todo_done_list'),
    path('todo/done/<int:pk>', views.todo_done, name='todo_done'),
]