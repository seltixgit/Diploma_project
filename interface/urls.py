from django.urls import path
from django.contrib.auth.views import LogoutView
from interface.views import (
    HomeView,
    UserCreateView,
    AuthCodeForm,
    UserDetailView,
    UserUpdateView,
    UserListView,
)
from interface.apps import InterfaceConfig

app_name = InterfaceConfig.name

urlpatterns = [
    path("logout/", LogoutView.as_view(next_page="interface:index"), name="logout"),
    path("", HomeView.as_view(), name="index"),
    path("login/", UserCreateView.as_view(), name="login"),
    path("verificat/", AuthCodeForm.as_view(), name="verificat"),
    path("user_detail/", UserDetailView.as_view(), name="user_detail"),
    path("user_update/", UserUpdateView.as_view(), name="user_update"),
    path("user_list/", UserListView.as_view(), name="user_list"),
]
