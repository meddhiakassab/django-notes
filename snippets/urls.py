from django.urls import path
from snippets import views


urlpatterns = [
    path('getPostSnippets/', views.getAllorCreataSnippet),
    path('snippets/<int:pk>', views.oneSnippetApplication)
]
