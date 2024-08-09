from django.urls import path

from .views import AddUser, VerifyAddedUser

urlpatterns = [
    path('add_user/', AddUser.as_view(), name='add_user'),
    path('verify_added_user/', VerifyAddedUser.as_view())
]