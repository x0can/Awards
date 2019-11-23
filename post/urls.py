from . import views
from django.urls import path


urlpatterns = [
    path('post/<int:pk>/',views.PostDetailView.as_view(), name ='post-detail'),
    path('post/new/',views.PostCreateView.as_view(), name ='post-create'),



]