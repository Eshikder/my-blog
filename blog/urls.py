from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('editor',views.editor, name='editor'),
    path('cv',views.cv, name='cv'),
]