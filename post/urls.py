from . import views
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

from django.urls import path,include


post_list = PostViewSet.as_view({'get': 'list'})
# user\_detail = UserViewSet.as\_view({'get': 'retrieve'})













urlpatterns = [
    path('detail/<int:pk>/',views.PostDetailView.as_view(), name ='post-detail'),
    path('post/new/',views.PostCreateView.as_view(), name ='post-create'),
    path (r'^search/',views.search_results,name= 'search_results'),    
    path('api-auth/',include('rest_framework.urls', namespace='rest_framework')),
    path('post/review/<int:pk>/',views.rate, name ='post-review'),    


]