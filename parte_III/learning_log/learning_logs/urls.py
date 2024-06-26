"""Defines url patterns for learning_logs."""

from django.urls import path
from . import views

urlpatterns = [
    # Home page.
    path('', views.index, name='index'),

    # Show all topics.
    path('topics/', views.topics, name='topics'),

    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # URL para novo tópico
    path('new_topic/', views.new_topic, name='new_topic'),

]
