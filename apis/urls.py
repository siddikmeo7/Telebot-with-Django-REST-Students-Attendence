from django.urls import path
from .views import *

urlpatterns = [
    path("user/", UserListAPIView.as_view(), name="user-list"),
    path("user/create", UserCreateAPIView.as_view(), name="user-create"),
    path("user/<int:pk>", UserRetrieveAPIView.as_view(), name="user-detail"),
    path("user/<int:pk>/update", UserRetrieveUpdateAPIView.as_view(), name="user-update"),
    path("user/<int:pk>/delete", UserDeleteAPIView.as_view(), name="user-delete"),


    path("group/", GroupListAPIView.as_view(), name="group-list"),
    path("group/create", GroupCreateAPIView.as_view(), name="group-create"),
    path("group/<int:pk>", GroupRetrieveAPIView.as_view(), name="group-detail"),
    path("group/<int:pk>/update", GroupRetrieveUpdateAPIView.as_view(), name="group-update"),
    path("group/<int:pk>/delete", GroupDeleteAPIView.as_view(), name="group-delete"),


    path("attenden/", AttendenListAPIView.as_view(), name="attenden-list"),
    path("attenden/create", AttendenCreateAPIView.as_view(), name="attenden-create"),
    path("attenden/<int:pk>", AttendenRetrieveAPIView.as_view(), name="attenden-detail"),
    path("attenden/<int:pk>/update", AttendenRetrieveUpdateAPIView.as_view(), name="attenden-update"),
    path("attenden/<int:pk>/delete", AttendenDeleteAPIView.as_view(), name="attenden-delete"),

]
