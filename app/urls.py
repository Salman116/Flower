from django.urls import path
from .views import *

urlpatterns = [
    # Authentication
    path("", DefaultAPI.as_view(), name=""),
    path("dummy", DummpAPI.as_view(), name="dummp"),
    path("task-result/<str:task_id>/", TaskResultAPI.as_view(), name="task-result"),
]