from django.urls import path
from .views import (
	contactDetailView,
	contactListView,
	contactCreateView,
	contactUpdateView,
	contactDeleteView
	
	)
from . import views


urlpatterns = [
    path('', contactListView.as_view(), name='blog-home'),
    path('post/<int:pk>', contactDetailView.as_view(), name='contact-detail'),
    path('create/', contactCreateView.as_view(), name='contact-button'),
    path('post/<int:pk>/update/', contactUpdateView.as_view(), name='contact-update'),
    path('post/<int:pk>/delete/', contactDeleteView.as_view(), name='contact-delete'),
    path('about', views.about, name='blog-about'),
    ]