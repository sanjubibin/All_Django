from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.shortcuts import redirect

from .data import Dataa

# Create your views here.
class RedirectHome(View):
    def get(self, request):
        return redirect(Dataa['Index']['url'])

class Index(View):
    def get(self, request):
        return render(request, 'htmls/100day_common.html', Dataa['Index']['for_render'])
    
class Day1(View):
    def get(self, request):
        return render(request, 'htmls/100day_common.html', Dataa['Day1']['for_render'])