from django.urls import path
#importing from the base app 
from . import views
#importing from the posts app
from HNC_posts.views import home, submit, vote, post

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('', home, name='homePage'),
    path('post/<str:post_id>/vote/', vote, name='vote'),
    path('post/<str:post_id>/', post, name='post'),
    path('submit/', submit, name='submit')
]