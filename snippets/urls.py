from django.urls import path
from . import views

urlpatterns = [
    path('', views.snippets, name='snippets'),
    path('snippets/<int:pk>', views.snippet_detail, name='snippet_detail'),
    path('snippets/new/', views.create_snippet, name='create_snippet'),
    path('snippets/<int:pk>/edit/', views.snippet_edit, name='snippet_edit'),
    path('snippets/<int:pk>/remove/', views.snippet_delete, name='snippet_delete'),
    path('snippets/<int:pk>/favorite/', views.add_to_library, name='add_to_library'),
    path('snippets/<int:pk>/undo_favorite/', views.delete_from_library, name='delete_from_library'),
    
    # user
    path('snippets/profile/', views.user_profile, name='user_profile'),
    
]