from django.urls import path
from contributions.views import (
    AddContributionAPIView,MemberContributionsAPIView,
    RoomContributionsAPIView,ContributionDetailAPIView
)

urlpatterns= [
    path('add-contribution/',AddContributionAPIView.as_view(),name="add-contribution"),
    path('my-contributions/',MemberContributionsAPIView.as_view(),name="my-contributions"),
    path('room-contributions/',RoomContributionsAPIView.as_view(),name="room-contributions"),
    path('edit-contribution/<str:pk>/',ContributionDetailAPIView.as_view(),name="edit-contribution"),
    path('delete-contribution/<str:pk>/',ContributionDetailAPIView.as_view(),name="delete-contribution"),
]