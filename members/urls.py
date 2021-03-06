from django.urls import path
from members.views import (
    RegisterAPIView,EditMemberAPIView,MemberAPIView,
    MembersAPIView,MemberDetailAPIView,DeleteAccountAPIView
)
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns=[
    path('register/',RegisterAPIView.as_view(),name="register"),
    path('login/',TokenObtainPairView.as_view(),name="login"),
    path('refresh-login/',TokenRefreshView.as_view(),name="refresh-login"),
    path('edit-member/',EditMemberAPIView.as_view(),name="edit-member"),
    path('member/',MemberAPIView.as_view(),name="current-member"),
    path('members/',MembersAPIView.as_view(),name="all-members"),
    path('member/<str:pk>/',MemberDetailAPIView.as_view(),name="individual-member"),
    path('delete-account/',DeleteAccountAPIView.as_view(),name="delete-account"),
]