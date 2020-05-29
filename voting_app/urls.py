from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('host_event_page/', views.host_event_page, name='host_event_page'),
    path('participate_to_vote/', views.participate_to_vote, name='participate_to_vote'),
    path('event_page/<event_code>/', views.event_page, name='event_page'),
    path('dashboard/', views.dashboard, name='dashboard'),
]