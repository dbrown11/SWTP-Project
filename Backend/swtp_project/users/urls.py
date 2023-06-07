from django.urls import path

from swtp_project.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
)

from swtp_project.users.map import render_map

from swtp_project.users.collector import test_collector

app_name = "users"
urlpatterns = [
    path("~collector/", view=test_collector, name="collector"),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
