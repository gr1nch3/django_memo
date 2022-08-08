from django.urls import path
from .views import create_todo, TodoList, TodoDetail, check_todo, TodoListDone, uncheck_todo

app_name = 'todo'

urlpatterns = [
    path('', TodoList.as_view(), name='todo_list'),
    path('completed/' , TodoListDone.as_view(), name='todo_list_done'),
    path('<int:pk>/', TodoDetail.as_view(), name='todo_detail'),
    path('create/', create_todo, name='create_todo'),
    path('check/<int:pk>/', check_todo, name='check_todo'),
    path('uncheck/<int:pk>/', uncheck_todo, name='uncheck_todo'),
    
]
