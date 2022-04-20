from django.urls import path
from topics.views import TopicAPIView,TopicsAPIView,TopicDetailAPIView

urlpatterns= [
    path('add-topic/',TopicAPIView.as_view(),name="add-topic"),
    path('all-topics/',TopicsAPIView.as_view(),name="all-topics"),
    path('edit-topic/<str:pk>/',TopicDetailAPIView.as_view(),name="edit-topic"),
    path('delete-topic/<str:pk>/',TopicDetailAPIView.as_view(),name="delete-topic"),
]