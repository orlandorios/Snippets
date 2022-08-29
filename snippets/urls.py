from django.urls import path
from . import views

urlpatterns = [
    path('', views.snippets, name='snippets'),
    path('snippets/<int:pk>', views.snippet_detail, name='snippet_detail'),
    path('snippets/new/', views.create_snippet, name='create_snippet'),
    path('snippets/<int:pk>/edit/', views.snippet_edit, name='snippet_edit'),
    
]