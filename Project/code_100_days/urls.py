from django.urls import path
from django.shortcuts import redirect

from .views import (RedirectHome, Index, Day1)
from .data import Dataa


urlpatterns = [
    path('', RedirectHome.as_view(), name='to_home_page'),
    path(f'{Dataa['Index']['url']}/', Index.as_view(), name=Dataa['Index']['url']),
    path(f'{Dataa['Index']['url']}/{Dataa['Day1']['url']}', Day1.as_view(), name=Dataa['Day1']['url'])
]