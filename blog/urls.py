from django.urls import path, include
from . import views
from django.contrib import admin


urlpatterns = [
    # 127.0.0.1:8000(local) this is where this takes you
    # my.djangosite.com(online)
    path('', views.post_list, name='post_list'),
    
    # 127.0.0.1:8000/post/2 
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

    # 127.0.0.1:8000/post/new(local)
    path('post/new/', views.post_new, name='post_new'),

    #127.0.0.1:8000/post/2/edit(local)
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

    #127.0.0.1:8000/drafts(local)
    path('drafts/', views.post_draft_list, name='post_draft_list'),

    #127.0.0.1:8000/publish/(local)
    path('post/<int:pk>/publish/', views.post_publish, name="post_publish"),

    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]

