from django.urls import path
from . import views #import the current direct views(home/views.py)

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('portfolio/',  views.portfolio.as_view(), name='portfolio'),
    path('portfolio/post/<int:pk>', views.PostDetail.as_view(), name='post_detail')
]
