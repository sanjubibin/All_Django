from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.shortcuts import redirect

from .data import Dataa

# Create your views here.
class RedirectHome(View):
    def get(self, request):
        return redirect(Dataa['Urls']['Index_url'])

class Index(View):
    def get(self, request):
        return render(request, 'htmls/100day_common.html', Dataa['Index']['for_render'])

class DaysAuto(View):
    def get(self, request, day_url: str):
        has_day = False
        for key, data in Dataa.items():
            if key.lower() == day_url.lower():
                has_day = True
        if not has_day:
            msg = f'{day_url} challenges is still under learning'
        else:
            msg = f'Here is the challenges for {day_url}'
        return render(request, 'htmls/100day_daysauto.html', {'day': msg})
    
class Day1(View):
    def get(self, request):
        data = Dataa['Day1']['for_render']
        return render(request, 'htmls/100day_day1.html', data)