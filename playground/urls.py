from django.urls import path
from . import views   # ✅ PUT IT HERE

urlpatterns = [
    path("hello/", views.say_hello),
]
