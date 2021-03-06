from django.urls import path
from rooms.views import (
    AddRoomAPIView,AllRoomsAPIView,
    MemberRoomsAPIView,IndividualRoomAPIView,RoomDetailAPIView
)

urlpatterns= [
    path('add-room/',AddRoomAPIView.as_view(),name="add-room"),
    path('all-rooms/',AllRoomsAPIView.as_view(),name="all-rooms"),
    path('my-rooms/',MemberRoomsAPIView.as_view(),name="my-rooms"),
    path('room/<str:pk>/',IndividualRoomAPIView.as_view(),name="individual-room"),
    path('edit-room/<str:pk>/',RoomDetailAPIView.as_view(),name="edit-room"),
    path('delete-room/<str:pk>/',RoomDetailAPIView.as_view(),name="delete-room")
]