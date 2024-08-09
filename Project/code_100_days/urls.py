from django.urls import path
from django.shortcuts import redirect

from .views import (RedirectHome, Index, Day1, DaysAuto)
from .data import Dataa


urlpatterns = [
    path('', RedirectHome.as_view(), name='to_home_page'),
    path(f'{Dataa['Urls']['Index_url']}/', Index.as_view(), name=Dataa['Urls']['Index_url']),
    path(f'{Dataa['Urls']['DaysAuto_url']}/<day_url>', DaysAuto.as_view(), name=Dataa['Urls']['DaysAuto_url']),


    path(f'{Dataa['Urls']['Day1_url']}', Day1.as_view(), name=Dataa['Urls']['Day1_url'])
]