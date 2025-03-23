from django.urls import path
from .views import index, run_code
#import views

urlpatterns = [
    path("", index, name="index"),  # This should map to index.html
    path("run_code/", run_code, name="run_code"),
]
