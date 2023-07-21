from django.urls import path, re_path

from post import views

app_name='post'
urlpatterns=[
    path('', views.PostLV.as_view(), name='post_list'),
    path('<int:pk>/', views.PostDV.as_view(), name='post_detail'),
    re_path(r'(?P<pk>[0-9]+)/$', views.PostDV.as_view(), name='post_detail'),
    path('add/', views.PostCV.as_view(), name = 'post_add'),
    path('search/', views.SearchFormView.as_view(), name='search'),
    path('change/', views.PostChangeLV.as_view(), name = 'change'),
    path('<int:pk>/delete/', views.PostDelV.as_view(), name = 'delete'),
    path('<int:pk>/update/', views.PostUV.as_view(), name='update'),
]