from django.contrib import admin
from django.urls import path, include
from django.urls.resolvers import URLPattern
# from .views import todolistView, update, delete

# from .views import (
#     TodoListView,
#     TodoListCreateView,
#     TodoListUpdateView,
#     TodoListDetailView,
#     TodoListDestroyView
# )

from .views import(
    TodoListGetCreateView,
    TodoListUpdateDestroyView
    
)


urlpatterns = [
    # path('', todolistView.as_view(), name='todolist'),
    # path('update/<pk>/', update, name='update'),
    # path('delete/<pk>/', delete, name='delete'),
    
    # path('', TodoListView.as_view(), name='todolist'),
    # path('create', TodoListCreateView.as_view(), name='create'),
    # path('detail/<pk>/', TodoListUpdateView.as_view(), name='detail'),
    # path('update/<pk>/', TodoListDetailView.as_view(), name='update'),
    # path('delete/<pk>/', TodoListDestroyView.as_view(), name='delete'),
    
    path('', TodoListGetCreateView.as_view(), name='create-list'),
    path('destroy-update/<str:pk>/', TodoListUpdateDestroyView.as_view(), name='destroy-update'),
]
